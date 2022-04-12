from django import forms
from .models import Resume, Contact

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

JOB_CITY_CHOICES = [
    ('Ahmedabad', 'Ahmedabad'),
    ('Rajkot', 'Rajkot'),
    ('Pune', 'Pune'),
    ('Banglore', 'banglore'),
    ('Mumbai', 'Mumbai')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICES,
                                         widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'email',
                  'profile_image', 'my_file']
        labels = {'name': 'FullName', 'dob': 'Date Of Birth', 'pin': 'Pin Code', 'mobile': 'Mobile Number',
                  'email': 'Email Id',
                  'profile_image': 'Profile Image', 'my_file': 'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})

        }


class ContactUsModalForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'dob', 'city', 'mobile', 'email']
        labels = {'name': 'Enter Your Name', 'dob':'Date Of Birth',
                  'city':'Enter Your City', 'Email':'Enter Your Email Address'}

        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
                  'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
                  'city':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'})
                  }

