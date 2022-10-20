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



//export hello
func hello(namePtr *C.char) string {
    name := C.GoString(namePtr)
    helloWorld := fmt.Sprintf("%s hello", name)
    return helloWorld
}

func main() {
}