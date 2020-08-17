# Generated by Django 3.0.2 on 2020-01-07 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_auto_20200107_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='score',
        ),
        migrations.AddField(
            model_name='points',
            name='match',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='match.Match'),
        ),
    ]
