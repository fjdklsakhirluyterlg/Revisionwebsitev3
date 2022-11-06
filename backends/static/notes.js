var urlid = window.location.href.split("")[window.location.href.split("").length - 1]
var socket = io.connect("http://127.0.0.1:5090");

if (Number.isInteger(parseInt(urlid))){
    id = parseInt(urlid)
    count = 1
} else {
    id = 0

    count = 0
}

function submit(idx){
    var text = document.getElementById("editor").innerHTML

    var data = {"text":text, "user_id":idx}

    if (count === 0){

    const url = document.location.origin

    fetch("/api/notes/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => window.location.href = `${url}/notes/view/${obj.id}`)

    document.getElementById("editor").innerHTML = text
    count += 1
    } else {
        data.id = id
        fetch(`/notes/edit/${id}`, {
            method : "POST",
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        }).then(res => res.json()).then(obj => id = obj.id)
        socket.emit("note-change", data=data)
    
        document.getElementById("editor").innerHTML = text
        count += 1
    }

    return false;
}

socket.on("note-changed", function(message){
    text = message.text
    document.getElementById("editor").innerHTML = text
    console.log(message)
})

function increase_count(){
    count += 1
}

function edit() {

    var text = document.getElementById("editor").innerHTML

    var data = {"text":text, "id":id}

    fetch(`/notes/edit/${id}`, {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => id = obj.id)

    document.getElementById("editor").innerHTML = text
    socket.emit("note-change", data=data)
    count += 1
}

window.onload = function(){
    var editor = document.getElementById("editor")
    editor.addEventListener("change", console.log("changed"))
}

// window.onload = function(){
// var target = document.querySelector('#editor');

// var observer = new MutationObserver(function(mutations) {
//   mutations.forEach(function(mutation) {
//     console.log(mutation.type);
//   });    
// });

// var config = { attributes: true, childList: true, characterData: true };

// observer.observe(target, config);
// }

// div.addEventListener("DOMNodeInserted", function (e) {
//     e.target 
// }, false);