# Generated by Django 4.2.3 on 2023-08-28 19:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_options_alter_userprofile_user_img'),
        ('memes', '0017_remove_comments_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='memes.meme')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userprofile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.RenameModel(
            old_name='contactEmail',
            new_name='ContactForm',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
