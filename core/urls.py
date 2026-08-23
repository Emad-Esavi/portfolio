from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("resume/download/", views.download_resume, name="download_resume"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("certificates/", views.certificates, name="certificates"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("contact/submit/", views.contact_submit, name="contact_submit"),
]
