# Generated by Django 5.0.5 on 2024-05-14 20:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Payment', '0002_remove_card_card_owner_remove_card_id_card_card_name_and_more'),
        ('Renters', '0002_remove_room_owner_acommodation_delete_apartment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_period_start', models.DateField()),
                ('rental_period_end', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Card', 'Card'), ('PSE', 'PSE'), ('PayPal', 'PayPal')], max_length=10)),
                ('payment_status', models.CharField(choices=[('On Hold', 'On Hold'), ('Approve', 'Approve'), ('Denied', 'Denied')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('acommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renters.acommodation')),
                ('card_selected', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Payment.card')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_as_seller', to=settings.AUTH_USER_MODEL)),
                ('shopper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_as_shopper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]