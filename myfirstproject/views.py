from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from music.form import UserForm

from music import form


class LoginView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        print("hola")
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('music:index')
        return render(request, self.template_name, {'form': form})