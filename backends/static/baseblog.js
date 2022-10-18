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

async function add_bookmark(user_id, blog_id){
    try{
    var note = document.getElementById("note").value
    var data = {"user_id":user_id, "blog_id":blog_id, "note":note}

    const response = await fetch("/api/blog/bookmark/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    })

    if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
    }
  
    const result = await response.json();
    return result;
    } catch (err) {
        console.log(err);
    }
}