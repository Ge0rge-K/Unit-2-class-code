'''
Name: George Koniaris
Date: 9/30/24
Description: Unit 2 Homework 1
'''

print('Problem 1'.center(20,'-'))

print("Theme One: The world was taken over by bass and it is up to robert, a 3rd generation fisherman. Only he can save the world from the bass!")
print("                                                                                                           ")
print("Theme: Two: A crew of five take on the challenge of stealing the decleration of independence from fort knox.")
print("                                                                                                             ")
print("Theme Three: Three dads all sit down on the couch to watch NFL sunday but then are transported through space and time by the couch and end up on the line of the very team they were watching.")

print("                                                                                                           ")
print("                                                                                                           ")
print("                                                                                                           ")
print("                                                                                                           ")

print('Problem 2'.center(20,'-'))

print(r"""
___________            __ ___.          .__  .__      _________                 .___                        __      __.__.__       .___ __________.__                
\_   _____/___   _____/  |\_ |__ _____  |  | |  |    /   _____/__ __  ____    __| _/____  ___.__. _____    /  \    /  \__|  |    __| _/ \______   \  | _____  ___.__.
 |    __)/  _ \ /  _ \   __\ __ \\__  \ |  | |  |    \_____  \|  |  \/    \  / __ |\__  \<   |  | \__  \   \   \/\/   /  |  |   / __ |   |     ___/  | \__  \<   |  |
 |     \(  <_> |  <_> )  | | \_\ \/ __ \|  |_|  |__  /        \  |  /   |  \/ /_/ | / __ \\___  |  / __ \_  \        /|  |  |__/ /_/ |   |    |   |  |__/ __ \\___  |
 \___  / \____/ \____/|__| |___  (____  /____/____/ /_______  /____/|___|  /\____ |(____  / ____| (____  /   \__/\  / |__|____/\____ |   |____|   |____(____  / ____|
     \/                        \/     \/                    \/           \/      \/     \/\/           \/         \/                \/                      \/\/     
""")


distance_to_seattle = 173.8

mpg = int(input("Enter your car's miles per gallon: "))
gas_price = float(input("Enter the price of gas per gallon: "))
tank_capacity = int(input("Enter your car's gas tank capacity in gallons: "))

gallons_needed = distance_to_seattle / mpg

total_cost = gallons_needed * gas_price

print(f"Total gallons needed for the trip: {gallons_needed} gallons")
print(f"Total cost to drive from Portland to Seattle: ${total_cost}")

if gallons_needed > tank_capacity:
    print("You will need to refuel during the trip.")
else:
    print("You have enough fuel capacity for the trip.")



