from django.urls import path, re_path

from . import views

# Cela permet aux templates de repérer les bons URLs (particulièrement utile lorsqu'il y aura de nombreuses app)
app_name = 'totp_page'

# URL management
urlpatterns = [
    path('', views.totp_homepage, name='totp_homepage'),
]