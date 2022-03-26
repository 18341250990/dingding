# -*- coding: utf-8 -*-
"""
@Description : 
@File        : ssh_manage.py
@Project     : SYProject
@Time        : 2021/8/17 下午6:41
@Author      : dj
@Software    : PyCharm
"""
import paramiko


class SSH_Manage:
    def __init__(self):
        self.host = '10.100.1.202'
        self.port = '22'
        self.user = 'root'
        self.password = 'Everjiankang'

    def conn(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, port=self.port, username=self.user, password=self.password, timeout=5)
        return ssh

    def exec(self,sql):
        ssh = self.conn()
        try:
            ssh.exec_command(sql)
            print('执行成功')

        except Exception as e:
            print(str(e))
        finally:
            ssh.close()


if __name__ == '__main__':
    path = '/Users/files/SYProject/config'
    sq = f'sftp root@10.100.1.202; echo "Everjiankang"; put  '
    SSH_Manage().exec(sq)
