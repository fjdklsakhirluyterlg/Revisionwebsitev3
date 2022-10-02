function check_single(id){
    const awnser = document.getElementById(`inputsingle${id}`).value
    var data = {"id":id, "awnser":awnser}
    fetch("/api/quiz/check/single", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()
    ).then(obj => console.log(obj.message)).catch((error) => {
        console.error('Error:', error);
    });
}