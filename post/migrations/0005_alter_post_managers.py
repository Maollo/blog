# Generated by Django 3.2.9 on 2021-11-11 19:35

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_estado_atual'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
