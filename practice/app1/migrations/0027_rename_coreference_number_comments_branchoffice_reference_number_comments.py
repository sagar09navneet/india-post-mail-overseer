# Generated by Django 4.1.12 on 2024-06-08 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_branchoffice_acquittance_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchoffice',
            old_name='coreference_number_comments',
            new_name='reference_number_comments',
        ),
    ]
