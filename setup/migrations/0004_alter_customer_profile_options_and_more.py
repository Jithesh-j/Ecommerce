# Generated by Django 5.0.1 on 2024-02-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_customer_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer_profile',
            options={'verbose_name_plural': 'Customer Profiles'},
        ),
        migrations.AddField(
            model_name='customer_profile',
            name='cart_details',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]