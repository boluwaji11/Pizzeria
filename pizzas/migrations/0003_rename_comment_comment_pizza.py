# Generated by Django 3.2 on 2021-04-23 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='pizza',
        ),
    ]
