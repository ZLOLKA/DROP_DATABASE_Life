from django import forms
from .models import Course, Teacher, Class, Student, Level


class CourseForm(forms.ModelForm):
    """
INSERT INTO Course(
    start_course,
    end_course,
    count_lesson,
    cost
) VALUES (
    get_from_form_start_course,
    get_from_form_end_course,
    get_from_form_count_lesson,
    get_from_form_cost
);
    """
    class Meta:
        model = Course
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    """
INSERT INTO Teacher(
    first_name,
    last_name,
    patronymic,
    birth_year,
    birth_month,
    birth_day,
    education,
    mob_number,
    email,
    passport,
    start_work,
    end_work
) VALUES (
    get_from_form_first_name,
    get_from_form_last_name,
    get_from_form_patronymic,
    get_from_form_birth_year,
    get_from_form_birth_month,
    get_from_form_birth_day,
    get_from_form_education,
    get_from_form_mob_number,
    get_from_form_email,
    get_from_form_passport,
    get_from_form_start_work,
    get_from_form_end_work
);
    """
    class Meta:
        model = Teacher
        fields = "__all__"


class ClassForm(forms.ModelForm):
    """
INSERT INTO Class(
    id_Course
) VALUES (
    get_from_form_id_Course
);
    """
    class Meta:
        model = Class
        fields = "__all__"


class StudentForm(forms.ModelForm):
    """
INSERT INTO Student(
    id_Class,
    first_name,
    last_name,
    patronymic,
    birth_year,
    birth_month,
    birth_day,
    passport,
    mob_number
) VALUES (
    get_from_form_id_Class,
    get_from_form_first_name,
    get_from_form_last_name,
    get_from_form_patronymic,
    get_from_form_birth_year,
    get_from_form_birth_month,
    get_from_form_birth_day,
    get_from_form_passport,
    get_from_form_mob_number
);
    """
    class Meta:
        model = Student
        fields = "__all__"


class LevelForm(forms.ModelForm):
    """
INSERT INTO Level(
    id_Course
) VALUES (
    get_from_form_id_Course
);
    """
    class Meta:
        model = Level
        fields = "__all__"
