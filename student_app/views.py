from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Student
from .forms import StudentForm


# Create your views here.

def add_students(request):
    StudentFormSet = formset_factory(StudentForm, extra=1)
    students = Student.objects.all()

    if request.method == 'POST':
        formset = StudentFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('add_students')
    else:
        formset = StudentFormSet()

    return render(request, 'add_students.html', {'formset': formset, 'students': students})
