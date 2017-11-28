# -*- coding: utf-8 -*-


#from utils import *

u_str = '2014number中英文数字文转'

#print(to_hex(u_str))
#print(from_hex_to_binary(6, 4))
#h = '111'
#8(int(h, 2))
def from_num_to_binary(key, lens):
   # import pdb
   # pdb.set_trace()
    out_put = ""
    for i in range(lens):
        out_put = str(key >> i & 1) + out_put
    return out_put
print(from_num_to_binary(2, 4))
