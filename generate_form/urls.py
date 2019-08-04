from django.urls import path
from rest_framework import routers
from . import views
from generate_form.models import Form_Model
import generate_form.api_views 
import generate_form.serializers
# router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'webhooks', views.HookViewSet, 'webhook')
urlpatterns = [
	path('api/v1/forms/', generate_form.api_views.FormList.as_view()),
	path('api/v1/forms/new', generate_form.api_views.FormCreate.as_view()),
    # url(r'^', include(router.urls)),
]