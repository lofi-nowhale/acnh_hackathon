# Generated by Django 5.0 on 2023-12-15 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Island',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('full', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Villagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('personality', models.CharField(max_length=200)),
                ('friendship_level', models.IntegerField()),
                ('dream_home', models.BooleanField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='IslandVillagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('island', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acnh.island')),
                ('villager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acnh.villagers')),
            ],
        ),
    ]
