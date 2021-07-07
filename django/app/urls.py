from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view

from .users.views import index, user_detail, user_list

schema_view = get_schema_view(
    title='My DRF Sample APP',
    description="Show how easy is to create a gateway API with documentation",
    renderer_classes=[JSONOpenAPIRenderer]
)

urlpatterns = [
    path('', index, name='index'),
    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
    path('schema.json', schema_view, name="openapi-schema"),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
         template_name='redoc.html',
         extra_context={'schema_url': 'openapi-schema'}
         ), name='redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
