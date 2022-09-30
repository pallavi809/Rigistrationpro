from django.urls import path
from .views import LoginPageView, LogoutView, SignUpView, HomeView
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    StudentfView,
    Show_Student,
    Update_student,
    Del_student,
    TeacherfView,
    Show_Teacher,
    Update_teacher,
    Del_teacher,
    StandardView,
    Show_standard,
    Update_standard,
    Del_standard,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home_url"),
    path("l1/", LoginPageView.as_view(), name="login_url"),
    path("logout/", LogoutView.as_view(), name="logout_url"),
    path("v1/", StudentfView.as_view(), name="stuf_url"),
    path("show/", Show_Student.as_view(), name="show"),
    path("update/<int:pk>/", Update_student.as_view(), name="update"),
    path("delete/<int:pk>/", Del_student.as_view(), name="delete"),
    path("teachacc/", TeacherfView.as_view(), name="teacherf_url"),
    path("showt/", Show_Teacher.as_view(), name="showt"),
    path("updateteacher<int:pk>/", Update_teacher.as_view(), name="updateteacher"),
    path("deleteteacher/<int:pk>/", Del_teacher.as_view(), name="deleteteacher"),
    path("stdacc/", StandardView.as_view(), name="std_url"),
    path("showstd/", Show_standard.as_view(), name="showstandard"),
    path("updatestd/<int:pk>/", Update_standard.as_view(), name="stdupdate"),
    path("stddelete/<int:pk>/", Del_standard.as_view(), name="stddelete"),
] 