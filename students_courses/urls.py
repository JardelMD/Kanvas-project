from django.urls import path
from courses.views import RetrieveUpdateStudentCourse

urlpatterns = [
    path("students/", RetrieveUpdateStudentCourse.as_view()),
]
