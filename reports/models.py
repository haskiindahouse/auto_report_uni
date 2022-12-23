from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return self.surname


class Group(models.Model):
    number = models.IntegerField(unique=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    # Показать на примере с заполнением
    teachers = models.ManyToManyField(Teacher)
    groups = models.ManyToManyField(Group)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    gradebook = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return self.surname