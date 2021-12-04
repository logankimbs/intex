# Generated by Django 3.2.9 on 2021-12-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_alter_triple_drug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triple',
            name='drug',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='portal.drugs'),
        ),
        migrations.AlterField(
            model_name='triple',
            name='prescriberid',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='portal.prescribers'),
        ),
    ]