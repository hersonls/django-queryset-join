from django.conf import settings
from django.test import TestCase
from querysetjoin import QuerySetJoin
from querysetjoin.tests.models import ModelOne, ModelTwo

def test_print(p):
    print "*" * 70
    print p
    print "*" * 70

class QuerySetJoinTests(TestCase):
    fixtures = ['querysetjoin-test-data.json']

    def testJoin(self):
        qs1 = ModelOne.objects.all()
        qs2 = ModelTwo.objects.all()

        # Join QuerySets
        qs_join = QuerySetJoin(qs1, qs2)

        # Count of all itens
        test_print("Counting of all itens of the joined querysets:")
        print qs_join.count()
        
        # Printing the attributes in common
        test_print("Printing attributes in common of the joined QuerySets:")

        for qs in qs_join:
            print qs.name
        
        # Ordering objects by attribute "name" ordening by ASC
        test_print("Ordering the objects by attribute name ASC:")
        
        for qs in qs_join.order_by("name"):
            print qs.name
        
        # Ordering objects by attribute "name" ordening by DESC
        test_print("Ordering the objects by attribute name by DESC:")
        
        for qs in qs_join.order_by("-name"):
            print qs.name