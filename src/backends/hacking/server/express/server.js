const express = require("express")
const app = express()

var port = 5070

app.get("/", (req, res) => {
    res.send("happy new year")
})

app.post("/data", (req, res) => {
    
})

app.run()