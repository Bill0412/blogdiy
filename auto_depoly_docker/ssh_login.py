import paramiko

host = '45.146.122.60'
port = 22122
username = 'root'
password = 'md02AZX3gMB61m2oWe'

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(host, port=port, username=username, password=password)
stdin, stdout, stderr = client.exec_command("pwd")
output = stdout.readlines()
print(output)
client.close()