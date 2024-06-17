from django.urls import path
from contents.views import ContentView, RetrieveUpdateDeleteContentView

urlpatterns = [
    path("contents/", ContentView.as_view()),
    path("contents/<content_id>/", RetrieveUpdateDeleteContentView.as_view()),
]
