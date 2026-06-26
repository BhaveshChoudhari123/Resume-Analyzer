from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from .models import EmailVerification
from .utils import generate_otp
from django.contrib import messages
from django.contrib.auth import logout

import re


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if len(password1) < 8:
             messages.error(
                  request,
                  "Password must be at least 8 characters long."
             )
             return redirect("register")

        if not re.search(r"[A-Z]", password1):
            messages.error(
                 request, 
                 "Password must contain at least one uppercase letter."
             )
            return redirect("register")
        
        if not re.search(r"[a-z]", password1):
             messages.error(
                 request,
                 "Password must contain at least one lowercase letter."
             )
             return redirect("register")

        if not re.search(r"\d", password1):
             messages.error(
                 request,
                 "Password must contain at least one number."
             )
             return redirect("register")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password1):
             messages.error(
                 request, 
                  "Password must contain at least one special character."
             )
             return redirect("register") 


        if not username:
            messages.error(request, "Username is required")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        otp = generate_otp()

        EmailVerification.objects.create(
           user=user,
           otp=otp
        )
        
        send_mail(
            subject="Resume Analyzer Email Verification",
            message=f"Your OTP is: {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(
            request,
            "OTP sent to your email. Please verify your account."
        )

        request.session["pending_user"] = user.username

        return redirect("verify_otp")

    return render(request, "register.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            verification = EmailVerification.objects.filter(
                user=user
            ).first()

            if verification and not verification.is_verified:

               messages.error(
                   request,
                   "Please verify your email before logging in."
               )

               return redirect("verify_otp")

            login(request, user)

            messages.success(
               request,
               f"Welcome {username}"
            )

            return redirect("/")

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, "login.html")


def logout_view(request):
    logout(request)

    messages.success(
        request,
        "Logged Out Successfully!"
    )

    return redirect("login")
    
from .models import EmailVerification

def verify_otp(request):

    if request.method == "POST":

        username = request.session.get("pending_user")
        entered_otp = request.POST.get("otp")

        try:
            user = User.objects.get(username=username)

            verification = EmailVerification.objects.get(user=user)

            expiry_time = verification.created_at + timedelta(minutes=5)

            if timezone.now() > expiry_time:

               messages.error(
                   request,
                   "OTP has expired. Please request a new OTP."
               )

               return redirect("verify_otp")

            if verification.otp == entered_otp:

                verification.is_verified = True
                verification.save()

                messages.success(
                    request,
                    "Email verified successfully. Please login."
                )

                return redirect("login")

            else:

                messages.error(
                    request,
                    "Invalid OTP."
                )

        except User.DoesNotExist:

            messages.error(
                request,
                "User not found."
            )

        except EmailVerification.DoesNotExist:

            messages.error(
                request,
                "Verification record not found."
            )

    return render(
        request,
        "verify_otp.html"
    )


def resend_otp(request):

    username = request.session.get("pending_user")

    if not username:

        messages.error(
            request,
            "Session expired. Please register again."
        )

        return redirect("register")

    user = User.objects.get(username=username)

    verification = EmailVerification.objects.get(user=user)

    otp = generate_otp()

    verification.otp = otp
    verification.created_at = timezone.now()
    verification.save()

    send_mail(
        subject="Resume Analyzer Email Verification",
        message=f"Your new OTP is: {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )

    messages.success(
        request,
        "A new OTP has been sent to your email."
    )

    return redirect("verify_otp")


def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")

        try:

            user = User.objects.get(email=email)

        except User.DoesNotExist:

            messages.error(
                request,
                "Email is not registered."
            )

            return redirect("forgot_password")

        otp = generate_otp()

        verification, created = EmailVerification.objects.get_or_create(
            user=user
        )

        verification.otp = otp
        verification.is_verified = False
        verification.created_at = timezone.now()
        verification.save()

        request.session["reset_user"] = user.username

        send_mail(

            subject="Password Reset OTP",

            message=f"Your OTP is: {otp}",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[email],

            fail_silently=False

        )

        messages.success(
            request,
            "OTP sent successfully."
        )

        return redirect("verify_otp")

    return render(
        request,
        "forgot_password.html"
    )


def reset_password(request):

    if request.method == "POST":

        otp = request.POST.get("otp")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("reset_password")

        username = request.session.get("reset_user")

        if not username:

            messages.error(
                request,
                "Session expired."
            )

            return redirect("forgot_password")

        user = User.objects.get(username=username)

        verification = EmailVerification.objects.get(user=user)

        if verification.otp != otp:

            messages.error(
                request,
                "Invalid OTP."
            )

            return redirect("reset_password")

        expiry_time = verification.created_at + timedelta(minutes=5)

        if timezone.now() > expiry_time:

            messages.error(
                request,
                "OTP expired."
            )

            return redirect("forgot_password")

        user.set_password(password1)
        user.save()

        verification.otp = ""
        verification.save()

        messages.success(
            request,
            "Password changed successfully."
        )

        return redirect("login")

    return render(
        request,
        "reset_password.html"
    )