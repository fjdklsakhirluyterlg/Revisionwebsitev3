package main

import(
    "fmt"                           
    "math"  
    "C"                        
)
func squarert(inte float64){
    fmt.Println(math.Sqrt(inte))
}   

func main() {
    fmt.Println("Hello, World!")
    var x float64 = 32.0
    squarert(x)
}