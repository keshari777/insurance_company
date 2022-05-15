import graphene

from core import models
from core.graphql import types, resolvers
from core.graphql.inputs import PolicyPerMonthFilterInput


class Query(graphene.ObjectType):
    """Query to fetch all the policy with its detail"""
    all_policy_detail = graphene.List(
        types.PolicyDetailType,
        resolver=resolvers.ModelListResolver(models.PolicyDetail),
    )

    """Query to fetch the policy with Id"""
    get_policy_by_id = graphene.List(
        types.PolicyDetailType,
        id=graphene.Int(required=True),
        resolver=resolvers.PolicyDetailByIdResolver(models.PolicyDetail),
    )

    """Query to count policies in a month with region filter"""
    get_policy_per_month = graphene.List(types.PolicyPerMonthType, filtering=PolicyPerMonthFilterInput(),
                                         resolver=resolvers.PolicyPerMonthResolver(models.PolicyDetail))
