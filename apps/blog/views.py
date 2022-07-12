import django_filters
import csv
from rest_framework import viewsets, filters
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

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

@api_view(['GET'])
def export_entries(request):
    export_file = '/tmp/django_entries_%s.log' % datetime.now().strftime('%Y%m%d-%H%M%S')

    with open(export_file, 'w') as f:
        writer = csv.writer(f)
        entries = Entry.objects.all()

        for e in entries:
            writer.writerow([e.id, e.title, e.body, e.created_at, e.updated_at, e.status])

    return Response('export entries at %s' % export_file)
