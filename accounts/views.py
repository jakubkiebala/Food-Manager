from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from kitchen.models import ShoppingList


# Create your views here.


class RegisterUserView(View):
    def get(self, request):
        return render(request, 'accounts/register_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != '' and password1 == password2:
            u = User(username=username)
            u.set_password(password1)
            u.save()
            ShoppingList.objects.create(user=u)
            redirect_url = request.GET.get('next', 'base')
            login(request, u)
            return redirect(redirect_url)
        else:
            return render(request, 'accounts/register_user.html', {'error': 'Hasła się nie zgadzają'})


class LoginUserView(View):
    def get(self, request):
        return render(request, 'accounts/login_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            redirect_url = request.GET.get('next', 'base')
            login(request, user)
            return redirect(redirect_url)
        else:
            return render(request, 'accounts/login_user.html', {'error': 'Nieprawidłowe Hasło lub Login'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('base')
