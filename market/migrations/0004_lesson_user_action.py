# Generated by Django 4.2.5 on 2023-10-01 11:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_userlessonrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='user_action',
            field=models.ManyToManyField(related_name='user_action', through='market.UserLessonRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
