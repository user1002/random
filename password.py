#import package
from codecs import encode,decode


#create functions for encoding/decoding
def e_rot13(s):
    return encode(s,'rot13')

def d_rot13(s):
    return decode(s,'rot13')

def e_cp037(s):
    return encode(s,'cp037')

def d_cp037(s):
    return decode(s,'cp037')

def e_hex(s):
    return encode(s,'hex_codec')

def d_hex(s):
    return decode(s,'hex_codec')


pwd = input("enter your password: ")

e_stage1 = e_rot13(pwd) #shift
e_stage2 = e_cp037(e_stage1) #encode 
e_stage3 = e_hex(e_stage2) #encode

pwd_store = e_stage3.hex() #store hex value

pwd_pull = pwd_store

d_stage1 = d_hex(pwd_pull).decode('utf-8') #retrieve hex value and decode
d_stage2 = bytes.fromhex(d_stage1) #get hex value from byte string
d_stage3 = d_cp037(d_stage2) #decode
d_stage4 = d_rot13(d_stage3) #unshift

pwd_return = d_stage4

print(pwd)
print(pwd_store)
print(pwd_return)


# f = open("C:\\Users\\jthekkel\\Desktop\\myfile.txt", "w")
# f.write(e_stage3.hex())
# f.close()
# with open("C:\\Users\\jthekkel\\Desktop\\myfile.txt", "r") as file:
#     xyz = file.read()