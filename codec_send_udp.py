'''
测试不通编码的中文发送的UDP端口
'''
import socket
def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #data1=bytes('中国',encoding='utf8')
    udp_socket.sendto('中国'.encode('utf-8'),('localhost',9111))
if __name__=='__main__':
    main()