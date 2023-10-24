package main

import "fmt"
import "rsc.io/quote" //Add this first then, run go mod tidy to install the dependency.

func main() {
	fmt.Println("hello :)") //first print statement in GoLang
	fmt.Println(quote.Go())
}