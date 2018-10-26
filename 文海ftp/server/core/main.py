from conf import settings
import socket,json

class FTPServer(object):
    """处理与客户端所有交互的socket server"""

    def __init__(self,management_instance):
        self.management_instance = management_instance  # 组合，调用management的实例
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((settings.HOST,settings.PORT))
        self.socket.listen(settings.MAX_SOCKET_LISTEN)

    def run_forever(self):
        """启动socket server"""
        print('starting 文海ftp server on %s:%s'.center(50,'-') %(settings.HOST,settings.PORT))
        self.request,self.addr = self.socket.accept()  # 赋值为全局的变量，其它函数无需传入参数也方便调用
        print("got a new connection from %s....." %(self.addr,))
        self.handle()

    def handle(self):
        """处理与用户的所有指令交互"""
        raw_data = self.request.recv(1024)
        print('------>',raw_data)
        data = json.loads(raw_data.decode('utf8'))
        action_type = data.get('action_type')
        if action_type:
            if hasattr(self,"_%s"% action_type):
                func = getattr(self,"_%s" % action_type)
                func(data)
        else:
            print("invalid command")


    def auth(self,data):
        """处理用户认证请求"""
        print("auth",data)


