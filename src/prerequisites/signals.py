from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from badges.models import Badge
from prerequisites.models import Prereq
from prerequisites.tasks import update_conditions_for_quest, update_quest_conditions_for_user, update_quest_conditions_all_users

User = get_user_model()


# @receiver([post_save, post_delete], sender=BadgeAssertion)
# def update_cache_triggered_by_badge_assertion(sender, instance, *args, **kwargs):
#     """ When a user earns a badge, recalculate what quests are available to them.
#     """
#     BadgeAssertion.badge
#     update_quest_conditions_for_user.apply_async(args=[instance.user_id], queue='default')


@receiver([post_save, post_delete], dispatch_uid="prerequisites.signals.update_cache_triggered_by_task_completion")
def update_cache_triggered_by_task_completion(sender, instance, *args, **kwargs):
    """ When a user completes a task (e.g. earns a badge, has a quest submission approved or rejected, or joins a course)
    Recalculate what is available to them.
    """

    # Do not proceed updating cache if an instance was just created
    if kwargs.get('created') is True:
        return

    list_of_models = ('BadgeAssertion', 'QuestSubmission', 'CourseStudent')
    if sender.__name__ in list_of_models:
        # TODO Since the cache is only for quests (as prereq parent object), only need to send for affected quests, not ALL quests?
        update_quest_conditions_for_user.apply_async(args=[instance.user_id], queue='default')


# Don't need post_delete, it doesn't affect on result and will be updated on next all conditions update
# @receiver([post_save], sender=Quest)
# def update_conditions_met_for_quest(sender, instance, *args, **kwargs):
#     update_conditions_for_quest.apply_async(kwargs={'quest_id': instance.id, 'start_from_user_id': 1}, queue='default')


# @receiver([post_save, post_delete], sender=Prereq)
@receiver([post_save, post_delete], sender=Badge, dispatch_uid="prerequisites.signals.update_conditions_met")
def update_conditions_met(sender, instance, *args, **kwargs):
    update_quest_conditions_all_users.apply_async(args=[1], queue='default', countdown=settings.CONDITIONS_UPDATE_COUNTDOWN)


@receiver([post_save, post_delete], sender=Prereq, dispatch_uid="prerequisites.signals.update_cache_triggered_by_prereq")
def update_cache_triggered_by_prereq(sender, instance, *args, **kwargs):
    """ Update the cache of available quests (PreqAllConditionsMet) for relevant users when Prereq objects are changed,
    If the parent of the Prereq object is a quest. (i.e a quest's prereqs were changed)
    """
    if instance.parent_content_type.model == 'quest':
        # # The parent_object itself being deleted could have cascaded to delete the sender Prereq, so it parent might not exist.
        # Cover this instance in a post_delete signal receiver for Quest objects.
        if instance.parent_object:
            update_conditions_for_quest.apply_async(kwargs={'quest_id': instance.parent_object.id, 'start_from_user_id': 1}, queue='default')
