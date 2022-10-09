count = 0

id = 0

function submit(id){
    var text = document.getElementById("editor").innerHTML

    data = {"text":text, "user_id":id}

    if (count >= 1){

    fetch("/api/notes/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => id = obj.id)

    document.getElementById("editor").innerHTML = text
    count += 1
    } else {
        fetch(`/notes/edit/${id}`, {
            method : "POST",
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        }).then(res => res.json()).then(obj => id = obj.id)
    
        document.getElementById("editor").innerHTML = text
    }
}

function increase_count(){
    count += 1
}