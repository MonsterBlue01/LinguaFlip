package main

import "fmt"

func main() {
	/* This is my first simple program */
    fmt.Println("Hello, World!")
	fmt.Println("Google" + "Runoob")					// concatenation of two strings

	var stockcode=123
    var enddate="2020-12-31"
    var url="Code=%d&endDate=%s"						// format string
    var target_url=fmt.Sprintf(url,stockcode,enddate)
    fmt.Println(target_url)
}

// single line comment
/*
	I am a multiline comment 
 */