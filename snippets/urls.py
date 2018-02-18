from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]