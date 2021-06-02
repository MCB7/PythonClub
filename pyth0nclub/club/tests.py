from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event 

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='test meeting')

    def  test_typestring(self):
         self.assertEqual(str(self.type), 'test meeting') 

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinute(TestCase):
    def setUp(self):
        self.type=MeetingMinute(meetingid='test meeting')

    def  test_typestring(self):
         self.assertEqual(str(self.type), 'test meeting') 

    def test_tablename(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='Test name')

    def  test_typestring(self):
         self.assertEqual(str(self.type), 'Test name') 

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')  

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(title='Test Event')

    def  test_typestring(self):
         self.assertEqual(str(self.type), 'Test Event') 

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')