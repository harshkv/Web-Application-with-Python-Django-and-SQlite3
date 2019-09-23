from django import forms
# from django.core.validators import ValidationError
#
# def validateName(value):
#     if value.isdigit():
#         raise ValidationError("username cannot be digit")
#
#
# def validateEmail(value):
#     if(value.find("@mytectra.com") < 0):
#         raise ValidationError("Invalid email (mytectra.com)")


class FormExample(forms.Form):
    username = forms.CharField(min_length=2, max_length=20,label='Name',required = True, error_messages={'required': "blank input",'min_length': "please provide more characters",'max_length': "please provide less characters"},
                               # validators=[validateName],
                               help_text="please provide the valid username",
                               widget=forms.TextInput(attrs={'placeholder': "emp name",'class':'text','id': 'fsdf'}))
    password1 = forms.CharField(max_length = 20,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length = 20,widget=forms.PasswordInput)

 #DROPDOWN
    cityList = (
        ('', '--Select Option --'),
        ('chennai', 'Chennai'),
        ('bangalore', 'Bangalore'),
        ('hyderabad', 'Hyderabad'),
        ('mysore', 'Mysore')
            )
    city = forms.ChoiceField(choices=cityList)

    #CHECKBOX
    is_active = forms.BooleanField(required = False)
    Active = forms.CharField(widget=forms.CheckboxInput,required=False)

    #RADIO BUTTON
    gn = (
        ('m','Male'),
        ('f','Female')
    )
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)

    email = forms.EmailField(
        # validators=[validateEmail]
        )

    address = forms.CharField(max_length=250, widget=forms.Textarea)

    def clean(self):
        form_data = self.cleaned_data
        if 'username' in form_data:
            if form_data['username'].isdigit():
                self.errors['username'] = ['Employee name cannnot be digits']
        if 'email' in form_data:
            if (form_data['email'].find('@mytectra') <0):
                self.errors['email'] = ['Email must have @mytectra']

        if 'password1' in form_data and 'password2' in form_data:
            if(form_data['password1'] != form_data['password2']):
                self.errors['password2'] = ['password is a mismatch']
        return form_data




