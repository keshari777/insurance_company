import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from core import models


class UserType(DjangoObjectType):
    class Meta:
        model = models.User
        fields = "__all__"


class PolicyDetailType(DjangoObjectType):
    class Meta:
        model = models.PolicyDetail
        fields = "__all__"


class PolicyPerMonthType(ObjectType):
    month = graphene.String()
    count = graphene.Int()
