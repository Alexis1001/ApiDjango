# Generated by Django 2.2.1 on 2019-06-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_auto_20190621_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Example2',
            },
        ),
    ]
