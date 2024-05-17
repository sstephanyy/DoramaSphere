from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm  # Correct import statement
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()  # Correct class name
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
