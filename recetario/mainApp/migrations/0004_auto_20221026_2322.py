# Generated by Django 3.1.1 on 2022-10-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_receta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
