cupcake_open = open("CupcakeInvoices.csv")

# for row in cupcake_open:
#     print(row)

# for types in cupcake_open:
#     types = types.rstrip('\n').split(',')
#     print(types[2])

# for types in cupcake_open:
#     types = types.rstrip('\n').split(',')
#     # print(types[2])
#     total_invoice = (int(types[3]) * float(types[4]))
#     print(types[0], types[1], "total is", total_invoice)


total = 0

for row in cupcake_open:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))

# print(total)

cupcake_open.close()


