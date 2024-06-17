from courses.models import Course
from courses.serializers import CourseSerializer, CourseStudentSerializer
from courses.permissions import IsAdminOrReadOlnly, IsSuperuser
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class CourseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOlnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(students=self.request.user)


class RetrieveUpdateDeleteCourse(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOlnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"


class RetrieveUpdateStudentCourse(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"
