# Generated by Django 5.1.1 on 2024-10-07 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_surveyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyimage',
            name='question_id',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestion'),
        ),
    ]