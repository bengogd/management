from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_type(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """
    def __str__(self):
        if self.is_student == True:
            return User.get_email(self.user) + " - is_student"
        else:
            return User.get_email(self.user) + " - is_teacher"
    """
    





