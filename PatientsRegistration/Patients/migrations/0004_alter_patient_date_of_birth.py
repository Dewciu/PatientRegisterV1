# Generated by Django 4.0.1 on 2022-02-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
