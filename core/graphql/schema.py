import graphene

from core.graphql.mutations import Mutation
from core.graphql.query import Query


class Queries(Query, graphene.ObjectType):
    pass


class Mutations(Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
