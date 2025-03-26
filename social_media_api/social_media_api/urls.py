from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

# إعداد توثيق API باستخدام drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="API documentation using Swagger UI",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# المسارات
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # مسارات الحسابات
    path('api/', include('posts.urls')),  # مسارات المنشورات
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),  # تسجيل الدخول
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # توثيق Swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # توثيق Redoc
]
