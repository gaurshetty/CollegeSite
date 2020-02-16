from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='College Site Application RESTAPI EndPoints')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#    #
#     path('api/v1/', include('department.apiroutes')),
#     url(r'^rapi-auth/', include('rest_framework.urls')),
#     url(r'^$', schema_view),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('department.apiroutes')),
    path('', include('restapi.api_routes')),
    url(r'^api/', include('rest_framework.urls')),
    url(r'^$', schema_view)
]
