# Generated by Django 3.0.2 on 2020-01-07 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_auto_20200107_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerhistory',
            name='player',
        ),
        migrations.AddField(
            model_name='player',
            name='history',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='player.PlayerHistory'),
        ),
    ]
