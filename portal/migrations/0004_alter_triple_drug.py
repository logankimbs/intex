# Generated by Django 3.2.9 on 2021-12-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20211204_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triple',
            name='drug',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='portal.drugs'),
        ),
    ]