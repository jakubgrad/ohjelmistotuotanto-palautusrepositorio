from matchers import *

class QueryBuilder:
    def __init__(self, build = All()):
        self.build_object = build

    def plays_in(self,team_name):
        return QueryBuilder(And(self.build_object, PlaysIn(team_name)))

    def has_at_least(self, number, attribute):
        return QueryBuilder(And(self.build_object, HasAtLeast(number, attribute)))

    def has_fewer_than(self, number, attribute):
        return QueryBuilder(And(self.build_object, HasFewerThan(number, attribute)))

    def build(self):
        return self.build_object