var stack_id = ""

function addstack(id){
    const name = document.getElementById("name").value
    console.log(name)
    data = {"user_id": id, "name": name, "cards": []}
    fetch("/api/stack/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => {
        ddd = res.json()
        console.log(ddd.id);
    }).catch((error) => {
        console.error('Error:', error);
    });
}

function addcardform(){
    var temp = document.getElementsByTagName("template")[0];
    var clon = temp.content.cloneNode(true);
    document.body.appendChild(clon);
}
