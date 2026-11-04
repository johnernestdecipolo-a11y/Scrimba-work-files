# hourly_rate = float(input("What is your hourly rate?"))
# hours_worked = int(input("How many hours have you worked?"))

# print (type(hourly_rate))
# print (type(hours_worked))

# salary = hourly_rate * hours_worked

# print (salary)

event = input("What was the event or occasion? ")
cost = float(input("How much was it? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): "))
group_size = int(input("How many people were in your group? "))
service_charge_total = cost * service_charge / 100
grand_total = cost + service_charge_total
total_per_person = grand_total / group_size

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service charge: ${service_charge_total:.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total:.2f}")
print()
print(f"Each person must PayUp:${total_per_person:.2f}")
print()
print(type(cost))
print(type(service_charge))
print(type(group_size))