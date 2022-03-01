window.onload = function() {
    document.querySelector("#hello-button").onclick = function() {
        let name = document.querySelector("#name-input").value;
        document.querySelector("#message-p").innerHTML = "Hello " + name + "!";
        return false;
    };
}
