from courses.models import Course
from accounts.models import Account
from rest_framework import serializers
from students_courses.serializers import StundentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        read_only_fields = ["students_courses", "contents"]


class CourseStudentSerializer(serializers.ModelSerializer):
    students_courses = StundentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["name"]

    def update(self, instance: Course, validated_data):
        students_found = []
        students_not_found = []
        for students_courses in validated_data["students_courses"]:
            student_email = students_courses["student"]["email"]
            student_found = Account.objects.filter(email=student_email).first()
            if not student_found:
                students_not_found.append(student_email)
            else:
                students_found.append(student_found)
        if len(students_not_found):
            raise serializers.ValidationError(
                {"detail": f"No active accounts was found: {", ".join(students_not_found)}."}
            )
        instance.students.add(*students_found)
        return instance
