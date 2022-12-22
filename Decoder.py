from ReferenceTable import ReferenceTable

class DecodeException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class Decoder(ReferenceTable):

    def __init__(self, c_i_dict, i_c_dict):
        super().__init__(c_i_dict, i_c_dict)
    
    def decode(self, plain_text, offset_char):

        if (offset_char not in self.c_i_dict):
            raise DecodeException("Unknown character in offset char")
        
        offset = self.c_i_dict[offset_char]

        decoded_str = ""

        for i in range(len(plain_text)):
            current_char = plain_text[i]

            if (current_char in self.c_i_dict):
                index = self.c_i_dict[current_char]
                index += offset

                if (index >= self.table_size):
                    index = index - self.table_size

                current_char = self.i_c_dict[index]

            decoded_str += current_char
        
        return decoded_str