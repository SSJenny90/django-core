# Generated by Django 4.2.11 on 2024-03-27 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contributors", "0001_initial"),
        ("core", "0001_initial"),
        ("organizations", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="contributor",
            name="identifiers",
            field=models.ManyToManyField(
                blank=True,
                help_text="A list of identifiers for the contributor.",
                to="core.identifier",
                verbose_name="identifiers",
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="interests",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A list of research interests for the contributor.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="research interests",
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="organization",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to="organizations.organization",
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="profile",
            field=models.ForeignKey(
                help_text="The person or organisation that contributed to the project or dataset.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="contributions",
                to="contributors.contributor",
                verbose_name="contributor",
            ),
        ),
        migrations.AddIndex(
            model_name="contribution",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="contributor_content_d2d9c8_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="contribution",
            unique_together={("profile", "content_type", "object_id")},
        ),
    ]
