from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, query = None, query_object = None):
        if query_object == None:
            self.query_object = query
        else:
            self.query_object = And(query_object, query)

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team), self.query_object)

    def hasAtLeast(self, atleast, what):
        return QueryBuilder(HasAtLeast(atleast, what), self.query_object)

    def hasFewerThan(self, fewerthan, what):
        return QueryBuilder(HasFewerThan(fewerthan, what), self.query_object)

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2), self.query_object)

    def build(self):
        if self.query_object == None:
            self.query_object = All()
        return self.query_object
