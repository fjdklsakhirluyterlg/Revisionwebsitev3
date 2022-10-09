count = 0

id = 0

function submit(id){
    var text = document.getElementById("editor").innerHTML

    data = {"text":text, "user_id":id}

    fetch("/api/notes/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => id = obj.id)

    document.getElementById("editor").innerHTML = text
}

function increase_count(){
    count += 1
}