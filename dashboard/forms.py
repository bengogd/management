from django import forms
from django.contrib.auth.models import User
from dashboard.models import User_type

class studentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','password']

BRANCH_CHOICES = (
    ('COMPS','COMPS'),
    ('IT','IT'),
    ('EXTC','EXTC')
)
class studentAddForm(forms.ModelForm):
    branch=forms.CharField(widget=forms.Select(choices=BRANCH_CHOICES))
    class Meta():
        model=User_type
        fields=['branch']

class teacherForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','password']

SUBJECT_CHOICES=(
    ('DS','Data Structures'),
    ('DLD','Digital Logic Design'),
    ('DM','Discrete Mathematics'),
    ('LA','Linear Algebra')
)

class teacherAddForm(forms.ModelForm):
    subject=forms.CharField(widget=forms.Select(choices=SUBJECT_CHOICES))
    class Meta():
        model=User_type
        fields=['subject']


        