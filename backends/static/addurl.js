function submit(user_id){
    var actual = document.getElementById("url").innerHTML
    var data = {"actual":actual, "user_id":user_id}
    fetch("/api/urls/shortner/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    })
}