costmer_name = input("Enter your name: ") 
age = int(input("Enter your age: ")) 
ticket_count = int(input("Enter ticket quantity: "))
is_vip = input("Are you VIP? (yes/no): ")

if age <= 12:
    base_price  = 10.00
elif age >= 65:
    base_price = 12.00
else:
    base_price =  20.00

subtotal = base_price * ticket_count

if ticket_count >= 5:
    group_discount = subtotal * 0.10
else:
    group_discount = 0.00
if is_vip == "yes":
    vip_discount = 5.00
else:
    vip_discount = 0.00

total_discount = group_discount + vip_discount
final_total = subtotal - total_discount

print("----TICKET INVOICE----")
print("Base Ticket Price:", base_price)
print("Subtotal:", subtotal)
print("Total Saved:", total_discount) 
print("Final Total Due:", final_total)
