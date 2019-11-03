# Dependencies
On most of the Linux distributions, this deploy instruction will work.

## websocket.py
### Dependencies
```bash
$ apt-get install pip3
$ pip3 install websockets
```

### Get WSS Certificate
Please refer to [this post](https://fenghe.us/wsssecure-websockt-fix-neterr_cert_revoked/) on my blog.

### Clear the port
In case the port is occupied,
```bash
$ lsof -wni tcp:6789 
# a pid should be shown for the thread running on that port
$ kill pid
```

### Deployment
```bash
$ nohup python3 web_socket.py &
```