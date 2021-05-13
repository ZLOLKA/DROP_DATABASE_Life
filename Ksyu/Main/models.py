from django.db import models


# Create your models here.
class Course(models.Model):
    """
CREATE TABLE Course(
    id              int               PRIMARY KEY,
    start_course    date    NOT NULL,
    end_course      date    NOT NULL,
    count_lesson    int     NOT NULL,
    cost            float   NOT NULL
);
    """
    start_course = models.DateField()
    end_course = models.DateField()
    count_lesson = models.IntegerField()
    cost = models.FloatField()


class Teacher(models.Model):
    """
CREATE TABLE Teacher(
    id          int                   PRIMARY KEY,
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    patronymic  varchar(30),
    birth_year  int         NOT NULL,
    birth_month int         NOT NULL,
    birth_day   int         NOT NULL,
    education   varchar(50),
    mob_number  int         NOT NULL,
    email       varchar(30),
    passport    varchar(20) NOT NULL,
    start_work  date        NOT NULL,
    end_work    date
);
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, null=True)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    education = models.CharField(max_length=50, null=True)
    mob_number = models.IntegerField()
    email = models.CharField(max_length=30, null=True)
    passport = models.CharField(max_length=20, null=True)
    start_work = models.DateField()
    end_work = models.DateField(null=True)
    courses = models.ManyToManyField(Course)


class Class(models.Model):
    """
CREATE TABLE Class(
    id          int PRIMARY KEY,
    id_Course   int REFERENCES Course(id)
);
    """
    id_Course = models.ForeignKey("Course", on_delete=models.CASCADE)


class Student(models.Model):
    """
CREATE TABLE Student(
    id          int PRIMARY KEY,
    id_Class    int REFERENCES Class(id),
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    patronymic  varchar(30),
    birth_year  int         NOT NULL,
    birth_month int         NOT NULL,
    birth_day   int         NOT NULL,
    passport    varchar(20) NOT NULL,
    mob_number  int         NOT NULL
);
    """
    id_Class = models.ForeignKey("Class", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, null=True)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    passport = models.CharField(max_length=20)
    mob_number = models.IntegerField()


class Level(models.Model):
    """
CREATE TABLE Level(
    id          int PRIMARY KEY,
    id_Course   int REFERENCES Course(id)
);
    """
    id_Course = models.ForeignKey("Course", on_delete=models.CASCADE)
