# Create Purchasing Information and Receipts for Lovely Loveseats
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
# price of lovely lovelyseat
l_l_price = 254.00
# description of sette
stylish_setee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
# Price of stylish setee
s_s_price = 180.50
# additional description of new item
luxury_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
# rpice of luxury lamp
luxury_lamp_price = 52.15
# Sales tax
sales_tax = 0.088

# First Customer
customer_one_total = 0
# customer one purchases
customer_one_itemization = ""
# customer purchases lovely loveseat
customer_one_total += l_l_price
# Adding to the customer purchase list
customer_one_itemization = (lovely_loveseat_description)
# customer purchases luxury lamp
customer_one_total = (customer_one_total + luxury_lamp_price)
# updating the purchase list
customer_one_itemization = (customer_one_itemization + " " + luxury_lamp_description)
# tax to be added
customer_one_tax = (customer_one_total * sales_tax)
customer_one_total = (customer_one_total + customer_one_tax)

print('Customer one items are :' + customer_one_itemization)
print('Customer one total is : ' + str(customer_one_total))