# Generated by Django 5.0.1 on 2024-01-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0014_alter_task_cgartistid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
