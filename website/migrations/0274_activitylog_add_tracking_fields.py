# Generated migration to add activity tracking fields to ActivityLog

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0273_issue_spam_reason_issue_spam_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="activitylog",
            name="domain",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="activitylog",
            name="activity_description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="activitylog",
            name="start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="activitylog",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
