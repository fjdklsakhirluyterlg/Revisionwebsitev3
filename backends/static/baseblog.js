function change_state(id){

    const btn = document.getElementById(`id`);
    btn.addEventListener('click', () => {
    const form = document.getElementById('form');

    if (form.style.display === 'none') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
    });

}

function add_bookmark(user_id, blog_id){
    var note = document.getElementById("note").value
    var data = {"user_id":user_id, "blog_id":blog_id, "note":note}

    fetch("/api/blog/bookmark/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()).then(obj => console.log(obj.id))
}