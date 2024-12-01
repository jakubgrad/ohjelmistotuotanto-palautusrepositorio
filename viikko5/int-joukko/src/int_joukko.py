


class IntJoukko:
    def _luo_lista(self, size):
        return [0] * size
    
    def __init__(self, capacity=5, growth_increment=5):    
        self.capacity = capacity
        self.growth_increment = growth_increment
        self.lqueue = self._luo_lista(self.capacity)
        self.number_of_elements = 0

    def kuuluu(self, n):
        return True if n in self.lqueue else False

    def resize(self):
        new_lqueue = self._luo_lista(self.number_of_elements + self.growth_increment)        
        self.kopioi_lista(self.lqueue, new_lqueue)
        self.lqueue = new_lqueue        

    def lisaa(self, number_to_be_added):
        if self.kuuluu(number_to_be_added):
            return False
        
        self.lqueue[self.number_of_elements] = number_to_be_added
        self.number_of_elements = self.number_of_elements + 1

        if self.number_of_elements == len(self.lqueue):
            self.resize()    

    def poista(self, number_to_be_removed):
        if number_to_be_removed not in self.lqueue:
            return False
        self.lqueue = list(filter(lambda x: x != number_to_be_removed, self.lqueue))
        self.number_of_elements = self.number_of_elements - 1

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.number_of_elements

    def to_int_list(self):
        return self.lqueue[0:self.number_of_elements]

    @staticmethod
    def yhdiste(a, b):
        helper_set = IntJoukko()
        for element in a.to_int_list() + b.to_int_list():
            helper_set.lisaa(element)
        return helper_set

    @staticmethod
    def leikkaus(a, b):
        helper_set = IntJoukko()    
        for i in filter(lambda x: x in b.lqueue, a.lqueue):
            helper_set.lisaa(i)
        return helper_set

    @staticmethod
    def erotus(a, b):
        helper_set = IntJoukko()
        for i in filter(lambda x: x not in b.lqueue, a.lqueue):
            helper_set.lisaa(i)
        return helper_set

    def __str__(self):
        elements = [str(self.lqueue[i]) for i in range(self.number_of_elements)]
        return "{" + ", ".join(elements) + "}"