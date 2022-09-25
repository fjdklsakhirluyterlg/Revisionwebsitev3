var stack_id = 0

function addstack(id){
    const name = document.getElementById("name").value
    console.log(name)
    data = {"user_id": id, "name": name, "cards": []}
    fetch("/api/stack/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()
    ).then(data => stack_id = data.id
    ).then(() => console.log(stack_id)).catch((error) => {
        console.error('Error:', error);
    });
}

function addcardform(){
    var temp = document.getElementsByTagName("template")[0];
    var clon = temp.content.cloneNode(true);
    var div = document.getElementById("cards")
    div.append(clon)
    // document.body.appendChild(clon);
}

function addcards(){
    const zip = (a, b) => a.map((k, i) => [k, b[i]]);
    var front = document.getElementsByClassName("front")
    var back = document.getElementById("back")
    var cards = zip(front, back)
    console.log(cards)
    for (var i = 0; i < cards.length; i++){
        console.log(i)
    }
}

function cardfetch(front, back){
    data = {"id": stack_id, "front": front, "back": back}
    fetch("/api/stack/cards/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => res.json()
    ).then(obj => console.log(obj.id)).catch((error) => {
        console.error('Error:', error);
    });
}