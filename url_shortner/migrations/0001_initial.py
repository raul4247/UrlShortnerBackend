# Generated by Django 2.0.2 on 2018-04-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('complete_url', models.CharField(max_length=2000)),
                ('short_url', models.CharField(max_length=15)),
            ],
        ),
    ]
