# Generated by Django 3.2.3 on 2021-05-24 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210524_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='artisan',
            new_name='artisan_order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer_order',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='artisan',
            new_name='artisan_review',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='customer',
            new_name='customer_review',
        ),
    ]