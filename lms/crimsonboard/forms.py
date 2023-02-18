from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['first_name','email','username','password1','password2']
        

#     def __init__(self,*args, **kwargs):
#         super(UserCreationForm,self).__init__(*args, **kwargs)
#         for name,field in self.fields.items():
#             field.widget.attrs.update({'class':'input'})

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )