# Generated by Django 5.0.2 on 2024-05-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='usrpswd',
            field=models.CharField(default='ethesag', max_length=45),
            preserve_default=False,
        ),
    ]
