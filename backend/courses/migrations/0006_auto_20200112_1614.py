# Generated by Django 3.0.2 on 2020-01-12 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200112_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='word',
        ),
        migrations.AddField(
            model_name='courses',
            name='word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Words'),
        ),
    ]
