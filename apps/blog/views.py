import django_filters
from rest_framework import viewsets, filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


@api_view(['GET'])
def get_title(request):
    params = request.query_params
    # return Response(params.get('id'))
    if 'id' in params.keys():
        with connection.cursor() as cursor:
            id = params.get('id')
            cursor.execute("SELECT title FROM blog_entry where id = %s", id)
            title = cursor.fetchone()
    else:
        return Response('id is required.')

    return Response({"id": id, "title": title[0]})
