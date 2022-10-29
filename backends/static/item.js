function checkout(user_id, objects){
    var act = objects.slice(0, amount)
    var data = {"user_id":user_id, "objects":act}
    fetch("/api/shop/checkout/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(console.log("done"))
}