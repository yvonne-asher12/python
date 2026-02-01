BSCIT-05-0072/2024
YVONNE KARIMI

#python lists
invt={}
i = 1

while True:
 item = input(f"Enter item name {i}:")
 if item == "":
   break #it stops loop if user presses enter
 quantity = int(input(f"Enter the quantity {i}:"))
 i += 1

 #allowing user to update quantity
 invt[item] = invt.get(item,0) + quantity

print (invt)

#retrieving of items
retrieve_item = input("Enter item to retrieve:")
if retrieve_item in invt:
     print(f"{retrieve_item} quantity: {invt[retrieve_item]}")
else:
         print(f"{retrieve_item} not found in the invt")
         
#calculating the total quantity
tot_qty = sum(invt.values())
print(tot_qty)



