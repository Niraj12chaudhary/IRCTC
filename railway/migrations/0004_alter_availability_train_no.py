# Generated by Django 4.2.4 on 2024-09-02 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0003_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='train_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_journeys', to='railway.train', unique=True),
        ),
    ]
