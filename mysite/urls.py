from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('marcador.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),]