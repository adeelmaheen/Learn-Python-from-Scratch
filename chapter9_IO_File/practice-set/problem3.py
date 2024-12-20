# write a profram to generate multiplication tables from 2 to 20 and write it to the different files.
# place these files in a folder for a 13 years old.

def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)

# ====================================================================================================

# def generate_table(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i} \n"
#     with open(f"tables_2_20/tables_{n}.txt","w") as f:
#         f.write(table)

# for i in range(2,21):
#     generate_table(i)    