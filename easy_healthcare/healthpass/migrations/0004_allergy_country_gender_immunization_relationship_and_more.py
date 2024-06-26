# Generated by Django 4.2.7 on 2024-03-26 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("healthpass", "0003_bloodgroup_hbgenotype_hepatitisa_hepatitisb_hiv_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Allergy",
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
                    "allergy",
                    models.CharField(
                        choices=[
                            ("Balsam of Peru", "Balsam of Peru"),
                            ("Buckwheat", "Buckwheat"),
                            ("Celery", "Celery"),
                            ("Egg", "Egg"),
                            ("Fish", "Fish"),
                            ("Fruit", "Fruit"),
                            ("Garlic", "Garlic"),
                            ("Oats", "Oats"),
                            ("Maize", "Maize"),
                            ("Milk", "Milk"),
                            ("Mustard", "Mustard"),
                            ("Peanut", "Peanut"),
                            ("Poultry Meat", "Poultry Meat"),
                            ("Red Meat", "Red Meat"),
                            ("Rice", "Rice"),
                            ("Sesame", "Sesame"),
                            ("Shellfish", "Shellfish"),
                            ("Soy", "Soy"),
                            ("Sulfites", "Sulfites"),
                            ("Tartrazine", "Tartrazine"),
                            ("Tree nut", "Tree nut"),
                            ("Wheat", "Wheat"),
                            ("Tetracycline", "Tetracycline"),
                            ("Dilantin", "Dilantin"),
                            ("Tegretol", "Tegretol"),
                            ("Penicillin", "Penicillin"),
                            ("Cephalosporins", "Cephalosporins"),
                            ("Sulfonamides", "Sulfonamides"),
                            (
                                "Non-steroidal anti-inflammatories",
                                "Non-steroidal anti-inflammatories",
                            ),
                            ("Intravenous contrast dye", "Intravenous contrast dye"),
                            ("Local anesthetics", "Local anesthetics"),
                            ("Pollen", "Pollen"),
                            ("Cat", "Cat"),
                            ("Dog", "Dog"),
                            ("Insect sting", "Insect sting"),
                            ("Mold", "Mold"),
                            ("Perfume", "Perfume"),
                            ("Cosmetics", "Cosmetics"),
                            ("Semen", "Semen"),
                            ("Latex", "Latex"),
                            ("Cold stimuli", "Cold stimuli"),
                            ("House dust mite", "House dust mite"),
                            ("Nickel", "Nickel"),
                            ("Gold", "Gold"),
                            ("Chromium", "Chromium"),
                            ("Cobalt", "Cobalt"),
                            ("Formaldehyde", "Formaldehyde"),
                            ("Photographic developers", "Photographic developers"),
                            ("Fungicide", "Fungicide"),
                            ("Dimethylaminopropylamine", "Dimethylaminopropylamine"),
                            ("Latex", "Latex"),
                            ("Paraphenylenediamine", "Paraphenylenediamine"),
                            (
                                "Glyceryl monothioglycolate",
                                "Glyceryl monothioglycolate",
                            ),
                            (
                                "Toluenesulfonamide formaldehyde",
                                "Toluenesulfonamide formaldehyde",
                            ),
                        ],
                        max_length=400,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                    "country",
                    models.CharField(
                        choices=[
                            ("Algeria", "DZA"),
                            ("Angola", "AGO"),
                            ("Benin", "BEN"),
                            ("Botswana", "BWA"),
                            ("Burkina Faso", "BFA"),
                            ("Burundi", "BDI"),
                            ("Cameroon", "CMR"),
                            ("Cape Verde", "CPV"),
                        ],
                        max_length=150,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gender",
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
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=5,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Immunization",
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
                    "immunization",
                    models.CharField(
                        choices=[
                            ("Hepatitis B", "HEPB"),
                            (
                                "Diphtheria, Tetanus, and Whooping Cough(Pertussis)",
                                "DTAP",
                            ),
                            ("Haemophilus Influenzae Type B", "HIB"),
                            ("Polio", "IPV"),
                            ("Pneumococcal", "PCV"),
                            ("Rotavirus", "RV"),
                            ("Influenza", "FLU"),
                            ("Chickenpox", "VARICELLA"),
                            ("Measles, Mumps, Rubella", "MMR"),
                            ("Hepatitis A", "HEPA"),
                            ("Human Papillomavirus", "HPV"),
                            ("Meningococcal Conjugate", "MENACWY"),
                            ("Serogroup B Meningococcal", "MENB"),
                            ("Pentavalent", "MENABCWY"),
                            ("Shingles", "ZOSTER"),
                        ],
                        max_length=300,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Relationship",
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
                    "relationship",
                    models.CharField(
                        choices=[
                            ("Grandfather", "GF"),
                            ("Grandmother", "GM"),
                            ("Father", "F"),
                            ("Mother", "M"),
                            ("Uncle", "U"),
                            ("Aunt", "A"),
                            ("Son", "S"),
                            ("Daughter", "D"),
                            ("Grandson", "GS"),
                            ("Granddaughter", "GD"),
                            ("Brother", "BRO"),
                            ("Sister", "SIS"),
                            ("Cousin", "C"),
                            ("Nephew", "N"),
                            ("Niece", "NC"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeneralInfo",
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
                    "passport_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        help_text="Please use the following format: <em>YYYY-MM-DD</em>."
                    ),
                ),
                (
                    "weight",
                    models.FloatField(
                        blank=True,
                        help_text="Please Enter your weight value",
                        null=True,
                    ),
                ),
                ("name_of_emergency_contact", models.CharField(max_length=300)),
                (
                    "email_of_emergency_contact",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "phone_number_of_emergency_contact",
                    models.CharField(
                        blank=True,
                        help_text="Please start your phone number with your country code first",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "allergies",
                    models.ManyToManyField(
                        related_name="allergy_general_info", to="healthpass.allergy"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="country_general_info",
                        to="healthpass.country",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="gender_general_info",
                        to="healthpass.gender",
                    ),
                ),
                (
                    "immunizations",
                    models.ManyToManyField(
                        related_name="immunization_general_info",
                        to="healthpass.immunization",
                    ),
                ),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_general_info",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "relationship",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="relationship_general_info",
                        to="healthpass.relationship",
                    ),
                ),
            ],
        ),
    ]
