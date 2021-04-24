from django.urls import path
from .views import MyLoginView, MyPasswordChangeView, MySignUpView
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("password_change/", MyPasswordChangeView.as_view(), name='password_change'),
    path("sign_up/", MySignUpView.as_view(), name='sign_up'),

]

