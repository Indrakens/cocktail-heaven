# Generated by Django 3.2.22 on 2023-11-09 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_featured_image_alt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='for_serving',
            new_name='additional',
        ),
    ]
