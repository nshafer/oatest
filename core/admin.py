from django.contrib import admin
from django_object_actions import DjangoObjectActions

from core.models import Article


@admin.register(Article)
class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    change_actions = ['publish_this']

    def get_change_actions(self, request, object_id, form_url):
        actions = super().get_change_actions(request, object_id, form_url)
        actions = list(actions)

        # Uncomment this to unquote the object_id
        # from django.contrib.admin.utils import unquote
        # object_id = unquote(object_id)

        print("object_id", object_id)
        obj = self.model.objects.get(pk=object_id)
        if obj.published:
            actions.remove('publish_this')
        return actions

    def publish_this(self, request, obj):
        obj.published = True
        obj.save(update_fields=['published'])
