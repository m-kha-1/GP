# Generated by Django 5.0.1 on 2024-01-17 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0008_task_completed_task_producerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='producerID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producerTasks', to='BASE.producer'),
        ),
        migrations.AddField(
            model_name='task',
            name='supervisorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisorTasks', to='BASE.supervisor'),
        ),
    ]
