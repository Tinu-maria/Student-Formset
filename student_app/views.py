from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from student_app.models import Student
from .forms import StudentForm


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