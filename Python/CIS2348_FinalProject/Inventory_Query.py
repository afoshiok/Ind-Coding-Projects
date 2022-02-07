#A. Favour Oshiokhale (1789715)
import datetime #For work I'm going to be doing with service dates.

inventory = input('Enter Manufacturer List:')
inventory_file = open(inventory)
inventory_contents = inventory_file.readlines()
inventory_join = ','.join(inventory_contents)
main_split = inventory_join.split('\n,')
empty_list = [] #Creates list that holds all lines
for i in main_split:
    empty_list.append(i)

new_list = [] #Creates a list for each line that will go inside empty_list
for i in empty_list:
    o = i.strip('][').split(',')
    new_list.append(o)

for i in new_list:  #Removes '\n' from list
    if '\n' in i:
        i[3] = ''

id_list =[] #Cretes list containing only ids
for i in new_list:
    id_list.append(i[0])

values_list = [] #Creates list for values
for i in new_list:
    values_list.append(i[1:3+1])

manufacturer_dict = dict(zip(id_list,values_list)) #Turns both lists to dictionary


price = input('Enter Price List:') #Imports the prices
price_file = open(price)
price_contents = price_file.readlines()
price_join = ','.join(price_contents)
price_split = price_join.split('\n')
price_split.remove('')
empty_price_list = []
for i in price_split:
    empty_price_list.append(i)

price_list = [] #List all prices will be in
for i in empty_price_list:
    p = i.strip('][').split(',')
    price_list.append(p)
for i in price_list:
    if '' in i:
        i.remove('') #Removes extra whitespace from price lists

prices_ids = []
for i in price_list:
    prices_ids.append(i[0])
prices = []
for i in price_list:
    prices.append(i[1])

prices_dict = dict(zip(prices_ids, prices)) #Turns both lists to a dictionary

service_dates = input('Enter Service Dates List:') #Imports the service dates
service_file = open(service_dates)
service_contents = service_file.readlines()
service_join = ','.join(service_contents)
service_split = service_join.split('\n')
service_split.remove('')
empty_service_list = [] #Service dates and id lists will go here
for i in service_split:
    empty_service_list.append(i)

service_list = []
for i in empty_service_list:
    s = i.strip('][').split(',') #Removes whitespaces from service_list
    service_list.append(s)
for i in service_list:
    if '' in i:
        i.remove('')

service_ids = []
for i in service_list:
    service_ids.append(i[0])
service_dates = []
for i in service_list:
    service_dates.append(i[1])

service_dict = dict(zip(service_ids,service_dates)) #Turns both list to dictionary

manu_sort = sorted(manufacturer_dict.values())
manu_sorted = {}

manu_key_sort = dict(sorted(manufacturer_dict.items()))

for i in manu_sort:      #Sorts dictionary in alphabetical order by manufacturer
    for key in manufacturer_dict.keys():
        if manufacturer_dict[key] == i:
            manu_sorted[key] = manufacturer_dict[key]

manu_keys = list(manu_sorted.keys())
manu_vals = list(manu_sorted.values())

prices_keys = list(prices_dict.keys())

full_inv = open('Full_Inventory.csv','w')

for key,value in manu_sorted.items(): #Prints values in Full_Inventory.csv
    if key in prices_dict and service_dict:
        full_inv.write('{},{},{},{},{},{}\n'.format(key,value[0],value[1],prices_dict[key],service_dict[key],value[2]))
full_inv.close()

laptop_inv = open('LaptopInventory.csv','w')
phone_inv = open('PhoneInventory.csv','w')
tower_inv = open('TowerInventory.csv','w')

for key,value in manu_key_sort.items(): #Prints values in laptop inventory
    if value[1] == 'laptop':
        laptop_inv.write('{},{},{},{},{}\n'.format(key,value[0],prices_dict[key],service_dict[key],value[2]))
laptop_inv.close()

for key,value in manu_key_sort.items(): #Prints values in phone inventory
    if value[1] == 'phone':
        phone_inv.write('{},{},{},{},{}\n'.format(key,value[0],prices_dict[key],service_dict[key],value[2]))
phone_inv.close()

for key,value in manu_key_sort.items(): #Prints values in tower inventory
    if value[1] == 'tower':
        tower_inv.write('{},{},{},{},{}\n'.format(key,value[0],prices_dict[key],service_dict[key],value[2]))
tower_inv.close()

dates_list = list(service_dict.items())

l = len(dates_list) #Suppose to sort the dates
for i in range(l-1):
    for k in range(i+1,l):
        if dates_list[i][1]>dates_list[k][1]:
            b = dates_list[i]
            dates_list[i]=dates_list[k]
            dates_list[k]=b
dates_sorted = dict(dates_list) #I couldn't get it to sort by date :(
past_service = open('PastServiceDateInventory.csv', 'w')
today = datetime.date.today()
today_str = today.strftime('%m/%d/%Y')

for key, value in (dates_sorted.items()):
    if value < today_str:
        past_service.write('{},{},{},{},{},{}\n'.format(key, manufacturer_dict[key][0], manufacturer_dict[key][1], prices_dict[key],value, manufacturer_dict[key][2]))
past_service.close()

prices_sorted ={}
sorted_prices = sorted(prices_dict, key=prices_dict.get)
for w in sorted_prices:
    prices_sorted[w]=prices_dict[w] #Doesn't sort by value correctly either :(

damage_inv = open('DamagedInventory.csv','w')
for key, value in manufacturer_dict.items():
    if value[2] == 'damaged':
        damage_inv.write('{},{},{},{},{}'.format(key,value[0],value[1],prices_dict[key],service_dict[key]))
damage_inv.close()

# -------------------------------------------------------------------------- Part 2 Below.

full_inv_open = open('Full_Inventory.csv')
full_inv_contents = full_inv_open.readlines()
full_inv_join = ','.join(full_inv_contents)
full_inv_split = full_inv_join.split('\n') #Turns contents into 1 large list.
full_inv_split.remove('') #Removes empty list element.
m_full_inv = [] # 'main' list I will work with throughout this part of the project.
for i in full_inv_split:    #Creates list with in list for full inventory
    f = i.strip('][').split(',')
    m_full_inv.append(f)

for i in m_full_inv:
    if i[0] == '' in i:
        i.remove('') #Removes extra whitespace

full_inv_ids = []
for id in m_full_inv:
    full_inv_ids.append(id[0]) #Puts ids into its own list
full_inv_vals = []
for val in m_full_inv:
    full_inv_vals.append(val[1:5+1])#Puts values into its own list

full_inv_dict = dict(zip(full_inv_ids,full_inv_vals)) # Creates a dictionary for the full inventory

#Now that we have our inventory in dictionary let's work move on to querying!
user_input = input('Enter Manufacturer and Type (case sensitive):')
while user_input != 'q':
    for key,value in full_inv_dict.items():
        global safeguard #Allows safeguard to be counted outside if statements.
        if value[0] in user_input and value[1] in user_input and value[4] != 'damaged' and value[3] > today_str:
            if value[4] != 'damaged' and value[3] > today_str:
                safeguard = 0
                pass
            print('Your item is: {} {} {} ${}'.format(key,value[0],value[1],value[2]))
            value_exist = True
            safeguard = 0 + int(value[2])   # Stops the program from printing "No such item in inventory" eventhough it's True.
        elif value[0] not in user_input and value[1] not in user_input:  #Added value[4] condition so it won't print damaged product
            if True:
                value_exist = False
            else:
                value_exist = True

    if value_exist == False:
        if safeguard > 0:
            pass
        else:
            print('No such item in inventory')  # FIXME: Even if the items are in the user_input it still prints (FIXED - 12/5/21 @ 11:21pm)
            value_exist = True
    else:
        pass
    safeguard = 0
    if value_exist == False:  # This triggers the similar item recomendations FIXME: Does print this all the time (FIXED - 12/6/21 @ 1:49pm, I don't know why it works with '==False')
        print('---You may, also, consider:---')
        for key,value in full_inv_dict.items():
            if value[1] in user_input and value[0] not in user_input:
                print('{} {} {} ${}'.format(key, value[0], value[1], value[2]))
        pass

    user_input = input('Enter Manufacturer and Type:')

#FIXME: ...there's nothing here, but I do have joke. What did the Python say when he came out of his shell? print("Hello world!")| Project Completed: 12/6/21 @ 2:08