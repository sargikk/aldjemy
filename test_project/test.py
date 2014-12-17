from django.test import TestCase
from sample.models import StaffAuthor


class AldjemyTestCase(TestCase):

    def test_sa_created(self):
        StaffAuthor.objects.create(name=u'abacaba', role=u'none', biography=u"test author")
        assert StaffAuthor.sa.query().count() == 1
