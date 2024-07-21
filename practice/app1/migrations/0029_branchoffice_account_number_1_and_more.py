# Generated by Django 4.1.12 on 2024-06-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_branchoffice_account_details_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchoffice',
            name='account_number_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='account_number_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='applications_received',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='applications_received_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='authorization_forms_available',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='authorization_forms_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='dispatched_to_account_office',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='dlt_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='dlt_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='doorstep_service_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='doorstep_service_requests',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='feedback_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='help_desk_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='help_desk_maintained',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='inventory_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='inventory_levels_maintained',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_policy_number_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_policy_number_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_proposal_type_2',
            field=models.CharField(choices=[('PLI', 'PLI'), ('RPLI', 'RPLI')], default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_proposals',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_publicity_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_publicity_material',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_transactions_type_1',
            field=models.CharField(choices=[('PLI', 'PLI'), ('RPLI', 'RPLI')], default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='pli_rpli_transactions_type_2',
            field=models.CharField(choices=[('PLI', 'PLI'), ('RPLI', 'RPLI')], default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='qr_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branchoffice',
            name='qr_displayed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
