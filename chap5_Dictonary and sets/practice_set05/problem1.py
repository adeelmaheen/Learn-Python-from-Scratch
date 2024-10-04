# Write a program to create a dictionary of Urdu words with values as their English translation. Provide user with an option to look it up!
words = {
    "Monday" : "Peer",
    "Tuesday" : "Mangal",
    "Wednesday" : "Budh",
    "Thursday" : "Jumerat",
    "Friday" : "Jumma",
    "Saturday" : "Hafta",
    "Sunday" : "Itwar"
}

word = input("Enter the Day name you want to look translate : " )
user_1 = words[word]
print(user_1)