"""HospitalCasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalBackend import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('userlogin/', views.UserCreateView.usercreateview.as_view()),

    path('user/', views.userView.UsuarioListView.as_view()),  
    path('user/<int:pk>/', views.userView.UsuarioRetrieveUpdateDeleteView.as_view()),  

    path('medico/', views.medicoView.MedicoListCreateView.as_view()),  
    path('medico/<int:pk>/', views.medicoView.MedicoRetrieveUpdateView.as_view()),

    path('enfermero/', views.enfermeroView.EnfermeroListCreateView.as_view()),  
    path('enfermero/<int:pk>/', views.enfermeroView.EnfermeroRetrieveUpdateDeleteView.as_view()),

    path('enfermeroPaciente/', views.enfermeropacienteView.EnfermeroPacienteListCreateView.as_view()),  
    path('enfermeroPaciente/<int:pk>/', views.enfermeropacienteView.EnfermeroPacienteRetrieveUpdateDeleteView.as_view()),

    path('historia/', views.historiaView.HistoriaListCreateView.as_view()),  
    path('historia/<int:pk>/', views.historiaView.HistoriaRetrieveUpdateDeleteView.as_view()),

    path('paciente/', views.pacienteView.PacienteListCreateView.as_view()),  
    path('paciente/<int:pk>/', views.pacienteView.PacienteRetrieveUpdateDeleteView.as_view()),

    path('familiar/', views.familiarView.FamiliarListCreateView.as_view()),  
    path('familiar/<int:pk>/', views.familiarView.FamiliarRetrieveUpdateDeleteView.as_view()),

     
    
    
        


]
