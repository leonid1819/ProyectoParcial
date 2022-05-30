const msgerChat = get(".chat-area");
const msgerForm = get(".input-area");
const msgerInput = get(".msger-input");
msgerForm.addEventListener("submit", event => {
    event.preventDefault();
    const msgText = msgerInput.value;

    botResponse(msgText);
    });
function appendMessage( text) {
    //   Simple solution for small apps
    const msgHTML = `<div class="income-msg">
        <img src="{{url_for('static', filename='img/ico_boton_flot/ColmiBot5.png')}}" class="avatar" alt="">
        <span class="msg"> ${text}</span>
    </div>`;
    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
    }

function botResponse(rawText) {
    // Bot Response
    $.get("/get", { msg: rawText }).done(function (data) {
        console.log(rawText);
        console.log(data);
        const msgText = data;
        appendMessage( msgText);
    });
}


function get(selector, root = document) {
    return root.querySelector(selector);
    }