package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
	"encoding/json"
)

const (
	connHost = "localhost"
	connPort = "8980"
	connType = "tcp"
)

func main() {
	type messe struct{
		username string
		message string 
	}

	fmt.Println("Connecting to", connType, "server", connHost+":"+connPort)
	conn, err := net.Dial(connType, connHost+":"+connPort)
	if err != nil {
		fmt.Println("Error connecting:", err.Error())
		os.Exit(1)
	}

	reader := bufio.NewReader(os.Stdin)

	for {

		fmt.Print("Text to send: ")

		input, _ := reader.ReadString('\n')
		fmt.Print("User name")
		user, _ := reader.ReadString('\n')
		js := &messe{user, input}
		out, err := json.Marshal(js)
		if err != nil {
			panic (err)
		}
		conn.Write([]byte(string(out)))

		message, _ := bufio.NewReader(conn).ReadString('\n')

		log.Print("Server relay: " + message)
	}
}