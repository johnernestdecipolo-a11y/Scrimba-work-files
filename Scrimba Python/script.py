# code = "FLASH50"

# promo_code = input("Enter the promo code: ")
# print(code == promo_code)
# print(code != promo_code) 


unread_message = 0
age = 25
cart_total = 45
tickets_left = 8

print(f"Has unread messages (more than 0): {unread_message > 0}")
print(f"Old enough to rent a car (25 or older): {age >= 25}")
print(f"Under the $50 free-shipping minimum: {cart_total < 50}")
print(f"Sold out(0 or fewer tickets left): {tickets_left <= 0}")