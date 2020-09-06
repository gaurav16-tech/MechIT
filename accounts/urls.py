from django.conf.urls import url
from accounts import views
from .views import signup_view, activation_sent_view, activate
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
   url(r'^about/$',views.AboutView.as_view(),name='about'),
   url(r'^contact/$',views.DetailView.as_view(),name='contact'),
   url(r'login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
