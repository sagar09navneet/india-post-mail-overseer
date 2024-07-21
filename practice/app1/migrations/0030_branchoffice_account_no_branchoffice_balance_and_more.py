# Generated by Django 4.1.12 on 2024-07-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_branchoffice_account_number_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchoffice',
            name='account_no',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Account No.'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='balance',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Balance'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='deposit',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Deposit'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='last_transaction_date',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Date of Last Transaction'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='new_passbook_entry',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='1st Page Entry of New Passbook (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='scheme_type',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Scheme Type'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='sms_alert',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='SMS Alert (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='system_receipt',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='System Generated Receipt Provided'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='withdrawal',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Withdrawal'),
        ),
    ]
