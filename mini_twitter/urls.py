import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views import View
from django.http import HttpResponse
from django.template.exceptions import TemplateDoesNotExist
from django.shortcuts import render
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet
from mini_twitter.docs.schema import schema_view
from mini_twitter.settings import BASE_DIR

# Roteador da API
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# View que renderiza o React index.html
class FrontendAppView(View):
    def get(self, request):
        try:
            return render(request, 'index.html')
        except TemplateDoesNotExist:
            return HttpResponse(
                "index.html not found. Run `npm run build` in your React app.",
                status=501,
            )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('apps.accounts.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # Servindo o manifest.json diretamente da pasta build
    re_path(r'^(?P<path>logo\d+\.png)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'frontend', 'build')
    }),
    # Qualquer outra rota vai pro index.html do React
    re_path(r'^.*$', FrontendAppView.as_view(), name='home'),
]
