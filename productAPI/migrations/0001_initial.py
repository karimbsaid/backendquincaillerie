# Generated by Django 5.0.6 on 2024-06-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('reference', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
            ],
        ),
    ]
