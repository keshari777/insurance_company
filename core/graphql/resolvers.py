from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Count
from django.db.models.functions import ExtractMonth


class ModelListResolver:
    """Resolver that loads all the model instances"""

    def __init__(self, model):
        self.model = model

    def __call__(self, info, source, **kwargs):
        query_set = self.model.objects.all()

        return query_set


class PolicyDetailByIdResolver:
    """Resolver that loads the specific Policy model instance"""

    def __init__(self, model):
        self.model = model

    def __call__(self, source, info, id):
        try:
            policy_detail = self.model.objects.filter(Q(policy_id=id) | Q(customer_id__customer_id=id))
            result = policy_detail
        except ObjectDoesNotExist:
            result = None

        return result


class PolicyPerMonthResolver:
    """Resolver to calculate policies bought per month with region filter"""

    def __init__(self, model):
        self.model = model

    def __call__(self, info, source, filtering=None):
        if filtering is None:
            filtering = {}
        try:
            get_region = Q(customer_id__region__in=filtering.get("region")) if filtering.get("region") else Q()
            policy_monthly_data = self.model.objects.filter(get_region)\
                .annotate(
                month=ExtractMonth('date_of_purchase')).values(
                'month').annotate(
                count=Count('policy_id')).order_by('-month')
            result = policy_monthly_data
        except ObjectDoesNotExist:
            result = None
        return result
