from django.test import TestCase
from django.core.files import File
from architect.models import Architect, Classification, Project
from architect import utf8lit

class ModelTests(TestCase):

    def setUp(self):
        super(ModelTests,self).setUp()
        self.add_architects()
        self.add_classifications()
        
    def tearDown(self):
        super(ModelTests,self).tearDown()
        for m in (Architect, Classification, Project):
            m.objects.all().delete()
            self.assertEqual( m.objects.count(), 0 )
                
    def add_architects(self):
        for a in utf8lit.test_architects:
            arch = Architect( firstname_e = a[0], lastname_e = a[1],
                firstname_h = a[2], lastname_h = a[3],
                email = a[4], portrait = File(file(a[5])) )
            arch.save()
        
    def add_classifications(self):
        for c in ('Commercial', 'Residential'):
            classification = Classification( title_e = c[0], title_h = c[1] )
            classification.save()
            
    def add_projects(self):
        p = Project()
        self.assertNotEqual(p, None)
        
    def test_add_stuff(self):
        self.assertEqual( Architect.objects.count(), 2 )
        danny = Architect.objects.get( firstname_e = 'Danny' )
        self.assertEqual( danny.lastname_e, 'Din' )

        
