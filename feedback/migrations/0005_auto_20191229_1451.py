# Generated by Django 2.2.8 on 2019-12-29 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='votes',
            new_name='upvotes',
        ),
    ]
