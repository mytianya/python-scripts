'''
16进制字符串与字符串编码
'''
import binascii
def str_to_hexstr(string):
    str_bin=string.encode('utf-8')
    return binascii.hexlify(str_bin).decode('utf-8')
def hexstr_to_str(hex_str):
    hex=hex_str.encode('utf-8')
    str_bin=binascii.unhexlify(hex)
    return str_bin.decode('utf-8')
def main():
    print(str_to_hexstr('中国'))
    print(hexstr_to_str('e4b8ade59bbd'))
if __name__=='__main__':
    main()