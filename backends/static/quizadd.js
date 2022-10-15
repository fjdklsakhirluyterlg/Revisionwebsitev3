function sumbit_quiz(id){
    var name = document.getElementById("name")
    var description = document.getElementById("description")
    var user_id = id
    var categories = document.getElementById("categories").split(" ")
    data = {"user_id":user_id, "description":description, "name":name, "categories":categories}
    fetch("/api/quiz/add")

}