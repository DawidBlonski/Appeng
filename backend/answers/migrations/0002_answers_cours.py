# Generated by Django 3.0.2 on 2020-02-04 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('answers', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Courses'),
        ),
    ]