# Generated by Django 3.0.2 on 2020-01-09 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courses',
            name='word',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Words'),
        ),
    ]
