# django-queryset-join

Django queryset join is a simple way to join QuerySets of different models and
manipulates them.

Ideas, modifications, patches are welcome:
http://github.com/hersonls/django-queryset-join

## Usage

To join QuerySets of different models is very simple just instantiating the
class querysetjoin.QuerySetJoin passing as parameters the threads QuerySets
desired.

Available methods are:

* function:: all()

   Return all itens from the junction of QuerySets

* function:: order(field)

   Return all items from the junction of QuerySets ordered by field passed as
   parameter. Currently it is possible to order by only one field. By default
   ascending order is specified to order from highest to lowest is simply add
   the sign "-" at the beginning of the string.


Example below:

```python
    >>> from querysetjoin import QuerySetJoin
    >>> from models import ModelOne, ModelTwo
    >>>
    >>> # Join QuerySets
    >>> qs_join = QuerySetJoin(qs1, qs2)
    >>>
    >>> # Count of all itens
    >>> test_print("Counting of all itens of the joined querysets:")
    >>> print qs_join.count()
    4
    >>> # Printing the attributes in common
    >>> for qs in qs_join:
    >>>    print qs.name
    Hersonls
    Tomas
    A: test case model two
    B: test case model two
    >>> # Ordering objects by attribute "name" ordening by ASC
    >>> for qs in qs_join.order_by("name"):
    >>>    print qs.name
    A: test case model two
    B: test case model two
    Hersonls
    Tomas
    >>> # Ordering objects by attribute "name" ordening by DESC
    >>> for qs in qs_join.order_by("-name"):
    >>>    print qs.name
    Tomas
    Hersonls
    B: test case model two
    A: test case model two
```

## To-Do

Following is the list of features to be added:

1. Order by more than one field

Suggestions are welcome at:
http://github.com/hersonls/django-queryset-join