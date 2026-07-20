from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail

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
            messages.error(
                request,
                "Username is required"
            )
            return redirect("register")

        if password1 != password2:
            messages.error(
                request,
                "Passwords do not match"
            )
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Username already exists"
            )
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                "Email already registered"
            )
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(
            request,
            "Registration successful. Please login."
        )

        return redirect("login")

    return render(
        request,
        "register.html"
    )


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

        try:
        
         send_mail(
            subject="Resume Analyzer Email Verification",
            message=f"Your OTP is: {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
         )

        except Exception as e:

            print("EMAIL ERROR:", str(e))

            messages.error(
                request,
                "Unable to send password reset OTP."
            )

            return redirect("forgot_password")

        messages.success(
            request,
            "OTP sent successfully."
        )

        return redirect("reset_password")

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