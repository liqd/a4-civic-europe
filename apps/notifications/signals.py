from django.db.models import signals
from django.dispatch import receiver

from adhocracy4.actions.models import Action
from adhocracy4.actions.verbs import Verbs
from adhocracy4.comments.models import Comment
from apps.ideas.models import Idea
from apps.journeys.models import JourneyEntry

from . import emails


@receiver(signals.post_save, sender=Action)
def send_create_notification(sender, instance, created, **kwargs):
    action = instance
    if action.verb == Verbs.ADD.value:
        modelcls = action.obj_content_type.model_class()

        if (modelcls is Idea):
            emails.SubmitIdeaNotification.send(action.obj)
        elif (modelcls is Comment):
            emails.NotifyCreatorEmail.send(action)
            emails.NotifyFollowersOnNewComment.send(action)
        elif (modelcls is JourneyEntry):
            emails.SubmitJourneyNotification.send(action.obj)
            emails.NotifyFollowersOnNewJourney.send(action)
