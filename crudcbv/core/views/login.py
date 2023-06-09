from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from core.forms import LoginForm


class LoginView(View):
    def get(self, request):
        data = { 'form': LoginForm() }
        return render(request, 'core/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password \
                and authenticate(username=username, password=password):
                login(request.user)
                return HttpResponseRedirect(reverse('home'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, 'core/login.html', data)