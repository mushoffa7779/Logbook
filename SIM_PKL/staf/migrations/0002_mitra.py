# Generated by Django 2.2.13 on 2020-09-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mitra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=225)),
                ('alamat', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]