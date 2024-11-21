# Generated by Django 5.1.1 on 2024-11-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTypeFlow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('dimension', models.CharField(choices=[('EI', 'Extroversion/Introversion'), ('SN', 'Sensing/Intuition'), ('TF', 'Thinking/Feeling'), ('JP', 'Judging/Perceiving')], max_length=2)),
            ],
        ),
    ]
