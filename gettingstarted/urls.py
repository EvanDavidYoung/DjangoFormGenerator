from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from generate_form import urls
admin.autodiscover()
import generate_form
import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    url("generate_form/", include(generate_form.urls))
]
