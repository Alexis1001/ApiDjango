# Generated by Django 2.2.1 on 2019-07-11 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='cotrasenia',
            new_name='contrasenia',
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='re_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denuncias', to='denuncias.Usuario'),
        ),
    ]
