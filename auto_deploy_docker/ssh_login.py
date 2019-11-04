import paramiko
import asyncio


def execute_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()
    print(output)


def deploy_to(host, port, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)

    execute_command(client, "apt install docker.io")
    execute_command(client, "docker pull wordpress")
    execute_command(client, "docker run --name wp0 -p 80:80 -d wordpress")

    client.close()


host = '108.61.207.105'
port = 22
username = 'root'
password = '4%MqP7-,rQ{F4m$b'
deploy_to(host, port, username, password)
