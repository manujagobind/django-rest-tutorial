from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)