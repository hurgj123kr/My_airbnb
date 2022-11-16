from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


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






