from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mini Twitter API",
        default_version='v1',
        description="Documentação da API do projeto Mini Twitter. API de seguidores, usuários e autenticação JWT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@minitwitter.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # permission_classes=(IsAuthenticated,),
    permission_classes=(AllowAny,),
)
