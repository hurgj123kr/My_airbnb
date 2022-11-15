from django.views import View
from django.shortcuts import render
from . import forms

class LoginView(View):
    
    def get(self, request):
        form = forms.LoginForm(initial={"email":"hurgj123kr@daum.net"})
        return render(request, "users/login.html", {"form": form,})
    

    def post(self,request):
        form = forms.LoginForm()
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form}) 