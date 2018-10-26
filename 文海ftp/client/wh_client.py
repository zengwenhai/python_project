import optparse
import socket
import json


class FtpClient(object):
    """ftp客户端"""
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="ftp server ip_addr")
        parser.add_option("-P","--port",type="int",dest="port",help="ftp server port")
        parser.add_option("-u","--user",dest="username",help="username info")
        parser.add_option("-p","--password",dest="password",help="password info")
        self.options,self.args = parser.parse_args()
        print(self.options,self.args)
        self.argv_verification()
        self.make_connection()

    def argv_verification(self):
        """检查参数合法性"""
        if not self.options or not self.options:
            exit("must supply server and port parameters")  # 退出并打印

    def make_connection(self):
        """建立socket链接"""
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.options.server,self.options.port))

    def auth(self):
        """用户认证"""
        count = 0
        while count < 3:
            username = input("please input your username:").strip()
            if not username:
                continue
            password = input("please input your password:").strip()

            cmd = {
                'action_type':'auth',
                'username':username,
                'password':password,
            }
            self.sock.send(json.dumps(cmd).encode('utf8'))
            self.sock.recv(1024)

    def interactive(self):
        """处理与Ftpserver的所有交互"""
        if self.auth():
            pass




if __name__ =="__main__":
    ftp = FtpClient()
    ftp.interactive()  # 和用户交互


















