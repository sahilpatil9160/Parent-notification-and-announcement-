from django.contrib import admin
from django.urls import path
from authapp.views import main, user_login, user_signup, reset, home, user_logout, filter, add_student, mark_student, delete, submit, send_ann, an_filter, send_email, how, at_mail, about, stu_delete, del_filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main"),
    path("user_login/", user_login, name="user_login"),
    path("user_signup/", user_signup, name="user_signup"),
    path("reset/", reset, name="reset"),
    path("home/", home, name="home"),
    path("user_logout/", user_logout, name="user_logout"),
    path("filter/", filter, name="filter"),
    path("add_student/", add_student, name="add_student"),
    path("mark_student/", mark_student, name="mark_student"),
    path("delete/<int:id>", delete, name="delete"),
    path("submit", submit, name="submit"),
    path("send_ann", send_ann, name="send_ann"),
    path("an_filter", an_filter, name="an_filter"),
    path("send_email", send_email, name="send_email"),
    path("how", how, name="how"),
    path("at_mail/", at_mail, name="at_mail"),
    path("about/", about, name="about"), 
    path("stu_delete", stu_delete, name="stu_delete"),	
    path("del_filter", del_filter, name="del_filter"),	   
]
