# Generated by Django 4.0.5 on 2022-06-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichapersonaje', '0008_alter_secundaria_campo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica',
            name='valor',
            field=models.CharField(default=1, max_length=2),
        ),
    ]
