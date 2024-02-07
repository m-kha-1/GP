# Generated by Django 5.0.1 on 2024-01-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0010_alter_task_producerid_alter_task_supervisorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('LIGHT', 'lighting'), ('COMP', 'compositing'), ('ANIM', 'animation'), ('MODEL', 'modelling'), ('SURFACE', 'surfacing'), ('FX', 'fx'), ('RIG', 'rigging')], max_length=50),
        ),
    ]