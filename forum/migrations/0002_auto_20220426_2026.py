# Generated by Django 3.2.2 on 2022-04-26 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussione',
            old_name='autore',
            new_name='autore_discussione',
        ),
        migrations.RenameField(
            model_name='sezione',
            old_name='destrizione',
            new_name='descrizione',
        ),
    ]
