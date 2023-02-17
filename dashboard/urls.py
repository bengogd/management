from django.urls import path
from dashboard import views

urlpatterns = [
    path('registerStudent/',views.registerStudent,name='registerStudent'),
    path('registerTeacher/',views.registerTeacher,name='registerTeacher'),
    path('',views.userLogin,name='userLogin'),
]
