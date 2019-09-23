from django import forms
from crud.models import Employee,Education
from django.core.validators import ValidationError

def checkName(value):
    if value.isdigit():
        raise ValidationError("Name cannot be digits")

class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(max_length =20,validators=[checkName])
    class Meta:
        model = Employee
        fields = '__all__'

        #  or
        # fields = ('emp_name','emp_email','address','phone')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields ='__all__'
