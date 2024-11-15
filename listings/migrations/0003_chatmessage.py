# Generated by Django 5.1.2 on 2024-11-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
