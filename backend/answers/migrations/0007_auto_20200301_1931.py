# Generated by Django 3.0.2 on 2020-03-01 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200301_1914'),
        ('answers', '0006_auto_20200301_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(auto_created=True, default=23, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_user', to='courses.Courses'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answers',
            name='word',
            field=models.ForeignKey(auto_created=True, default=23123, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_word', to='courses.Courses'),
            preserve_default=False,
        ),
    ]
