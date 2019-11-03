// Dependency: Jquery

(() => {
    document.addEventListener("DOMContentLoaded", () => {
        $("[type='hidden']").remove();

    });

    const socket = new WebSocket("wss://deploy.blogdiy.net:6789");
    // Connection Opened
    socket.addEventListener('open', (event) => {
        msg = {msg: 'hello'}
        socket.send(JSON.stringify(msg))
    });

    // Listen for messages
    socket.addEventListener('message', (event) => {
        console.log('Message from server ', event.data);
    });


    $("#contact-form-25").submit((event) => {


        socket.send({
            host: $("#host").val(),
            port: $("#port").val(),
            username: $("#username").val(),
            password: $("#password").val()
        });
    });

})();
