"""
    You're cleaning up your phone's contact list and organizing your close friends from Jos.
    Your friends list is: friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
    
    1. You made a new close friend "Kemi" and want to add her between "John" and "Mary".
    2. "Daniel" moved to Lagos and you don't talk anymore, so remove him from your close friends list.
    3. "Aisha" got married and now goes by "Aisha_M". Update her name in the list.
    4. You want to add your cousin "Zainab" at the end of the list.
    5. Create a new list with only the first 3 friends from your updated list and display it.
    6. Find out what position "Paul" is in your final friends list (remember: position counting starts from 1 for humans!).
    7. arrange your contacts in Descending Alphabetical Order using.
"""
friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]

friends.insert(4, "Kemi")
friends.remove(friends[1])

friends[0] = "Aisha_M"
friends.append("Zainab")

top_3_friends = friends[:3]

paul_position = friends.index("Paul") + 1

descending_friends = sorted(friends)[::-1]

print("Updated Friends List:", friends)
print("Top 3 Friends:", top_3_friends)
print("Position of Paul:", paul_position)
print("Descending Friends List:", descending_friends)

