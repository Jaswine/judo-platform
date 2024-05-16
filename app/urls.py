from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', include('admin.urls')),
    # path('api/admin/', include('admin.api.urls')),
    # path('', include('client.urls')),
    # path('auth/', include('user.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('auth/', include('user.urls')),
)