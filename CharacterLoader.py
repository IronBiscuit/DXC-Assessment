class CharacterLoader:

    def __init__(self, char_file):
        self.index_char_dict = {}
        self.char_index_dict = {}
        self.load_file(char_file)

    def load_file(self, char_file):
        with open(char_file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                character = line[0]
                self.index_char_dict[i] = character
                self.char_index_dict[character] = i
        
    def get_ref_dicts(self):
        return self.index_char_dict, self.char_index_dict
        
