# 1/
# for i in range(0, 20):
#     print(i)
#     if i == 5 or i ==10:
#         continue
#     print(i)


#2/

# for i in range(3, 30):
# if i % 3 == 0:
#     break
#     print(i)

#3/

# for i in range(3, 30):
# if i % 3 == 0:
#     continue
#     print(i)

#pass 

# for i in range(0,21):
#     pass


#     for ( i = 0; i < 10; i++){

#     }


# Function to calculate electricity bill
# def calculate_bill(units, threshold=100):
#     base_rate = 450  # ₹450 per unit
#     extra_charge = 20  # Additional ₹20 per unit above the threshold

#     if units <= threshold:
#         total_bill = units * base_rate
#     else:
#         # Calculate bill for units within threshold
#         base_bill = threshold * base_rate
#         # Calculate extra charges for units above the threshold
#         extra_units = units - threshold
#         extra_bill = extra_units * (base_rate + extra_charge)
#         total_bill = base_bill + extra_bill

#     return total_bill

# # Example usage
# units_consumed = float(input("Enter the number of units consumed: "))
# bill = calculate_bill(units_consumed)
# print(f"Total electricity bill for {units_consumed} units: ₹{bill:,.2f}")

# Function to calculate electricity bill



# def calculate_bill(units, threshold=0):
#     base_rate = 450  # ₹450 per unit
#     extra_charge = 20  # Additional ₹20 per unit above the threshold

#     if units <= threshold:
#         total_bill = units * base_rate
#     else:
#         base_bill = threshold * base_rate
#         extra_units = units - threshold
#         extra_bill = extra_units * (base_rate + extra_charge)
#         total_bill = base_bill + extra_bill

#     return total_bill

# # Example usage with a for loop
# unit_consumptions = [50, 120, 200, 90, 150]  # List of unit consumptions for different scenarios

# print("Electricity Bill Summary:")
# for i, units in enumerate(unit_consumptions, start=1):
#     bill = calculate_bill(units)
#     print(f"User {i}: {units} units -> ₹{bill:,.2f}")

# units_value = 0
# if curr_units <= 350:
#     unit_value = 10
#     print(curr_units * unit_value)
#     else:
#         unit_value = 20
#         print(curr_units * unit_value)

#      unit_value = 0
#  if curr_units <=300:
#     if curr_units <= 200:
#         if curr_units <= 100:
#             print(0)


# continue  [ 1-30    10-30]  
# for i in range (1, 11):
#     for j in range(1, 31):
#         if i == 7:
#             continue
#         print(i,j)
     
# for i in range (1, 11):
#               j = 1
#               while j <= 30:
#                 # print(i, j)
#                 # j = j + 1
#             # for j in range(1, 31):
#                 if j >= 16 and i == 7:
#                 continue
#              print(i,j)
#              j = j + i

    #  j = 1 
    #  while j <= 30:
    #     print(j)


    # for i in range (1, 11):
    #   j = 1
    #   while j <= 30:
    #     if j >= 16 and i == 7:
    #       j=j+1
    #       continue
    #     print(i,j)
    #         #  j = j + i/


# for i in range(0, 20):
#     print(i)
#      continue
#     print(i)
#     print(i)
   

#    for i in range(0, 20):
#     print(i)
#      if i == 5 or i == 10:
#         continue
#         print(i)

# for i in range(0, 20):
#      if i == 5 or i == 10:
#         print(i)
    
    for i in range(3 , 30):
        if i % 3 == 0:

            print(i)