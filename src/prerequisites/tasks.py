from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from celery import shared_task

from quest_manager.models import Quest
from prerequisites.models import Prereq, PrereqAllConditionsMet


User = get_user_model()


@shared_task(name='update_quest_conditions_for_user')
def update_quest_conditions_for_user(user_id):
    user = User.objects.filter(id=user_id).first()
    if not user:
        return
    pk_met_list = [obj.pk for obj in Quest.objects.all() if Prereq.objects.all_conditions_met(obj, user)]
    met_list, created = PrereqAllConditionsMet.objects.update_or_create(
        user=user, model_name=Quest.get_model_name(), defaults={'ids': str(pk_met_list)})
    return met_list.id


@shared_task(name='update_conditions_for_quest')
def update_conditions_for_quest(quest_id, start_from_user_id):
    quest = Quest.objects.filter(id=quest_id).first()
    if not quest:
        return

    users = User.objects.filter(id__gte=start_from_user_id)[:25]
    for user in users:
        if not Prereq.objects.all_conditions_met(quest, user):
            return

        filter_kwargs = {'user': user, 'model_name': Quest.get_model_name()}
        met_list = PrereqAllConditionsMet.objects.filter(**filter_kwargs).first()
        if met_list:
            met_list.add_id(quest.id)
        else:
            met_list = PrereqAllConditionsMet.objects.create(ids=[quest.id], **filter_kwargs)
    else:
        user = User.objects.filter(id__gte=user.id + 1).values('id').first()
        if user:
            update_conditions_for_quest.apply_async(
                kwargs={'quest_id': quest.id, 'start_from_user_id': user['id'] + 1}, queue='default', countdown=20
            )


@shared_task(name='update_quest_conditions_all')
def update_quest_conditions_all(start_from_user_id):
    if start_from_user_id == 1 and cache.get('update_conditions_all_task_waiting'):
        return

        cache.set('update_conditions_all_task_waiting', True, settings.CONDITIONS_UPDATE_COUNTDOWN)

    users = User.objects.filter(id__gte=start_from_user_id).values_list('id', flat=True)[:25]
    for uid in users:
        update_quest_conditions_for_user.apply_async(args=[uid], queue='default')
    else:
        user = User.objects.filter(id__gte=uid + 1).values('id').first()
        if user:
            update_quest_conditions_all.apply_async(args=[user['id']], queue='default', countdown=30)
