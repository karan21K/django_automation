# Generated by Django 5.0.1 on 2024-03-28 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0005_emailtracking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='send_at',
            new_name='sent_at',
        ),
    ]
