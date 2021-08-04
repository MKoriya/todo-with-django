from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from login.forms import CreateUserFrom, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def loginView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        context = {'form': UserLoginForm}
        return render(request, 'login.html', context=context)


    if request.method == 'POST':
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user=user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Invalid Credentials!!')
                return render(request, 'login.html')

        except Exception as e :
            context = {'error': e}
            return render(request, 'login.html', context)
        


def signUpView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        context = {'form': CreateUserFrom}
        return render(request, 'signup.html', context=context)

    if request.method == 'POST':
        data = request.POST

        userForm = CreateUserFrom(data)
        if userForm.is_valid():
            userForm.save()
            return redirect('login')
        else:
            context = {'error': "Error!! Password Must contain atleast 8 character and can't be entirely numeric"}
            return render(request, 'signup.html', context=context)

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('home')

def homeView(request):
    return render(request, 'home.html')



# Test@123