package main

import "fmt"

func main() {
	/* This is my first simple program */
    fmt.Println("Hello, World!")
	fmt.Println("Google" + "Duckduckgo")			    // concatenation of two strings

	var stockcode=123
    var enddate="2020-12-31"
    var url="Code=%d&endDate=%s"						// format string
    var target_url=fmt.Sprintf(url,stockcode,enddate)
    fmt.Println(target_url)

    var a string = "Google"
    fmt.Println(a)
                                                        // These are two examples of variables in Go
    var b, c int = 1, 2
    fmt.Println(b, c)

    var d int
    fmt.Println(d)
                                                        // These are two variables that are only defined and not assigned a value (the system will assign default values to them)
    var e bool
    fmt.Println(e)

    // var a *int
    // var a []int
    // var a map[string] int
    // var a chan int                                   // Some variable examples
    // var a func(string) int
    // var a error

    var i int
    var f float64
    var g bool                                          // Some variable examples
    var h string
    fmt.Printf("%v %v %v %q\n", i, f, g, h)

    // j := 1                                           // This can be used as a way of declaring variables

    var k = true
    fmt.Println(k)                                      // In this case the system automatically classifies the variable

    // var vname1, vname2, vname3 type
    // vname1, vname2, vname3 = v1, v2, v3

    // var vname1, vname2, vname3 = v1, v2, v3          // In this case the system automatically classifies the variable

    // vname1, vname2, vname3 := v1, v2, v3             // Variables appearing on the left-hand side of := should not have already been declared, otherwise a compilation error will result


    // // This way of writing the factorization keyword is generally used to declare global variables
    // var (
    //     vname1 v_type1
    //     vname2 v_type2
    // )

    const LENGTH int = 10
    const WIDTH int = 5                                 // Two examples of const variables
    var area int
    const l, m, n = 1, false, "str"                     // multiple assignment

    area = LENGTH * WIDTH
    fmt.Printf("The area is : %d", area)
    println()
    println(l, m, n)

    const (                                             // An example that use "iota" in "enumerate"
        a = iota                                        // 0
        b                                               // 1
        c                                               // 2
        d = "ha"                                        // independent value, iota += 1
        e                                               // "ha"   iota += 1
        f = 100                                         // iota +=1
        g                                               // 100  iota +=1
        h = iota                                        // 7, restore count
        i                                               // 8
    )
    fmt.Println(a, b, c, d, e, f, g, h, i)

}

// single line comment
/*
	I am a multiline comment 
 */