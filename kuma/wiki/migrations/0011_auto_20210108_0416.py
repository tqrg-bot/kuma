# Generated by Django 2.2.16 on 2021-01-08 04:16

from django.db import migrations


def forward(apps, schema_editor):
    Flag = apps.get_model("waffle", "Flag")
    Flag.objects.filter(
        name__in=["kumaediting", "page_move", "section_edit", "spam_checks_enabled"]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0010_auto_20210107_1338"),
    ]

    operations = [migrations.RunPython(forward)]
