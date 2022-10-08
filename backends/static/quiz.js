function check_single(id){
    const awnser = document.getElementById(`inputsingle${id}`).value
    var data = {"id":id, "awnser":awnser}
    fetch("/api/quiz/check/single", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()
    ).then(obj => obj.message === "correct" ? document.getElementById(`spansingle${id}`).innerHTML = "&#x2713;": "&#10006;").then(obj => console.log(obj.message)).catch((error) => {
        console.error('Error:', error);
    })
}

function check_multi(id, question_id){
    var data = {"awnser_id":id, "question_id":question_id}
    fetch("/api/quiz/check/multiple", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(thing => thing.message === "correct" ? document.getElementById(`spanmulti${question_id}`).innerHTML = "&#x2713;": "&#10006;").then(obj => console.log(obj.message)).catch((error) => {
        console.error('Error:', error);
    })
}