# Generated by Django 4.2.7 on 2023-11-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toregion',
            name='date_received',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='date_received_by_region',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='date_received_from_region',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='date_sent_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='date_sent_to_teams',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='date_signed_sa',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='toregion',
            name='document_date',
            field=models.DateField(),
        ),
    ]
