const express = require("express")
const app = express()

var port = 5070

app.get("/", (req, res) => {
    res.send("hi")
})