# Generated by Django 3.0.2 on 2020-03-01 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20200301_1914'),
        ('answers', '0009_auto_20200301_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answers',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Words'),
        ),
    ]
