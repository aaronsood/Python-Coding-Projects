temperature = int(input("What is the temperature? (Celcius)"))
rain = input("Is it raining? (Y/N)").lower()
if temperature <= 5:
    outfit =  "Very cold! Wear a heavy jacket and other garments to keep yourself warm or stay indoors with a heater going."
elif 5 <= temperature <= 10:
    outfit =  "Cold, wear a jacket to stay warm."
elif 11 <= temperature <= 20:
    outfit =  "Still may be slightly cold, but you should be fine wearing a hoodie and pants."
elif 21 <= temperature <= 25:
    outfit = "Slightly warm, wear a t-shirt and shorts"
elif 26 <= temperature <= 30:
    outfit = "It is pretty hot now, wear a t-shirt and shorts."
else:
     outfit =  "Very hot! Wear something light like a singlet or enjoy a nice cold breeze by sitting in front of the AC."

if rain == "y":
    outfit +=" Bring an umbrella as well."
elif rain == "n":
    outfit += " No need for an umbrella."
else:
    print("Invalid input.")
print(f"{outfit}")

