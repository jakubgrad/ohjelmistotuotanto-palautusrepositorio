from matchers import All

class QueryBuilder:
    def __init__(self, build = All()):
        self.build_object = build

    def build(self):
        return self.build_object