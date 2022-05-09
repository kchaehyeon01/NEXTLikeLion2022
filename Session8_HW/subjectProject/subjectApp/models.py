from django.db import models

import subjectApp

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    major = models.ForeignKey(
        "Major", on_delete=models.CASCADE, related_name="subject")
    subject_name = models.CharField(max_length=20)
    prof_name = models.CharField(max_length=20)
    memo = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name