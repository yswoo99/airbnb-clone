from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField(default=5)
    cleanliness = models.IntegerField(default=5)
    location = models.IntegerField(default=5)
    check_in = models.IntegerField(default=5)
    value = models.IntegerField(default=5)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.review} - {self.room}"
