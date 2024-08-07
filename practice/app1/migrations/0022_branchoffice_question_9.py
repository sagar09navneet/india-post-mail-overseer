# Generated by Django 4.1.12 on 2024-06-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_branchoffice_bo_account_branchoffice_bo_slip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchoffice',
            name='question_9',
            field=models.TextField(blank=True, default=dict, null=True, verbose_name='Examine the BO Accounts since the last visit to see that the BPM has not unnecessarily retained excess cash. Examine whether the arrangements for exchange of cash with the Account Office are satisfactory and record instances of delay in payment of Money Orders, Savings Bank withdrawals etc. for want of funds. Whether the norms for remittances have been followed as mentioned in the Directorate letter No.24- 3/2012/PO dated 01/10/2018. Educate the BPM on the procedure to be followed if the amount exceeds the prescribed limit.'),
        ),
    ]
