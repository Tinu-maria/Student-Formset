from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm


# Create your views here.

def add_students(request):
    StudentFormSet = modelformset_factory(Student, StudentForm, extra=1, can_delete=True)
    # import pdb; pdb.set_trace()
    students = Student.objects.all()

    if request.method == 'POST':
        formset = StudentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    form.instance.delete()
                else:
                    form.save()
            return redirect('add_students')
    else:
        formset = StudentFormSet()

    return render(request, 'add_students.html', {'formset': formset, 'students': students})


def add_teachers(request, student_id):
    student = Student.objects.get(id=student_id)
    TeacherFormSet = inlineformset_factory(Student, Teacher, form=TeacherForm, extra=0, can_delete=True)
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        formset = TeacherFormSet(request.POST, instance=student)

        if formset.is_valid():
            formset.save()

    else:
        formset = TeacherFormSet(instance=student)

    return render(request, 'add_teachers.html', {'formset': formset, 'teachers': teachers})

