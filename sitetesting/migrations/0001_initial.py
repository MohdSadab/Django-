# Generated by Django 3.2.5 on 2021-07-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(max_length=255)),
                ('type', models.CharField(choices=[('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days')], max_length=255)),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('website_type', models.CharField(choices=[('Up', 'Up'), ('Down', 'Down')], max_length=10)),
            ],
        ),
    ]
