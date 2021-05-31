# Generated by Django 3.2.3 on 2021-05-28 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=100, size=[400, 400], upload_to='images')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('payment_details', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_details', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=10)),
                ('user_type', models.CharField(max_length=10)),
                ('services', models.CharField(blank=True, max_length=100, null=True)),
                ('artisan_approved', models.BooleanField(default=False)),
                ('blocked', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('artisan_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_basket', to='accounts.userprofile')),
                ('customer_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_basket', to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('comment', models.TextField()),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('artisan_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_review', to='accounts.userprofile')),
                ('customer_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_review', to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField()),
                ('artisan_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_order', to='accounts.userprofile')),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_order', to='accounts.userprofile')),
            ],
        ),
    ]
