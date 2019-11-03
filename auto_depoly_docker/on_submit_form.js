(() => {
    // document.getElementById("port").value = "hello, js";
    const form = document.querySelector("#contact-form-25");

    // if there is a server info upload form
    if(form) {
        const submit_button = form.querySelector(".contact-submit > .pushbutton-wide");
        submit_button.addEventListener("click", () => {
            console.log("submitted");
        })
    }
})();
