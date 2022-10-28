function checkout(user_id, objects, amount){
    var act = objects[amount - 1]
    var data = {"user_id":user_id, "objects":act}
    fetch("/api/shop/checkout/add", {
        method : "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    })
}