"""Blogicum urls."""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls import include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blogicum'

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/',
         CreateView.as_view(
             template_name='registration/registration_form.html',
             form_class=UserCreationForm,
             success_url=reverse_lazy('blog:index')
         ),
         name='registration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.internal_server_error'
