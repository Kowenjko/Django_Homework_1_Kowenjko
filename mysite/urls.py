
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    re_path(r'', include('blog.urls'))
]
