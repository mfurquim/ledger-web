# Generated by Django 2.1.7 on 2019-04-12 16:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payee', models.CharField(max_length=512)),
                ('new_payee', models.CharField(blank=True, max_length=512)),
                ('acc_from', models.CharField(blank=True, max_length=512, verbose_name='Account from')),
                ('acc_to', models.CharField(blank=True, max_length=512, verbose_name='Account to')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(32)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together={('payee', 'user')},
        ),
    ]
