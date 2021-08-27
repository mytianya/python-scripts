'''
创建一个udp服务器
'''
from socketserver import BaseRequestHandler,UDPServer
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('客户端地址:',self.client_address)
        msg,sock=self.request
        print(msg)
if  __name__=='__main__':
    serv=UDPServer(('',9111),TimeHandler)
    serv.serve_forever()