# Generated by Django 4.2.4 on 2024-09-02 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='end_journey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_journeys', to='railway.station'),
        ),
    ]
