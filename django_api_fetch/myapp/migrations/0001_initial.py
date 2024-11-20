# Generated by Django 5.1.3 on 2024-11-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("image", models.URLField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("discount", models.FloatField()),
            ],
        ),
    ]