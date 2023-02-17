from django.shortcuts import render,redirect
from dashboard.forms import studentForm,studentAddForm,teacherForm,teacherAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import User_type
from django.contrib.auth.models import User


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userLogin'))

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_studentForm=studentForm(request.POST)
        var_studentAddForm=studentAddForm(request.POST)
        if var_studentForm.is_valid() and var_studentAddForm.is_valid():
            studentprimary=var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            studentAdd=var_studentAddForm.save(commit=False)
            studentAdd.student=studentprimary
            studentAdd.save()
            registered=True
    else:
        var_studentForm=studentForm()
        var_studentAddForm=studentAddForm()
    return render(request,'dashboard/registerStudent.html',{'var_studentForm':var_studentForm,'var_studentAddForm':var_studentAddForm,'registered':registered})


def registerTeacher(request):
    registered=False
    if request.method=='POST':
        var_teacherForm=teacherForm(request.POST)
        var_teacherAddForm=teacherAddForm(request.POST)
        if var_teacherForm.is_valid() and var_teacherAddForm.is_valid():
            teacherprimary=var_teacherForm.save()
            teacherprimary.set_password(teacherprimary.password)
            teacherprimary.save()
            teacherAdd=var_teacherAddForm.save(commit=False)
            teacherAdd.teacher=teacherprimary
            teacherAdd.save()
            registered=True
    else:
        var_teacherForm=teacherForm()
        var_teacherAddForm=teacherAddForm()
    return render(request,'dashboard/registerTeacher.html',{'var_teacherForm':var_teacherForm,'var_teacherAddForm':var_teacherAddForm,'registered':registered})

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            type_obj = User_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('studentDash') #Go to student home
            elif user.is_authenticated and type_obj.is_teacher:
                return redirect('teacherDash') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return HttpResponse('<h1>Page was found</h1>')
            # return render(request, 'dashboard/login.html')
    return render(request, 'dashboard/login.html')



def studentDash(request):
    return render(request,'dashboard/studentDash.html')

def teacherDash(request):
    return render(request,'dashboard/teacherDash.html')