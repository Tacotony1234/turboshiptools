from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Assuming 'profile' is a valid named URL
        else:
            # Updated path to template
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    # Updated path to template
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # Assuming you have a logout.html under accounts/templates/accounts/
    return render(request, 'accounts/logout.html', {'message': 'Logged out successfully'})

@login_required
def profile_view(request):
    # Assuming you have a profile.html under accounts/templates/accounts/
    return render(request, 'accounts/profile.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # Corrected syntax here
            form.save()
            return redirect('home')  # Assuming 'home' is a named URL you have defined
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

