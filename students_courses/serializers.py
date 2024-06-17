from students_courses.models import StudentCourse
from rest_framework import serializers


class StundentCourseSerializer(serializers.ModelSerializer):
    student_id = serializers.UUIDField(source="student.id", read_only=True)
    student_username = serializers.CharField(source="student.username", read_only=True)
    student_email = serializers.EmailField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "student_id",
            "student_username",
            "student_email",
            "status"
        ]
