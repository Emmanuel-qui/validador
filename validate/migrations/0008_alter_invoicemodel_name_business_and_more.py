# Generated by Django 4.1 on 2022-11-07 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validate', '0007_alter_validateresultmodel_estruc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='name_business',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='name_receiver',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='series',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
