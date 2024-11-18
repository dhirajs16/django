import graphene
from graphene_django import DjangoObjectType
from .models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'city')

class Query(graphene.ObjectType):
    clients = graphene.List(ClientType)

    def resolve_clients(self, info, **kwargs):
        return Client.objects.filter(city="Ramgarh")

schema = graphene.Schema(query=Query)