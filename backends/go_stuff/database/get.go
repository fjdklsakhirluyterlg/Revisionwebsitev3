package main

import (
	"fmt"
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3", "../../database.db")
	rows, err := db.Query("SELECT * FROM User")
    
	var count int

	for rows.Next() {
		count++
	}

	rows.Close()
	fmt.Print(count)

}

func checkErr(err error) {
	panic("unimplemented")
}
