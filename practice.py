#inputs
customer_name = input("Enter your name -->  ")
order_number = int(input("Your order number -->  "))
order_total = float(input("Your order total -->  "))
is_student = bool(input("Are you a student? (Press Enter if not) -->  "))
is_weekend = bool(input("Is it weekend? (Press Enter if not) -->  "))
has_coupon = bool(input("Do you have a coupon? (Press Enter if not) -->  "))
is_member = bool(input("Are you a member? (Press Enter if not) -->  "))
is_delivery = bool(input("Is it for delivery? (Press Enter if not) -->  "))

#calculations
delivery_fee = 50.00

if order_total >= 1000 and has_coupon == True:
    total = 0.00
    print("Expected:", total)
elif order_total >= 1500:
    total = order_total + delivery_fee - 150.00
    print("Expected:", total)
elif is_member == True and is_weekend == True:
    total = order_total * 0.80 + delivery_fee
    print("Expected:", total)
elif is_student == True or has_coupon == True:
    total = order_total * 0.90 + delivery_fee
    print("Expected:", total)
elif is_weekend == True:
    total = order_total + delivery_fee + 30.0
    print("Expected:", total)
else:
    total = order_total + delivery_fee
    print("Expected:", total)

print(customer_name, "/", order_number, "/", total)    


