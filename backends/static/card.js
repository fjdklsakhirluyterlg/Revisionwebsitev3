function addstack(id){
    const name = document.getElementById("name").val()
    data = {"user_id": id, "name": name}
    fetch("/api/stack/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res);
        alert("added")
    }).catch((error) => {
        console.error('Error:', error);
    });
}

var form = document.getElementById("myForm");
function handleForm(event) { event.preventDefault(); } 
if(form){
form.addEventListener('submit', handleForm)
}