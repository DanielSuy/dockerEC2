# Generated by Django 5.0 on 2023-12-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineaasignacion',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]