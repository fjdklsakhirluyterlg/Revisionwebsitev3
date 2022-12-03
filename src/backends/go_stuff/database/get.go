package main

import (
	"fmt"
	"database/sql"
	// "os"
	_ "github.com/mattn/go-sqlite3"
)

func mainx() {
	db, err := sql.Open("sqlite3", "../../database.db")
	rows, errs := db.Query("SELECT * FROM User")
    if err != nil{
		fmt.Print("error")
	}
	if errs != nil{
		fmt.Print("error")
	}
	var count int

	for rows.Next() {
		count++
	}

	rows.Close()
	fmt.Print(count)

}
