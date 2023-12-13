from django.urls import path
from .views import LoginStudentView, LoginCompanyView, LogoutView

urlpatterns = [
    # login
    path('student/', LoginStudentView.as_view(), name='loginStudent'),
    path('company/', LoginCompanyView.as_view(), name='loginCompany'),

    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),

]

