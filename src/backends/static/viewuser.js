function follow_user(current, follow){
    data = {"current_user":current, "followed":follow}

    fetch("/follow/user", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(window.location.reload())
}

function unfollow_user(current, follow){
    data = {"current_user":current, "followed":follow}

    fetch("/unfollow/user", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(window.location.reload())
}