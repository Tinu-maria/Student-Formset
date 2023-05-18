from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ["name", "is_active"]

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.is_active:
            for field in self.fields.values():
                field.disabled = True
    # In init method, if instance exists and if active field is true,
    # disabled attribute of all fields in the form is set to true
