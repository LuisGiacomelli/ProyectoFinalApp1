# Generated by Django 4.0.5 on 2022-09-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_dia_vuelo_fecha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('id_vuelo', models.IntegerField()),
            ],
        ),
    ]
