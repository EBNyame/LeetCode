func isPalindrome(x int) bool {
    converted := strconv.Itoa(x)
    reversed := reverse(converted)
    if (x < 0){
        return false
    }else if (reversed == converted ){
        return true 
    }else{
        return false
    }
}

func reverse(x string) string{
    runes := [] rune(x)
    var reversedX []rune

    for i := len(x)-1; i >= 0; i--{
        reversedX = append(reversedX, runes[i])
    } 
    return string(reversedX)
}