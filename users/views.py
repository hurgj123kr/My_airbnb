import os
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms,models


class LoginView(FormView):

    # python만 function식 구현

    # def get(self, request):
    #     form = forms.LoginForm(initial={"email":"hurgj123kr@daum.net"})
    #     return render(request, "users/login.html", {"form": form,})
    

    # def post(self,request):
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get("email")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(request, username=email, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect(reverse("core:home"))
            
    #     return render(request, "users/login.html", {"form": form}) 

    # classform django식 구현
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
        

    
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignupView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name":"test", "last_name":"god", "email":"dddd@naver.com"}

    def form_valid(self,form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)

def verification_email(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # access message
    except models.User.DoesNotExist:
        # error mesasge
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")


def github_callback(request):
    pass






