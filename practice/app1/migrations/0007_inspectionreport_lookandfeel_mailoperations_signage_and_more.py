# Generated by Django 5.0.1 on 2024-04-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0006_branchoffice_delete_conclusion"),
    ]

    operations = [
        migrations.CreateModel(
            name="InspectionReport",
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
                    "previous_inspection_pending",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
                ("previous_inspection_comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="LookAndFeel",
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
                    "look_and_feel",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
                ("look_and_feel_comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MailOperations",
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
                    "articles_in_deposit_comments",
                    models.TextField(verbose_name="No. of articles in deposit"),
                ),
                (
                    "articles_beyond_period",
                    models.BooleanField(
                        verbose_name="Whether articles beyond prescribed period"
                    ),
                ),
                (
                    "articles_beyond_period_comments",
                    models.TextField(
                        verbose_name="Comments on articles beyond prescribed period"
                    ),
                ),
                (
                    "article_condition",
                    models.BooleanField(
                        verbose_name="Whether article in deposit in good condition"
                    ),
                ),
                (
                    "article_condition_comments",
                    models.TextField(verbose_name="Comments on article condition"),
                ),
                (
                    "compare_articles_comments",
                    models.TextField(
                        verbose_name="Compare the number of articles in deposit comments"
                    ),
                ),
                (
                    "check_delivery_status",
                    models.BooleanField(verbose_name="Check delivery status"),
                ),
                (
                    "check_delivery_status_comments",
                    models.TextField(verbose_name="Comments on delivery status"),
                ),
                ("date_of_receipt", models.DateField(verbose_name="Date of receipt")),
                ("date_of_delivery", models.DateField(verbose_name="Date of delivery")),
            ],
        ),
        migrations.CreateModel(
            name="Signage",
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
                    "bo_signage",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
                ("signage_comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="WorkCarriedOut",
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
                    "work_carried_out",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
                ("work_carried_out_comments", models.TextField()),
            ],
        ),
    ]
