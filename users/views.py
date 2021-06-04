from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} has been created .You can now Login.')
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
    


def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'{username} ,your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request,'users/profile.html',{'u_form':u_form})