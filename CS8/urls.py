
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')),
    re_path(r'^api/v1/example/', include('example.urls')),
    re_path(r'^api/v1/', include('denuncias.urls')),
    re_path(r'^api/v1/', include('petcitas.urls')),

    # path(r'^api-auth/', include('rest_framework.urls'))
    #url(r'^upload/$', views.ImageCreateAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
