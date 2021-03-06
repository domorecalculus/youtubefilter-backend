# Generated by Django 3.2.7 on 2021-10-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_group_channels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='video_ids',
        ),
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='channel',
            name='uploads_playlist_id',
            field=models.CharField(default='UC5dR5zyXkTUsnFkOZF84aMQ', max_length=100),
            preserve_default=False,
        ),
    ]
