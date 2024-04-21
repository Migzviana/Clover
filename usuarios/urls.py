from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path ('', RedirectView.as_view(pattern_name='cadastro', permanent=False)),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('sair/', views.sair, name="sair")
]