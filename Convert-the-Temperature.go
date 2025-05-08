
func convertTemperature(celsius float64) []float64 {
    var (
            Kelvin float64
            Fahrenheit float64
        )
    var ans [] float64
    
    Kelvin = celsius + 273.15
    Fahrenheit = celsius * 1.80 + 32.00
    ans = append(ans, Kelvin,Fahrenheit)

    return ans

}