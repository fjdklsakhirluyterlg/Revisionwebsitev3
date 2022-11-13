package main

import (
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3", "../../database.db")
	checkErr(err)
	rows, err := db.Query("SELECT * FROM User")
	checkErr(err)
    
	var count int

	for rows.Next() {
		count += 1
	}

	fmt.Print(count)

}

func checkErr(err error) {
	panic("unimplemented")
}
