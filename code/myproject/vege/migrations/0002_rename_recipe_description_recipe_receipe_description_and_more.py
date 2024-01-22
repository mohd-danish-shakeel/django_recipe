# Generated by Django 5.0.1 on 2024-01-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_description',
            new_name='receipe_description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='receipe_name',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_image',
        ),
        migrations.AddField(
            model_name='recipe',
            name='receipe_image',
            field=models.ImageField(default='', upload_to='receipe_images/'),
            preserve_default=False,
        ),
    ]