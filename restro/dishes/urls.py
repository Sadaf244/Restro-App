from graphene_django.views import GraphQLView
from dishes.schema import schema
from django.urls import path

urlpatterns=[
    path("restro",GraphQLView.as_view(graphiql=True,schema=schema)),  
]