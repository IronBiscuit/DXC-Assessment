class ReferenceTable:

    def __init__(self, c_i_dict, i_c_dict):
        self.c_i_dict = c_i_dict
        self.i_c_dict = i_c_dict
        self.table_size = len(c_i_dict)