package main

import(
    "fmt"                           
    "math"  
    "C"                        
)

//export squarert
func squarert(inte float64){
    fmt.Println(math.Sqrt(inte))
}   

//export helloworld
func helloworld(){
    fmt.Println("hi")
}

func main() {
}