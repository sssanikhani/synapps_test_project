# Generated by Django 3.1.3 on 2020-11-13 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reports', '0003_auto_20201113_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='submitter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', related_query_name='reports', to=settings.AUTH_USER_MODEL),
        ),
    ]
