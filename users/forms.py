from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("User Password Wrong"))
        except models.User.DoesNotExist:
            self.add_error("email",forms.ValidationError("User does not exist"))

# UsercreationForm way 
class SignUpForm(UserCreationForm):

    username = forms.EmailField(label="Email")

#django Model.Form way
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ("first_name", "last_name", "email")
#     password = forms.CharField(widget=forms.PasswordInput)
#     check_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

#     # python signup email create 구현 방식
#     # def clean_email(self):
#     #     email = self.cleaned_data.get("email")
#     #     try:
#     #         models.User.objects.get(email=email)
#     #         raise forms.ValidationError("User already exits with that email")
#     #     except models.User.DoesNotExist:
#     #         return email
    
    def clean_password1(self):

        password = self.cleaned_data.get("password")
        check_password = self.cleaned_data.get("check_password")
        if password != check_password:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()




