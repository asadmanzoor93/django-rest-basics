from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
