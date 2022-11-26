function checkout(user_id, objects){
    var amount = document.getElementById("amount").value
    var act = objects.slice(0, amount)
    console.log(act)
    var data = {"user_id":user_id, "objects":act}
    fetch("/api/shop/checkout/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(document.getElementById("stock").value -= amount).then(document.getElementById("amount").value = "")
}

function increment_counter(){

}

function submit_review(){
    
}