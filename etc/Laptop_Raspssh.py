import paramiko # pip install paramiko
import time
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    address = input("ServerAddress: ")
    # address = '192.168.219.104'
    username = input("UserName: ")
    # username = 'pi'
    pw = input("Password: ")
    # pw = '1234'
    ssh.connect(hostname = address, port = 22, username = username,password = pw)
    print('ssh connected')
    channel = ssh.invoke_shell()
    channel.send("pwd\n")
    time.sleep(0.5)
    output = channel.recv(65535).decode("utf-8")
    print(output, end="")
    
    while True:
        str = input()
        channel.send(str + '\n')
        time.sleep(0.5)
        output = channel.recv(65535).decode("utf-8")
        print(output, end="")
        
except Exception as err:
    print(err) # ssh connect failure message
finally:
    ssh.close()