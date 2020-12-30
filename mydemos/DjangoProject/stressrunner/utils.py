# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/7/6 14:43
# @File    : utils.py
import threading

import paramiko


class ServerOpt:

    def __init__(self, host, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh.connect(hostname=host, port=22, username=username, password=password)

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        stdout = stdout.read().decode("utf8")
        stderr = stderr.read().decode("utf8")
        return {'stdout': stdout, 'stderr': stderr}

    def put_files(self, from_path, to_path):
        sftp = self.ssh.open_sftp()
        sftp.put(from_path, to_path)

    def get_files(self, from_path, to_path):
        sftp = self.ssh.open_sftp()
        sftp.get(from_path, to_path)

    def ssh_close(self):
        self.ssh.close()


class RecodeThread(threading.Thread):
    def __init__(self, funcName, *args):
        threading.Thread.__init__(self)
        self.args = args
        self.funcName = funcName
        self.exitcode = 0
        self.exception = None
        self.exc_traceback = ''

    def run(self):
        try:
            self._run()
        except Exception as e:
            self.exitcode = 1
            self.exception = e

    def _run(self):
        try:
            self.funcName(*(self.args))
        except Exception as e:
            raise e




