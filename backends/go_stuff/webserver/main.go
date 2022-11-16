package main

import (
	"net/http";
	"fmt";
	"log"
)

const (
	Host = "localhost"
	Port = "8090"
)

func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is a Simple HTTP Web Server!")
}

func main() {
	http.HandleFunc("/", home)
	err := http.ListenAndServe(Host+":"+Port, nil)
	if err != nil {
		log.Fatal("Error Starting the HTTP Server : ", err)
		return
	}
}
