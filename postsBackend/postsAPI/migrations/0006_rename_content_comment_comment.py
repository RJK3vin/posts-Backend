# Generated by Django 4.2.17 on 2025-01-08 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postsAPI', '0005_rename_comment_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
