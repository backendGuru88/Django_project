from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),  # Ensure a forward slash after "login"
    # path('send_signup_email/', views.send_signup_email, name='send_signup_email'),  # Ensure a forward slash after "send_mail_test"
]


