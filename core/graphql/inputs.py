import graphene


class UpdatePolicyInput(graphene.InputObjectType):
    policy_id = graphene.Int(required=True)
    premium = graphene.Int(required=True)
    date_of_purchase = graphene.Date()


class PolicyPerMonthFilterInput(graphene.InputObjectType):
    region = graphene.List(graphene.String)
