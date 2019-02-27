import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import Action


def create_action(user, verb, content_object=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb,
                                            created__gte=last_minute)
    if content_object:
        content_type = ContentType.objects.get_for_model(content_object)
        similar_actions = similar_actions.filter(content_type=content_type,
                                                 object_id=content_object.id)
    if not similar_actions:
        action = Action(user=user, verb=verb, content_object=content_object)
        action.save()
        return True
    return False
