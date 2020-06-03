# Generated by Django 2.2.12 on 2020-05-13 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0058_auto_20200511_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='is_sponsored_root_folder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='folder',
            name='read_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='folder',
            name='sponsored_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_folders', to='perma.Registrar'),
        ),
        migrations.AddField(
            model_name='historicallinkuser',
            name='sponsored_root_folder',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='perma.Folder'),
        ),
        migrations.AddField(
            model_name='linkuser',
            name='sponsored_root_folder',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_user', to='perma.Folder'),
        ),
    ]