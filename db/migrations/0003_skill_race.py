# Generated by Django 4.0.2 on 2022-09-09 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_guild_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]