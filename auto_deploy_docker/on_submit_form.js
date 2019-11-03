(() => {
    let submit_button = null;

    document.addEventListener("DOMContentLoaded", () => {

        // document.getElementById("port").value = "hello, js";
        const form = document.querySelector("#contact-form-25");
        // if there is a server info upload form
        if(form) {
            submit_button = form.querySelector(".contact-submit > .pushbutton-wide");
            // console.log(form);
            console.log(submit_button);

            if(submit_button) {
               submit_button.addEventListener("click", () => {

                const fields = ['host', 'port', 'username', 'password'];
                let server_info = {};
                for(let field in fields) {
                    console.log(field);
                    server_info[field] = document.getElementById(field).value;
                }

                // the web socket
                const socket = new WebSocket("wss://deploy.blogdiy.net:6789")

                // Connection Opened
                socket.addEventListener('open', (event) => {
                    msg = {msg: 'hello, websocket'};
                    socket.send(JSON.stringify(msg))});

                // Listen for messages
                socket.addEventListener('message', (event) => {
                    console.log('Message from server ', event.data);
                });

                socket.send(JSON.stringfy(server_info));
                console.log(server_info);

            })
            }

        }
    })

})();
