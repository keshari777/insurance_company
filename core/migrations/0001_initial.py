# Generated by Django 4.0.4 on 2022-05-15 19:30

import core.managers
import core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('customer_id', models.IntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1)])),
                ('address', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('marital_status', models.IntegerField(choices=[(1, 'Married'), (0, 'Unmarried')], null=True)),
                ('region', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')], max_length=1, null=True)),
                ('salary_range', models.CharField(choices=[('0-$25K', 'Low'), ('$25K-$70K', 'Medium'), ('>$70K', 'High')], max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PolicyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('policy_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('date_of_purchase', models.DateField(validators=[core.models.validate_date])),
                ('premium', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('vehicle_segment', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('fuel_type', models.CharField(choices=[('CNG', 'Cng'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], max_length=6)),
                ('bodily_injury_liability', models.BooleanField(choices=[(True, '1'), (False, '0')])),
                ('personal_injury_protection', models.BooleanField(choices=[(True, '1'), (False, '0')])),
                ('property_damage_liability', models.BooleanField(choices=[(True, '1'), (False, '0')])),
                ('collision', models.BooleanField(choices=[(True, '1'), (False, '0')])),
                ('comprehensive', models.BooleanField(choices=[(True, '1'), (False, '0')])),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
