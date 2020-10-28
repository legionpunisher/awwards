from django.test import TestCase

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
