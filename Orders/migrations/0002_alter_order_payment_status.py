# Generated by Django 5.0.5 on 2024-05-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('On Hold', 'On Hold'), ('Approved', 'Approved'), ('Denied', 'Denied')], max_length=10),
        ),
    ]
