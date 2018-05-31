# Generated by Django 2.0.5 on 2018-05-31 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacoes', '0001_initial'),
        ('core', '0004_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacoes.Localizacao'),
        ),
    ]
