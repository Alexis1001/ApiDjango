# Generated by Django 2.2.1 on 2019-07-11 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=1000)),
                ('cotrasenia', models.CharField(blank=True, max_length=1000)),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='media/')),
                ('date_joined', models.DateField()),
                ('delete', models.BooleanField(default=False)),
                ('re_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='denuncias.Usuario')),
            ],
            options={
                'db_table': 'denuncia',
            },
        ),
    ]
