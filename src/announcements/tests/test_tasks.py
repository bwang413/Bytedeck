from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy
import djconfig

from announcements import tasks
from announcements.models import Announcement

User = get_user_model()


class AnnouncementTasksTests(TestCase):
    """ Run tasks asyncronously with apply() """

    def setUp(self):
        djconfig.reload_maybe()

        self.announcement = mommy.make(Announcement)

        # need a teacher before students can be created or the profile creation will fail when trying to notify
        self.test_teacher = User.objects.create_user('test_teacher', is_staff=True)
        self.test_student1 = User.objects.create_user('test_student')
        self.test_student2 = mommy.make(User)

    def test_send_announcement_emails(self):
        task_result = tasks.send_announcement_emails.apply(kwargs={"content": "", "url": "https://example.com"})
        self.assertTrue(task_result.successful())

    def test_publish_announcement(self):
        self.assertTrue(self.announcement.draft)
        task_result = tasks.publish_announcement.apply(
            kwargs={
                'user_id': self.test_teacher.id,
                'announcement_id': self.announcement.id,
                'absolute_url': "https://example.com"
            }
        )
        self.assertTrue(task_result.successful())

        # Make sure the announcement is no longer a draft
        # get updated instance of announcement
        no_longer_draft_announcement = Announcement.objects.get(pk=self.announcement.pk)
        self.assertFalse(no_longer_draft_announcement.draft)

    def test_send_notifications(self):
        # run method as synchronous task
        task_result = tasks.send_notifications.apply(
            kwargs={
                'user_id': self.test_teacher.id,
                'announcement_id': self.announcement.id
            })
        self.assertTrue(task_result.successful())
