# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User interaction
def main():
        temp_input = input("Enter the temperature to convert (e.g., 32): ")
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate the temperature value
        temperature = float(temp_input)

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
