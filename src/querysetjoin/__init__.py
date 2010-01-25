import re

from operator import attrgetter
from itertools import islice, chain
from django.core.exceptions import FieldError

ORDER_PATTERN = re.compile(r'\?|[-+]?[.\w]+$')
REPR_OUTPUT_SIZE= 2

class QuerySetJoin(object):
    """Does the addition of QuerySets of different models or not and returns 
    a new QuerySet with these joints.
    """

    def __init__(self, *querysets):
        self.querysets = querysets
        self.order = {}

    def __repr__(self):
        data = list(self[:REPR_OUTPUT_SIZE + 1])
        if len(data) > REPR_OUTPUT_SIZE:
            data[-1] = "...(remaining elements truncated)..."
        return repr(data)

    def __getitem__(self, ndx):
        """Return an item or slice from the junction of QuerySets
        """
        if type(ndx) is slice:
            return list(islice(self._all(), ndx.start, ndx.stop, ndx.step or 1))
        else:
            return islice(self._all(), ndx, ndx+1).next()

    def _all(self):
        """Iterates records in all subquerysets"""
        return chain(*self.querysets)

    def _clone(self):
        """Returns a clone of this querysets joined
        """
        return self.__class__(*self.querysets)

    def count(self):
        """Returns the sum of all numbers of results of each queryset
        using the count method.
        """
        return sum(qs.count() for qs in self.querysets)

    def order_by(self, field):
        """Return all items from the junction of QuerySets ordered by field
        passed as parameter. Currently it is possible to order by only one
        field. By default ascending order is specified to order from highest
        to lowest is simply add the sign "-" at the beginning of the string.
        """
        reverse = False

        if ORDER_PATTERN.match(field):
            if field[:1] == "-":
                reverse = True
                field = field[1:]
        else:
            raise FieldError("The pattern is not correctly")

        self.order = {"reverse": reverse, "key": attrgetter(field)}
        return sorted(self._all(), **self.order)

    def all(self):
        """Return all itens from the junction of QuerySets
        """
        return self._all()
