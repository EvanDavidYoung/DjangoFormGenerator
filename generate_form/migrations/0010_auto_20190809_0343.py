# Generated by Django 2.2.3 on 2019-08-09 03:43

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('generate_form', '0009_auto_20190809_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_model',
            name='form_response',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
