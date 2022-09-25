function addstack(id){
    const name = document.getElementById("name").value
    console.log(name)
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
function handleForm(event) { event.preventDefault(); addstack(1); alert("called handleform") } 
if(form){
form.addEventListener('submit', handleForm)
}