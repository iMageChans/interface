# Generated by Django 5.0.7 on 2024-08-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_profile', '0008_alter_usermerchantprofile_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToNodeVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=255)),
                ('node_id', models.CharField(max_length=255)),
                ('node_name', models.CharField(max_length=255)),
                ('vote', models.CharField(max_length=255)),
            ],
        ),
    ]
