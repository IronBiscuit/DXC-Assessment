from ReferenceTable import ReferenceTable

class EncodeException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class Encoder(ReferenceTable):

    def __init__(self, c_i_dict, i_c_dict):
        super().__init__(c_i_dict, i_c_dict)
    
    def encode(self, plain_text, offset_char):

        if (offset_char not in self.c_i_dict):
            raise EncodeException("Unknown character in offset char")
        
        offset = self.c_i_dict[offset_char]

        encoded_str = ""

        for i in range(len(plain_text)):
            current_char = plain_text[i]

            if (current_char in self.c_i_dict):
                index = self.c_i_dict[current_char]
                index -= offset

                if (index < 0):
                    index = self.table_size + index

                current_char = self.i_c_dict[index]

            encoded_str += current_char
        
        return encoded_str
            
            
            