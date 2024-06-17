from contents.serializers import ContentSerializer
from contents.models import Content
from contents.permissions import IsSuperuser, IsUserOnCourseByContent
from courses.models import Course
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication


class ContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get("course_id")
        serializer.save(course_id=course_id)


class RetrieveUpdateDeleteContentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOnCourseByContent]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        content = Content.objects.filter(id=self.kwargs.get("content_id")).first()
        if not content:
            raise NotFound("content not found.")
        course = Course.objects.filter(id=self.kwargs.get("course_id")).first()
        if not course:
            raise NotFound("course not found.")
        self.check_object_permissions(self.request, content)
        return content
