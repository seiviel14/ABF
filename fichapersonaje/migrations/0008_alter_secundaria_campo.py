# Generated by Django 4.0.5 on 2022-06-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapersonaje', '0007_secundaria_campo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secundaria',
            name='campo',
            field=models.CharField(max_length=200),
        ),
    ]
