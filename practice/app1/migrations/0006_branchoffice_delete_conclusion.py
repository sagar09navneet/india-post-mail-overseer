# Generated by Django 5.0.1 on 2024-04-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0005_delete_acquittance_delete_branchoffice_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BranchOffice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "branch_name",
                    models.CharField(
                        max_length=100, verbose_name="Name of the Branch Office (BO)"
                    ),
                ),
                (
                    "account_office_name",
                    models.CharField(
                        max_length=100, verbose_name="Name of the Account Office (AO)"
                    ),
                ),
                (
                    "head_office_name",
                    models.CharField(
                        max_length=100, verbose_name="Name of the Head Office"
                    ),
                ),
                (
                    "facility_id",
                    models.IntegerField(
                        verbose_name="Facility ID of the BO Profit/Cost centre ID of the BO"
                    ),
                ),
                (
                    "establishment",
                    models.DateField(verbose_name="Establishment of the BO"),
                ),
                (
                    "last_inspection",
                    models.DateField(
                        verbose_name="Date of Last Inspection (DLI) and by whom"
                    ),
                ),
                (
                    "subsequent_visits",
                    models.DateField(
                        verbose_name="Date of subsequent visits by Mail Overseer since DLI"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Conclusion",
        ),
    ]
