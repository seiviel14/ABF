# Generated by Django 4.0.5 on 2022-06-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapersonaje', '0004_rename_caracteristicas_caracteristica_secundaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]