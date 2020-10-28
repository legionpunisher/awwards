from django.test import TestCase
from .models import *
# Create your tests here.
class ProjectTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='a')
        self.task = Project.objects.create(id=1,
                                           by=self.user,
                                           title='a',
                                           description='b',
                                           link='c')

    def test_instance(self):
        self.assertTrue(isinstance(self.task,Project))

    def test_get_project(self):
        self.task.save()
        project = Project.get_project('a')
        self.assertTrue(len(project)>0)

    def test_search(self):
        self.task.save()
        project = Project.search('a')
        self.assertTrue(len(project)>0)

    def test_single_project(self):
        self.task.save()
        project = Project.single_project(1)
        self.assertTrue(len(project)>0)
class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='a')
        self.task = Project.objects.create(id=1,
                                           by=self.user,
                                           title='a',
                                           description='b',
                                           link='c')
        self.profile = Profile.objects.create(name=self.user,
                                              bio='b',
                                              projects=self.task,
                                              contact='c')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile('a')
        self.assertTrue(len(profile)>0)
class RateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='a')
        self.task = Project.objects.create(by=self.user,
                                           title='a',
                                           description='b',
                                           link='c')
        self.rate = Rate.objects.create(rater=self.user,
                                        task=self.task,
                                        design='3',
                                        content='3',
                                        usability='3',
                                        average='3',
                                        review='a')

    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rate))
