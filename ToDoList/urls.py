
from django.contrib import admin
from django.urls import path
from main_app.views import home, register, update_task, delete_task , complete_task , index
from django.contrib.auth.views import LoginView, LogoutView 
urlpatterns = [
    path("", index, name="index"),
    path("Task", home, name="home"),

    path('admin/', admin.site.urls),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", register, name="register"),

    path("update/task/<int:pk>/", update_task, name="update_task"),
    path("complete/task/<int:pk>/", complete_task, name="complete_task"),
    path("delete/task/<int:pk>/", delete_task, name="delete_task"),
]
