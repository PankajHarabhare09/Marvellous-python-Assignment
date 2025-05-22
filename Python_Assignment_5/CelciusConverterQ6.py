def ConvertCelcius(cel):
    fahrenheit = 0
    fahrenheit = (cel * 9 / 5 ) + 32 
    return fahrenheit

def main():
    print("Enter the Celcius: ")
    celcius = int(input())

    fahrenheit = ConvertCelcius(celcius)
    print("Tempreture in Fahrenheit " , fahrenheit,"F")

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter the Celcius:
26
Tempreture in Fahrenheit  78.8 F
'''