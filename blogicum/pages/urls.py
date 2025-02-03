"""Pages urls."""

from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contacts/', views.ContactsPageView.as_view(), name='rules'),
]
