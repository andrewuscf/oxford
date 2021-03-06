from datetime import datetime

from django.db import models


class PublishableModelManager(models.Manager):
    def get_queryset(self):
        return super(PublishableModelManager, self).get_query_set().filter((
            models.Q(published=True)
        ) & (
            models.Q(publication_date__isnull=True) | models.Q(publication_date__lte=datetime.now())
        ) & (
            models.Q(expiration_date__isnull=True) | models.Q(expiration_date__gt=datetime.now())
            )
        )
