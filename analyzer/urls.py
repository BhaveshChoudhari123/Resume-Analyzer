from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.upload_resume,
        name='upload_resume'
    ),

    path(
        'history/',
        views.resume_history,
        name='history'
    ),

    path(
        'download-report/',
        views.download_report,
        name='download_report'
    ),

    path(
       "ask-question/",
       views.ask_question,
       name="ask_question"
    ),

    path(
       "job-match/",
       views.job_match,
       name="job_match"
    ),
    

    path(
       "resume-improvement/",
       views.improve_resume_view,
       name="resume_improvement"
    ),
]