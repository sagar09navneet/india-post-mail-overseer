# Generated by Django 4.1.12 on 2024-07-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_branchoffice_account_no_branchoffice_balance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchoffice',
            old_name='account_no',
            new_name='account_no_1',
        ),
        migrations.RenameField(
            model_name='branchoffice',
            old_name='balance',
            new_name='balance_1',
        ),
        migrations.RenameField(
            model_name='branchoffice',
            old_name='deposit',
            new_name='deposit_1',
        ),
        migrations.RenameField(
            model_name='branchoffice',
            old_name='last_transaction_date',
            new_name='last_transaction_date_1',
        ),
        migrations.RenameField(
            model_name='branchoffice',
            old_name='new_passbook_entry',
            new_name='new_passbook_entry_2',
        ),
        migrations.RemoveField(
            model_name='branchoffice',
            name='scheme_type',
        ),
        migrations.RemoveField(
            model_name='branchoffice',
            name='sms_alert',
        ),
        migrations.RemoveField(
            model_name='branchoffice',
            name='system_receipt',
        ),
        migrations.RemoveField(
            model_name='branchoffice',
            name='withdrawal',
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='account_no_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Account No.'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='account_no_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Account No.'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='balance_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Balance'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='balance_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Balance'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='deposit_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Deposit'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='deposit_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Deposit'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='last_transaction_date_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Date of Last Transaction'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='last_transaction_date_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Date of Last Transaction'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='new_passbook_entry_1',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='1st Page Entry of New Passbook (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='new_passbook_entry_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='1st Page Entry of New Passbook (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='scheme_type_1',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Scheme Type'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='scheme_type_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Scheme Type'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='scheme_type_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Scheme Type'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='sms_alert_1',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='SMS Alert (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='sms_alert_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='SMS Alert (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='sms_alert_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='SMS Alert (Y/N)'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='system_receipt_1',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='System Generated Receipt Provided'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='system_receipt_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='System Generated Receipt Provided'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='system_receipt_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='System Generated Receipt Provided'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='withdrawal_1',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Withdrawal'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='withdrawal_2',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Withdrawal'),
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='withdrawal_3',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Withdrawal'),
        ),
    ]
