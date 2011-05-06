from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('Comment', 'issue_opened', models.BooleanField, initial=False),
    AddField('Comment', 'issue_status', models.CharField,
             initial='', max_length=1)
    AddField('ScreenshotComment', 'issue_opened', models.BooleanField,
             initial=False),
    AddField('ScreenshotComment', 'issue_status', models.CharField,
             initial='', max_length=1)
]

