from django.shortcuts import render
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
