import graphene
from graphene.types.generic import GenericScalar

from core.graphql import inputs
from core.models import PolicyDetail


class PolicyPremiumMutation(graphene.Mutation):
    """
           Updates Premium of a Policy.
           -----------------------------------------
           Args:
           _____
           policyData (inputs.UpdatePolicyInput): Input object for type UpdatePolicyInput

           Returns:
           ________
           ok: True,if the mutation succeeds else it returns ok:False, with error message
           """
    ok = graphene.Boolean()
    error = GenericScalar()

    class Arguments:
        policy_data = inputs.UpdatePolicyInput()

    @classmethod
    def mutate(cls, root, info, policy_data):
        if policy_data.date_of_purchase:
            return {"ok": False, "error": "Date of purchase can not be updated"}
        elif policy_data.premium > 1000000 or policy_data.premium < 1:
            return {"ok": False, "error": "Premium should be in the range 1 to 1000000"}
        else:
            try:
                policy = PolicyDetail.objects.get(policy_id=policy_data.policy_id)
                policy.premium = policy_data.premium
                policy.save()
            except Exception as e:
                return {"ok": False, "error": e}

        return {"ok": True}


class Mutation(graphene.ObjectType):
    policy_premium_update = PolicyPremiumMutation.Field()
