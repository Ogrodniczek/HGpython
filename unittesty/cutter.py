class Cutter(object):
    # def test_spawn_object_cutter(self):
    def __init__(self, lines, characters):
        self.lines = lines
        self.characters = characters
        self.tablica = []

    # def test_cut_input_without_cutting(self):
    def cut(self, input_data):
        self.tablica = input_data.split('\n')
        return self.tablica