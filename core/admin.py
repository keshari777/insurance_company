from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from django.contrib import admin

from core.models import User, PolicyDetail


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no username field."""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "name",
                    "customer_id",
                    "gender",
                    "mobile_number",
                    "address",
                    "age",
                    "marital_status",
                    "region",
                    "salary_range"
                )
            },
        ),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser",)},
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "customer_id",
                    "gender",
                    "mobile_number",
                    "address",
                    "age",
                    "marital_status",
                    "region",
                    "salary_range"
                ),
            },
        ),
    )

    list_display = (
        "email",
        "name",
        "is_staff",

    )
    search_fields = ("email", "name")
    ordering = ("email",)
    list_filter = (
        "is_active", "is_staff", "is_superuser"
    )


@admin.register(PolicyDetail)
class PolicyDetailsAdmin(admin.ModelAdmin):
    search_fields = ("policy_id", "customer_id__customer_id")
    list_display = (
        "policy_id",
        "customer_id",
        "date_of_purchase",

    )
    list_filter = (
        "date_of_purchase", "vehicle_segment", "fuel_type"
    )
