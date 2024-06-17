import uuid
from django.db import models


class COURSE_STATUS(models.TextChoices):
    NS = "not started"
    IP = "in progress"
    FI = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    status = models.CharField(
        max_length=11, choices=COURSE_STATUS.choices, default=COURSE_STATUS.NS
    )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="courses", null=True
    )

    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
