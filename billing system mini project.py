class Item:
    def __init__(self, item_Id, item_Name, item_Price):
        self.item_Id = item_Id
        self.item_Name = item_Name
        self.item_Price = item_Price


def Display(shopping_list, customer_Name, customer_ph, customer_Address):
    print("\n")
    print("\n")
    print("\n")
    print("                                         DHANU_RAGHU STORE ")
    print("_______________________________________________________________________________________________")
    print("\n")
    print(f"Name : {customer_Name} \t Phone Number : {customer_ph} \t Address : {customer_Address}")
    print("_______________________________________________________________________________________________")
    print("\n")
    total_Bill = 0
    for i in shopping_list:
        print(f"{i.item_Id} \t\t\t\t{i.item_Name} \t\t\t\t {i.item_Price}")
        total_Bill += i.item_Price
    print("_______________________________________________________________________________________________")
    print("\n")
    print(f"\t\t\t TOTAL BILL = {total_Bill}")



print("\n")
print("\n")
print("\n")
print("                                      WELL COME TO DHANU_RAGHU STORE ")
print("_________________________________________________________________________________________________ ")
print("\n")
shopping_list = []
customer_Name = input("Enter Your Name : ")
customer_ph = int(input("Enter your Phone Number : "))
customer_Address = input("Enter Your Address : ")
number_of_Items = int(input("How much Number of Items are You Want : "))
print("\n")
print("\n")



print("                                         DHANU_RAGHU STORE ")
print("__________________________________________________________________________________________________")
print("\n")
for i in range(0, number_of_Items):
    item_Id = i+1
    item_Name = input("Enter Item Name : ")
    item_Price = int(input("Enter Price : "))
    shopping_list.append(Item(item_Id, item_Name, item_Price))
Display(shopping_list, customer_Name, customer_ph, customer_Address)    
