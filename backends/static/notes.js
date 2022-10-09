urlid = window.location.href.split("")[window.location.href.split("").length - 1]

if (Number.isInteger(urlid)){
    id = urlid
    count = 1
} else {
    id = 0

    count = 0
}

function submit(idx){
    var text = document.getElementById("editor").innerHTML

    data = {"text":text, "user_id":idx}

    if (count < 1){

    const url = document.location.origin

    fetch("/api/notes/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => window.location.href = `${url}/notes/view/${obj.id}`)

    document.getElementById("editor").innerHTML = text
    count += 1
    } else {

        fetch(`/notes/edit/${id}`, {
            method : "POST",
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        }).then(res => res.json()).then(obj => id = obj.id)
    
        document.getElementById("editor").innerHTML = text
        count += 1
    }
}

function increase_count(){
    count += 1
}