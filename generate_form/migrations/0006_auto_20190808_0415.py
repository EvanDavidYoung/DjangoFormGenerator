# Generated by Django 2.2.3 on 2019-08-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_form', '0005_auto_20190808_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_model',
            name='form_response',
            field=models.CharField(blank=True, default='', max_length=1000000),
        ),
    ]
