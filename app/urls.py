from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('api/admin/', include('admin.api.urls')),
    path('', include('client.urls')),
    path('auth/', include('user.urls')),
]
