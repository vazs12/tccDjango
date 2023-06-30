from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django import forms
from . import models

def index(request):
    return render(request, 'home.html')


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['nome_aluno', 'cpf_aluno', 'data_nascimento', 'endereco', 'bairro', 'cidade', 'estado', 'cep', 'turma']
        widgets = {
            'nome': forms.TextInput(),
            'cpf_aluno': forms.TextInput(),
            'data_nascimento': forms.DateInput(),
            'endereco': forms.TextInput(),
            'bairro': forms.TextInput(),
            'cidade': forms.TextInput(),
            'estado': forms.Select(),
            'cep': forms.TextInput(),
            'turma': forms.Select(),
        }


class StudentCreateView(CreateView):
    model = models.Student
    form_class = StudentForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('index')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('accounts:home')  # Redirecionar para a página inicial após o login
#         else:
#             messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
#     return render(request, 'login.html')

# def register_view(request):
#      if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registro realizado com sucesso. Faça o login.')
#             return redirect('accounts:login')
#         else:
#             form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})



# def cadastro_view(request):
#     if request.method == 'POST':
#         form = Aluno(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sucesso')
#     else:
#         form = Aluno()
#     return render(request, 'cadastro.html', {'form': form})
