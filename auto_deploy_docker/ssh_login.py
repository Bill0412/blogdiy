import paramiko

def execute_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()
    print(output)


def deploy_to(host, port, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password, timeout=600)

    execute_command(client, "wget https://raw.githubusercontent.com/Bill0412/blogdiy/master/auto_deploy_docker/deploy_wordpress.sh")
    execute_command(client, "echo '\n' | nohup bash deploy_wordpress.sh &")

    client.close()


if __name__ == '__main__':
    host = '91.90.195.216'
    port = 3333
    username = 'root'
    password = 'f7bgsBE2'
    deploy_to(host, port, username, password)
