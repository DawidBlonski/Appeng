# Generated by Django 2.0.9 on 2019-05-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_answer',
            name='words',
            field=models.ManyToManyField(blank=True, related_name='user_words', to='appeng.Words'),
        ),
    ]
