from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
# login
class LoginModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


###student form
class Standard(models.Model):
    stud_std = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.stud_std}"


class StudentAcc(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, default=True)
    rollnum = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phonenum = PhoneNumberField(null=True)
    attendance = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.rollnum},{self.name},{self.email},{self.attendance}"


class TeacherAcc(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phonenum = PhoneNumberField(null=True)

    def __str__(self):
        return f"{self.name},{self.stu_name},{self.email}"
