function addstack(id){
    const name = document.getElementById("name").val()
    data = {"user_id": id, "name": name}
    fetch("/api/stack/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res);
    });
}