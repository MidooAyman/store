# Generated by Django 4.1.6 on 2023-04-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_login_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='login',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='login',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='login',
            name='size',
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(default='default_username', max_length=100),
        ),
    ]
