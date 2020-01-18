// Dependency: Jquery

(() => {
    document.addEventListener("DOMContentLoaded", () => {
        $("[type='hidden']").remove();

    });

    const socket = new WebSocket("wss://deploy.sitediy.fenghe.us:6789");
    // Connection Opened
    socket.addEventListener('open', (event) => {
        msg = {msg: 'hello'}
        socket.send(JSON.stringify(msg))
    });

    // Listen for messages
    socket.addEventListener('message', (event) => {
        console.log('Message from server ', event.data);
    });


    $("#contact-form-7").submit((event) => {
        let deploy_info = {
            blog_diy: {
                deploy: {
                    service: {
                        name: 'wordpress',
                            // default port: 80
                        port: $("#listen_port").val().length ? parseInt($("#listen_port").val()) : 80
                    },
                    target: {
                        host: $("#host").val(),
                        port: $("#port").val().length ? parseInt($("#port").val()) : 22,  // default port: 22
                        username: $("#username").val().length ? $("#username").val() : 'root',
                        password: $("#password").val()
                    }
                }
            }
        };
        socket.send(JSON.stringify(deploy_info));

        link = deploy_info.blog_diy.deploy.target.host + ':' + deploy_info.blog_diy.deploy.service.port;
        $("#contact-form-7").replaceWith(`<h4>如果您提供的服务器信息是正确的，您的WordPress网站能在10分钟内在自动完成部署。稍后您可以通过<a href="http://${link}/" target="_blank">http://${link}/</a>来配置您的网站。</h4>`);
    });

})();
