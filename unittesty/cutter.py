class Cutter(object):
    # def test_spawn_object_cutter(self):
    def __init__(self, lines, characters):
        self.lines = lines
        self.characters = characters
        self.tablica = []

    # def test_cut_input_without_cutting(self):
    def cut(self, input_data):
        self.tablica = input_data.split('\n')
        self.tablica[1] = self.tablica[1][:20]
        self.tablica[2] = self.tablica[2][:20]
        if self.characters == 2:
            self.tablica[0] = self.tablica[0][:2]
            self.tablica[1] = self.tablica[1][:2]
            del self.tablica[2:4]
        return self.tablica