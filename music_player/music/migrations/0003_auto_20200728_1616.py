# Generated by Django 3.0.3 on 2020-07-28 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favorite',
            new_name='is_favourite',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_image',
        ),
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='./media/tp1.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='album',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='./media/tp1.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.CharField(max_length=20),
        ),
    ]
