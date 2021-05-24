# Generated by Django 3.2.3 on 2021-05-23 14:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=100, size=[400, 400], upload_to='images'),
        ),
    ]