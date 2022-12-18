from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    internalId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    careerName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Grade(models.Model):
    gradeId = models.CharField(max_length=100)
    projectId = models.CharField(max_length=100)
    score = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Professor(models.Model):
    internalId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    facultyId = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
