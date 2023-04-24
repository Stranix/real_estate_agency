# Generated by Django 2.2.24 on 2023-04-24 11:48

from django.db import migrations


def link_flats_and_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        owner, *_ = Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber
        )

        owner.flats.add(flat)



class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20230424_1431'),
    ]

    operations = [
        migrations.RunPython(link_flats_and_owners)
    ]
