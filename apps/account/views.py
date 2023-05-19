from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login
from .forms import SignUpForm
from django.urls import reverse_lazy


# Create your views here.
class SignUpView(FormView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("entry:home")

    def form_valid(self, form: SignUpForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
