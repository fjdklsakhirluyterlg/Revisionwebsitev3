var quiz_id = 0;
var multi_id = 0

function sumbit_quiz(id){
    var name = document.getElementById("name")
    var description = document.getElementById("description")
    var user_id = id
    var categories = document.getElementById("categories").split(" ")
    data = {"user_id":user_id, "description":description, "name":name, "category":categories}
    fetch("/api/quiz/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(data => quiz_id = data.id)
}

function add_multi(){
    multi_id += 1
    var multi = document.getElementById("multi")
    var clone = multi.content.cloneNode(true);
    clone.querySelector(".main").id = multi_id
    var div = document.getElementById("main")
    div.append(clone)
}

