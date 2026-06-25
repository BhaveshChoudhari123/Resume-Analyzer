from django.shortcuts import render
from django.http import HttpResponse
from .rag_engine import (
    process_resume,
    ask_resume_question
)

from django.contrib.auth.decorators import login_required

from .pipelines.job_match_pipeline import (
    calculate_match_score
)

from .pipelines.resume_improvement_pipeline import (
    improve_resume
)

from .utils import (
    extract_text_from_pdf,
    calculate_resume_score,
    calculate_ats_score,
    get_resume_level
)

from .ai_engine import analyze_resume_with_ai
from .models import Resume
from .pdf_generator import generate_pdf_report

latest_report = {}

@login_required
def upload_resume(request):

    global latest_report

    if request.method == "POST":

        uploaded_file = request.FILES.get("resume")

        if uploaded_file:

            Resume.objects.create(
                user=request.user,
                resume_file=uploaded_file
            )

            text = extract_text_from_pdf(uploaded_file)

            # DEBUG OUTPUT
            print("\n\n========== RESUME TEXT ==========\n")
            print(text)
            print("\n=================================\n")

            chunks, index = process_resume(text)

            print("\n\n========== CHUNKS ==========\n")
            print(chunks)
            print("\n============================\n")

            

            request.session["resume_text"] = text

            ai_result = analyze_resume_with_ai(text)

            skills = ai_result.get("skills", [])
            missing_skills = ai_result.get("missing_skills", [])
            recommended_jobs = ai_result.get("recommended_jobs", [])
            strengths = ai_result.get("strengths", [])
            weaknesses = ai_result.get("weaknesses", [])
            suggestions = ai_result.get("suggestions", [])
            resume_summary = ai_result.get("resume_summary", "")
            interview_questions = ai_result.get("interview_questions", [])
            job_match = ai_result.get("job_match",[])

            score = calculate_resume_score(
                text,
                skills
            )

            ats_score = calculate_ats_score(text)

            resume_level = get_resume_level(score)

            skills_count = len(skills)
            missing_count = len(missing_skills)

            total_skills = skills_count + missing_count

            if total_skills > 0:
                skill_percentage = int(
                    (skills_count / total_skills) * 100
                )
            else:
                skill_percentage = 0

            latest_report = {
                "score": score,
                "ats_score": ats_score,
                "resume_level": resume_level,
                "skills": skills,
                "missing_skills": missing_skills,
                "recommended_jobs": recommended_jobs,
                "resume_summary": resume_summary,
                "strengths": strengths,
                "weaknesses": weaknesses,
                "suggestions": suggestions,
                "interview_questions": interview_questions,
                "job_match": job_match,
            }

            return render(
                request,
                "upload.html",
                {
                    "success": True,
                    "skills": skills,
                    "missing_skills": missing_skills,
                    "recommended_jobs": recommended_jobs,
                    "score": score,
                    "ats_score": ats_score,
                    "job_match": job_match,
                    "resume_level": resume_level,
                    "skill_percentage": skill_percentage,
                    "strengths": strengths,
                    "weaknesses": weaknesses,
                    "suggestions": suggestions,
                    "resume_summary": resume_summary,
                    "interview_questions": interview_questions,
                    "skills_count": skills_count,
                    "missing_count": missing_count
                }
            )

    return render(request, "upload.html")


def resume_history(request):

    resumes = Resume.objects.filter(
    user=request.user
).order_by(
    "-uploaded_at"
)

    return render(
        request,
        "history.html",
        {
            "resumes": resumes
        }
    )


def download_report(request):

    global latest_report

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; '
        'filename="resume_report.pdf"'
    )

    print("PDF REPORT DATA")
    print(latest_report)

    generate_pdf_report(
        response,
        latest_report.get("score",0),
        latest_report.get("ats_score",0),
        latest_report.get("resume_level","N/A"),
        latest_report.get("skills",[]),
        latest_report.get("missing_skills",[]),
        latest_report.get("recommended_jobs",[]),
        latest_report.get("resume_summary", ""),
        latest_report.get("strengths", []),
        latest_report.get("weaknesses", []),
        latest_report.get("suggestions", []),
        latest_report.get("interview_questions", [])
    )

    return response


from django.http import JsonResponse




def ask_question(request):

    if request.method == "POST":

        question = request.POST.get("question")

        text = request.session.get(
            "resume_text",
            ""
        )

        if not text:

            return JsonResponse({
                "answer": "Upload resume first."
            })

        chunks, index = process_resume(text)

        answer = ask_resume_question(
        question,
        chunks,
        index
        )

        return JsonResponse({
            "answer": answer
        })

    return JsonResponse({
        "answer": "Invalid request"
    })


def job_match(request):

    if request.method == "POST":

        resume_text = request.session.get(
            "resume_text",
            ""
        )

        job_description = request.POST.get(
            "job_description",
            ""
        )

        score = calculate_match_score(
            resume_text,
            job_description
        )

        return render(
            request,
            "job_match.html",
            {
                "score": score,
                "job_description": job_description
            }
        )

    return render(
        request,
        "job_match.html"
    )


def improve_resume_view(request):

    result = None

    if request.method == "POST":

        resume_text = request.session.get(
            "resume_text",
            ""
        )

        result = improve_resume(
            resume_text
        )

    return render(
        request,
        "resume_improvement.html",
        {
            "result": result
        }
    )