from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.managers import UserManager


def validate_date(date):
    if date < datetime.now().date():
        raise ValidationError("Date cannot be in the past")


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class MaritalStatus(models.IntegerChoices):
        MARRIED = '1'
        UNMARRIED = '0'

    class Region(models.TextChoices):
        NORTH = 'N', _('North')
        SOUTH = 'S', _('South')
        EAST = 'E', _('East')
        WEST = 'W', _('West')

    class SalaryRange(models.TextChoices):
        LOW = '0-$25K'
        MEDIUM = '$25K-$70K'
        HIGH = '>$70K'

    username = None
    customer_id = models.IntegerField(unique=True, null=True, validators=[
        MinValueValidator(1)
    ])
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, null=True)
    mobile_number = models.IntegerField(null=True, blank=True, validators=[
        MaxValueValidator(9999999999),
        MinValueValidator(1)
    ])
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, validators=[
        MaxValueValidator(200),
        MinValueValidator(1)
    ])
    marital_status = models.IntegerField(choices=MaritalStatus.choices, null=True)
    region = models.CharField(max_length=1, choices=Region.choices, null=True)
    salary_range = models.CharField(max_length=10, choices=SalaryRange.choices, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if not self.customer_id:
            return self.email
        return str(self.customer_id)


class BaseModel(models.Model):
    """
    contains basic fields to be inherited by other models
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class PolicyDetail(BaseModel):
    BOOL_CHOICES = ((True, '1'), (False, '0'))

    class VehicleSegment(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'

    class FuelType(models.TextChoices):
        CNG = 'CNG'
        Petrol = 'Petrol'
        Diesel = 'Diesel'

    policy_id = models.IntegerField(validators=[
        MinValueValidator(1)
    ])
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, validators=[
        MinValueValidator(1)
    ])
    date_of_purchase = models.DateField(validators=[validate_date])
    premium = models.IntegerField(validators=[
        MinValueValidator(1)
    ])
    vehicle_segment = models.CharField(max_length=1, choices=VehicleSegment.choices)
    fuel_type = models.CharField(max_length=6, choices=FuelType.choices)
    bodily_injury_liability = models.BooleanField(choices=BOOL_CHOICES)
    personal_injury_protection = models.BooleanField(choices=BOOL_CHOICES)
    property_damage_liability = models.BooleanField(choices=BOOL_CHOICES)
    collision = models.BooleanField(choices=BOOL_CHOICES)
    comprehensive = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return str(self.policy_id)
