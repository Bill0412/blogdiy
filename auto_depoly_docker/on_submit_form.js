(() => {
    let submit_button = null;
    let count = 0;
    document.addEventListener("DOMContentLoaded", () => {

        // document.getElementById("port").value = "hello, js";
        const form = document.querySelector("#contact-form-25");
        // if there is a server info upload form
        if(form) {
            submit_button = form.querySelector(".contact-submit > .pushbutton-wide");
            console.log(form);
            console.log(submit_button);

            if(submit_button) {
               submit_button.addEventListener("click", () => {

                const fields = ['host', 'port', 'username', 'password'];
                let server = {};
                for(let field in fields) {
                    console.log(field);
                    server[field] = document.getElementById(field).value;
                }
               console.log(server);

            })
            }

        }
    })

})();
