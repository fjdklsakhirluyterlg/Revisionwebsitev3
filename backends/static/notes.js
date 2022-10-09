function submit(id){
    var text = document.getElementById("editor").innerHTML

    data = {"text":text, "user_id":id}

    fetch("/api/notes/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()
    )

}