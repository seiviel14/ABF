# Generated by Django 4.0.5 on 2022-06-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapersonaje', '0002_rename_nombre_característica_caracteristicas_nombre_caracteristica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristicas',
            name='caracteristica',
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='valor',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
