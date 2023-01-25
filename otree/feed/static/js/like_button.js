console.log("like button ready!");

function like() {
    var attention_check = document.getElementById("like_button")
    attention_check.className="bi bi-heart-fill text-danger"
    attention_check.innerHTML="&nbsp;5&emsp;"

    var redirect_button = document.getElementById("submitButton")
    var submit_button = document.createElement("button")
    submit_button.setAttribute("type", "submit")
    submit_button.className = "btn btn-outline-dark btn-sm m-2"
    submit_button.innerHTML = "Submit"
    redirect_button.parentNode.replaceChild(submit_button, redirect_button);
}