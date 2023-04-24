# Generated by Django 2.2.24 on 2023-04-24 11:18

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230424_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='like_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True, verbose_name='ФИО владельца:')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, db_index=True, region=None, verbose_name='Нормализованный номер телефона:')),
                ('phonenumber', models.CharField(max_length=20, db_index=True, verbose_name='Номер телефона:')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности:')),
            ],
        ),
    ]
