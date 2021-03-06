# Generated by Django 4.0.5 on 2022-06-23 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_personaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_característica', models.CharField(max_length=15)),
                ('caracteristica', models.CharField(max_length=2)),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichapersonaje.personaje')),
            ],
        ),
    ]
