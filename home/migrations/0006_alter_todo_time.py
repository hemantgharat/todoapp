# Generated by Django 3.2.16 on 2023-09-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
