import paramiko


def execute_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()
    print(output)


host = '45.146.122.60'
port = 22122
username = 'root'
password = 'md02AZX3gMB61m2oWe'

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(host, port=port, username=username, password=password)
execute_command(client, "git clone https://github.com/Bill0412/blogdiy.git")
execute_command(client, "cd blogdiy/auto_deploy_docker")
execute_command(client, "nohup python ")


client.close()