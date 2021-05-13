from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CourseForm, TeacherForm, ClassForm, StudentForm, LevelForm
from .models import Course, Teacher, Class, Student, Level


# Create your views here.
def home(request):
    all_Courses = Course.objects.all()    # SELECT * FROM Courses;
    all_Teachers = Teacher.objects.all()  # SELECT * FROM Teachers;
    all_Classes = Class.objects.all()     # SELECT * FROM Class;
    all_Students = Student.objects.all()  # SELECT * FROM Students;
    all_Levels = Level.objects.all()      # SELECT * FROM Levels;

    context = {
        "all_courses":  all_Courses,
        "all_teachers": all_Teachers,
        "all_classes":  all_Classes,
        "all_students": all_Students,
        "all_levels":   all_Levels,
    }
    return render(request, "Home.html", context)


def db_form(request, table_name):
    if table_name == "Course":
        Form = CourseForm
    elif table_name == "Teacher":
        Form = TeacherForm
    elif table_name == "Class":
        Form = ClassForm
    elif table_name == "Student":
        Form = StudentForm
    elif table_name == "Level":
        Form = LevelForm
    else:
        raise Exception("Incorrect table name")

    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    context = {
        "form": form,
    }
    return render(request, "DB_Form.html", context)
