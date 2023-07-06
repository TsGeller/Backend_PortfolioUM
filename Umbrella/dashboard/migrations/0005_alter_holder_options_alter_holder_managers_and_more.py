# Generated by Django 4.2.2 on 2023-07-06 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0004_alter_stock_name_stock"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="holder",
            options={},
        ),
        migrations.AlterModelManagers(
            name="holder",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="holder",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="user_permissions",
        ),
        migrations.RemoveField(
            model_name="holder",
            name="username",
        ),
        migrations.AlterField(
            model_name="walletcashflow",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.holder"
            ),
        ),
    ]