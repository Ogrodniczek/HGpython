class Duck(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, how_many=1):
        self.quack(how_many)
    def quack(self, how_many=1):
        print('Quack!' * how_many)

class DuckHerd(object):
    def __init__(self, *kaczki):
        self.kaczki = list(kaczki)
        self.kaczki = kaczki
    def __iadd__(self, kaczki):
        self.kaczki.append(list(kaczki))
        return self
    def __len__(self):
        return len(self.kaczki)

    def __getitem__(self, imie):
        for kaczka in self.kaczki:
            if kaczka.name == imie:
                return kaczka

