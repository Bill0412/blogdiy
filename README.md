# Blog DIY Project
Most of the demos here is likely to become a feature of my project <https://sitediy.fenghe.us>, which is a various sites startup guidance for Chinese users.

## Feature 1: Deploy WordPress to a Remote Server
1. Given the **host**, **port**, **username** and **password** of a remote server, the server creates a thread and deploy the latest WordPress Docker to a remote server and the WordPress container listens at port 80.

### Todos
1. - [x] Send the target server information to the server that is in charge of deployment
2. - [x] When this server receives the instructions (currently only deploy WordPress Docker) from <https://sitediy.fenghe.us/>, it should deploy the docker to the target remote server. A bash script should be implemented. Using git clone and executing the script to deploy.
3. - [ ] Fix: establish connection with the mysql server.
4. - [ ] When the server finishes its operation, it should the result back.

## More Features: Auto deploy more templates
Following are some of the templates that I decide to implement
- SSR
- Outline
- Hexo

## More Features
Under development.

## How to Contact Me
My Blog: <https://fenghe.us/>

## License
MIT