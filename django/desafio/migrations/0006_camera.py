# Generated by Django 3.0.7 on 2020-06-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0005_auto_20200615_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera', models.ManyToManyField(to='desafio.Post')),
            ],
        ),
    ]