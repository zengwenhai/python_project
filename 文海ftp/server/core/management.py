import sys
from core import main



class ManagementTool(object):
    """负责对用户输入的指令进行解析并调用相应模块处理"""
    def __init__(self,sys_argv):
        self.sys_argv = sys_argv
        print(self.sys_argv)
        self.verify_argv()

    def verify_argv(self):
        """解析并验证指令"""
        if len(self.sys_argv) < 2:  # 最少要有一个指令参数
            print("error sys_argv")
            self.help_msg()
        cmd = self.sys_argv[1]
        print(cmd)
        if not hasattr(self,cmd):
            print("invalid argument")
            self.help_msg()

    def help_msg(self):
        msg = """
        start                start FTP server,
        stop                 stop FTP server,
        restart              restart FTP server,
        createuser username  create a FTP user
        """
        exit(msg)

    def execute(self):
        """解析并执行指令"""
        cmd = self.sys_argv[1]
        func = getattr(self,cmd)
        func()


    def start(self):
        """start ftp server"""
        server = main.FTPServer(self)
        server.run_forever()

