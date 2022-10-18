function follow_user(current, follow){
    data = {"current_user":current, "followed":follow}

    fetch("/follow/user", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => document.getElementById("follow").innerHTML = obj.message)
}