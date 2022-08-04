package main

import "fmt"

func main() {
	/* This is my first simple program */
    fmt.Println("Hello, World!")
	fmt.Println("Google" + "Duckduckgo")			                // concatenation of two strings

	var stockcode=123
    var enddate="2020-12-31"
    var url="Code=%d&endDate=%s"						            // format string
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
    // var a chan int                                               // Some variable examples
    // var a func(string) int
    // var a error

    var i int
    var f float64
    var g bool                                                      // Some variable examples
    var h string
    fmt.Printf("%v %v %v %q\n", i, f, g, h)

    // j := 1                                                       // This can be used as a way of declaring variables

    var k = true
    fmt.Println(k)                                                  // In this case the system automatically classifies the variable

    // var vname1, vname2, vname3 type
    // vname1, vname2, vname3 = v1, v2, v3

    // var vname1, vname2, vname3 = v1, v2, v3                      // In this case the system automatically classifies the variable

    // vname1, vname2, vname3 := v1, v2, v3                         // Variables appearing on the left-hand side of := should not have already been declared, otherwise a compilation error will result


    // // This way of writing the factorization keyword is generally used to declare global variables
    // var (
    //     vname1 v_type1
    //     vname2 v_type2
    // )

    const LENGTH int = 10
    const WIDTH int = 5                                             // Two examples of const variables
    var area int
    const l, m, n = 1, false, "str"                                 // multiple assignment

    area = LENGTH * WIDTH
    fmt.Printf("The area is : %d", area)
    println()
    println(l, m, n)

    const (                                                         // An example that use "iota" in "enumerate"
        o = iota                                                    // 0
        p                                                           // 1
        q                                                           // 2
        r = "ha"                                                    // independent value, iota += 1
        s                                                           // "ha"   iota += 1
        t = 100                                                     // iota +=1
        u                                                           // 100  iota +=1
        v = iota                                                    // 7, restore count
        w                                                           // 8
    )
    fmt.Println(o, p, q, r, s, t, u, v, w)

    var x int = 21
    var y int = 10
    var z int

    z = x + y                                                       // The following are examples of some operator symbols
    fmt.Printf("Line 1 - the value of z is %d\n", z )
    z = x - y
    fmt.Printf("Line 2 - the value of z is %d\n", z )
    z = x * y
    fmt.Printf("Line 3 - the value of z is %d\n", z )
    z = x / y
    fmt.Printf("Line 4 - the value of z is %d\n", z )
    z = x % y
    fmt.Printf("Line 5 - the value of z is %d\n", z )
    x++
    fmt.Printf("Line 6 - the value of z is %d\n", x )
    x = 21                                                          // For the convenience of testing, x is reassigned to 21 here
    x--
    fmt.Printf("Line 7 - the value of z is %d\n", x )

    var aa int = 21
    var ab int = 10

    if( aa == ab ) {
        fmt.Printf("Line 1 - aa is equal to ab\n" )
    } else {
        fmt.Printf("Line 1 - aa isn't equal to ab\n" )
    }
    if ( aa < ab ) {
        fmt.Printf("Line 2 - aa is smaller than ab\n" )
    } else {
        fmt.Printf("Line 2 - aa isn't smaller than ab\n" )
    } 
    
    if ( aa > ab ) {
        fmt.Printf("Line 3 - aa is greater than ab\n" )
    } else {
        fmt.Printf("Line 3 - aa isn't greater than ab\n" )
    }
    /* Lets change value of aa and ab */
    aa = 5
    ab = 20
    if ( aa <= ab ) {
        fmt.Printf("Line 4 - aa is less than or equal to ab\n" )
    }
    if ( ab >= aa ) {
        fmt.Printf("Line 5 - ab is greater than or equal to aa\n" )
    }

    var ac bool = true
    var ad bool = false
    if ( ac && ad ) {
        fmt.Printf("First line - condition is true\n" )
    }
    if ( ac || ad ) {
        fmt.Printf("Second line - condition is true\n" )
    }
    /* Modify the values of ac and ad */
    ac = false
    ad = true
    if ( ac && ad ) {
        fmt.Printf("Third line - condition is true\n" )
    } else {
        fmt.Printf("Third line - condition is false\n" )
    }
    if ( !(ac && ad) ) {
        fmt.Printf("Fourth line - condition is true\n" )
    }

    var ae uint = 60      /* 60 = 0011 1100 */  
    var af uint = 13      /* 13 = 0000 1101 */
    var ag uint = 0          

    ag = ae & af           /* 12 = 0000 1100 */ 
    fmt.Printf("Line 1 - the value of ag is %d\n", ag )

    ag = ae | af           /* 61 = 0011 1101 */
    fmt.Printf("Line 2 - the value of ag is %d\n", ag )

    ag = ae ^ af           /* 49 = 0011 0001 */
    fmt.Printf("Line 3 - the value of ag is %d\n", ag )

    ag = ae << 2          /* 240 = 1111 0000 */
    fmt.Printf("Line 4 - the value of ag is %d\n", ag )

    ag = ae >> 2          /* 15 = 0000 1111 */
    fmt.Printf("Line 5 - the value of ag is %d\n", ag )

    var ah int = 21
    var ai int

    ai =  ah
    fmt.Printf("Line 1 - = operator instance, ai value = %d\n", ai )

    ai +=  ah
    fmt.Printf("Line 2 - += operator instance, ai value = %d\n", ai )

    ai -=  ah
    fmt.Printf("Line 3 - -= operator instance, ai value = %d\n", ai )

    ai *=  ah
    fmt.Printf("Line 4 - *= operator instance, ai value = %d\n", ai )

    ai /=  ah
    fmt.Printf("Line 5 - /= operator instance, ai value = %d\n", ai )

    ai  = 200; 

    ai <<=  2
    fmt.Printf("Line 6 - <<= operator instance, ai value = %d\n", ai )

    ai >>=  2
    fmt.Printf("Line 7 - >>= operator instance, ai value = %d\n", ai )

    ai &=  2
    fmt.Printf("Line 8 - &= operator instance, ai value = %d\n", ai )

    ai ^=  2
    fmt.Printf("Line 9 - ^= operator instance, ai value = %d\n", ai )

    ai |=  2
    fmt.Printf("Line 10 - |= operator instance, ai value = %d\n", ai )

    var aj int = 4
    var ak int32
    var al float32
    var am *int

    /* operator instance */
    fmt.Printf("Line 1 - aj variable type = %T\n", aj );
    fmt.Printf("Line 2 - ak variable type = %T\n", ak );
    fmt.Printf("Line 3 - al variable type is = %T\n", al );

    /*  & and * operator examples */
    am = &aj     /* 'am' contains the address of the 'aj' variable */
    fmt.Printf("The value of aj is %d\n", aj);
    fmt.Printf("*am is %d\n", *am);

    var an int = 100;

    /* Evaluate Boolean Expressions */
    if an < 20 {
        /* If the condition is true then execute the following statement */
        fmt.Printf("an is less than 20\n" );
    } else {
        /* If the condition is false then execute the following statement */
        fmt.Printf("an is not less than 20\n" );
    }
    fmt.Printf("The value of an is: %d\n", an);

    var grade string = "B"
    var marks int = 90

    switch marks {
        case 90: grade = "A"
        case 80: grade = "B"
        case 50,60,70 : grade = "C"
        default: grade = "D"  
    }

    switch {
        case grade == "A" :
            fmt.Printf("excellent!\n" )     
        case grade == "B", grade == "C" :
            fmt.Printf("good\n" )      
        case grade == "D" :
            fmt.Printf("pass\n" )      
        case grade == "F":
            fmt.Printf("failed\n" )
        default:
            fmt.Printf("poor\n" );
    }
    fmt.Printf("Your level is %s\n", grade );

    var ao interface{}
        
    switch ap := ao.(type) {
        case nil:   
            fmt.Printf("type of ao: %T", ap)                
        case int:   
            fmt.Printf("ao is of type int")                       
        case float64:
            fmt.Printf("ao is of type float64")           
        case func(int) float64:
            fmt.Printf("ao is of type func(int)")                      
        case bool, string:
            fmt.Printf("ao is bool or string" )       
        default:
            fmt.Printf("unknown") 
    }
    switch {
    case false:
            fmt.Println("1. The case conditional statement is false")
            fallthrough
    case true:
            fmt.Println("2. The case conditional statement is true")
            fallthrough
    case false:
            fmt.Println("3. The case conditional statement is false")
            fallthrough
    case true:
            fmt.Println("4. The case conditional statement is true")
    case false:
            fmt.Println("5. The case conditional statement is false")
            fallthrough
    default:
            fmt.Println("6. Default case")
    }

    var aw, ax, ay chan int
    var az, ba int

    select {
    case az = <-aw:
        fmt.Printf("received ", az, " from aw\n")
        case ax <- ba:
        fmt.Printf("sent ", ba, " to ax\n")
        case bb, bc := (<-ay):                                      // same as: bb, bc := <-ay
        if bc {
            fmt.Printf("received ", bb, " from ay\n")
        } else {
            fmt.Printf("ay is closed\n")
        }
        default:
        fmt.Printf("no communication\n")
    }

    ap := 0
    for i := 0; i <= 10; i++ {
        ap += i                                                     // Simplest for loop example
    }
    fmt.Println(ap)

    aq := 1
    for ; aq <= 10; {
        aq += aq                                                    // A not-so-typical for loop
    }
    fmt.Println(aq)

    for aq <= 10{
        aq += aq                                                    // You can also write it like this, more like a While statement
    }
    fmt.Println(aq)

    ar := 0
    for {
        ar++                                                        // If there is no break, the loop will go on indefinitely
        break;
    }
    fmt.Println(ar)

    as := []string{"google", "runoob"}
    for i, s := range as {
        fmt.Println(i, s)
    }
                                                                    // These two are more typical for each types
    at := [6]int{1, 2, 3, 5} 
    for i, x:= range at {
        fmt.Printf("Value of x at position %d = %d\n", i, x)
    }

    au := make(map[int]float32)
    au[1] = 1.0
    au[2] = 2.0
    au[3] = 3.0
    au[4] = 4.0
    
    for key, value := range au {
        fmt.Printf("key is: %d - value is: %f\n", key, value)       // read key and value
    }

    for key := range au {
        fmt.Printf("key is: %d\n", key)                             // read key
    }

    for _, value := range au {
        fmt.Printf("value is: %f\n", value)                         // read value (Note the underscore)
    }

    fmt.Println("---- break ----")
    for i := 1; i <= 3; i++ {
        fmt.Printf("i: %d\n", i)
        for i2 := 11; i2 <= 13; i2++ {
            fmt.Printf("i2: %d\n", i2)
            break
        }
    }

    fmt.Println("---- break label ----")
    re0:
        for i := 1; i <= 3; i++ {
            fmt.Printf("i: %d\n", i)
            for i2 := 11; i2 <= 13; i2++ {
            fmt.Printf("i2: %d\n", i2)
            break re0
        }
    }

    var bd int = 10

    for bd < 20 {
        if bd == 15 {
            bd = bd + 1;
            continue;
        }
        fmt.Printf("The value of bd is: %d\n", bd);
        bd++;     
    }

    fmt.Println("---- continue ---- ")
    for i := 1; i <= 3; i++ {
        fmt.Printf("i: %d\n", i)
        for i2 := 11; i2 <= 13; i2++ {
            fmt.Printf("i2: %d\n", i2)
            continue
        }
    }

    fmt.Println("---- continue label ----")
    re:
    for i := 1; i <= 3; i++ {
        fmt.Printf("i: %d\n", i)
        for i2 := 11; i2 <= 13; i2++ {
            fmt.Printf("i2: %d\n", i2)
            continue re
        }
    }

    var a int = 10

    LOOP: for a < 20 {
        if a == 15 {
            a = a + 1
            goto LOOP
        }
        fmt.Printf("The value of a is : %d\n", a)
        a++     
    } 
}

// single line comment
/*
	I am a multiline comment 
 */