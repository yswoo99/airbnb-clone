from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    pass


@admin.register(models.Conversation)
class CoonversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    pass
