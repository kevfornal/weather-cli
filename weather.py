import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a city name. Example: python weather.py 'London'")
        return

    city = sys.argv[1]
    print(f"Fetching weather for: {city}...")
    # Add your weather API logic here

if __name__ == "__main++":
    main()
