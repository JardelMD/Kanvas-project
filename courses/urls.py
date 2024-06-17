from django.urls import path
from courses.views import CourseView, RetrieveUpdateDeleteCourse

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<course_id>/", RetrieveUpdateDeleteCourse.as_view()),
]
