# Generated by Django 5.1.3 on 2024-11-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0008_usuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]