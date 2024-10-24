# write a program to greet all the person names stored in a list and starts with "S"

name_list = [ "Sobia", "Maha", "Zara", "Sara", "Zoha", "Sania"]

for name in name_list:
    if(name.startswith("S")):
        print(f"Hello Good Day! {name}")