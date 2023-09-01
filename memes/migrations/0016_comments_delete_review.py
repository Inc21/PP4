# Generated by Django 4.2.3 on 2023-08-28 00:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_options_alter_userprofile_user_img'),
        ('memes', '0015_contactemail_alter_meme_sad_face_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='memes.meme')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userprofile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]