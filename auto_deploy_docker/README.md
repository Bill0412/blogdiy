# Dependencies
On most of the Linux distributions, this deploy instruction will work.

## web_socket.py
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

## web_socket.js
This should be inserted at the footers by using the WordPress plugin Insert Headers and Footers.
```html
<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script>
<!-- web_socket.js should be inside here. -->
</script>
```