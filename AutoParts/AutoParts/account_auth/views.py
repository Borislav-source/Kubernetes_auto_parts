from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from AutoParts.account_auth.forms import SignInForm, SignUpForm


class SignInView(FormView):
    template_name = 'pages/sign-in.html'
    form_class = SignInForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class SignUpView(CreateView):
    template_name = 'pages/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


def sign_out(request):
    logout(request)
    return redirect('index')
