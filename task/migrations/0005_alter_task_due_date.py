# Generated by Django 4.2.6 on 2023-11-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_task_created_task_updated_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
    ]
