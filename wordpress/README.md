This is the wordpress docker with mysql composer.

## CLI

### Prerequisites
```console
$ docker swarm init
```

### Deploy
```console
$ env WP_PORT=80 docker stack deploy -c stack.yml wp
```
- `wp` is the app instance name, you can replace it with you own name.
- `WP_PORT` is the port to which you want your docker service map on your server.

### Remove the service
```console
$ docker stack rm wp
```

### List the services
```console
$ docker service ls
```

## References
1. This part is based on <https://hub.docker.com/_/wordpress>
2. Set Environment Variables: <https://github.com/docker/cli/issues/939>