from django.urls import path
from .views import predict_view, patient_dashboard
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('predict/', predict_view, name='predict'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   # path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("patient_dashboard/", patient_dashboard, name="patient_dashboard"),
]


