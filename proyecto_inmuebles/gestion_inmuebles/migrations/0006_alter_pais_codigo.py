# Generated by Django 5.1.3 on 2024-11-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0005_alter_pais_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='codigo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
