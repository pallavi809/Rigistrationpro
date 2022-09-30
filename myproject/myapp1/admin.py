from django.contrib import admin
from .models import StudentAcc, TeacherAcc, Standard, LoginModel

# Register your models here.


class StdAdmin(admin.ModelAdmin):
    list_display = ["stud_std"]


admin.site.register(Standard, StdAdmin)


class StuAdmin(admin.ModelAdmin):
    list_display = ["rollnum", "name", "email", "attendance"]


admin.site.register(StudentAcc, StuAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phonenum"]


admin.site.register(TeacherAcc, TeacherAdmin)
