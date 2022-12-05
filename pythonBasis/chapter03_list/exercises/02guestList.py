guest_list = ['ironman', 'superman', 'batman']

print(guest_list[0].title() + ', come have a dinner with me.')
print(guest_list[1].title() + ', do you want a dinner with me tonight?')
print(guest_list[2].title() + ", let's go for a dinner.")

print("\nChanging Guest List, bez one of the list can't make the dinner")
print(guest_list[0].title() +" can't have a dinner with me.")
guest_list.insert(0, 'spiderman')
print(guest_list[0].title() + ', come have a dinner with me.')
print(guest_list[1].title() + ', do you want a dinner with me tonight?')
print(guest_list[2].title() + ", let's go for a dinner.")

print("\nI just found a bigger dinner table, i want invite more three guests")
guest_list.insert(0, 'Captain America')
guest_list.insert(2, 'black widow')
guest_list.append('Doctor Stange')
print(guest_list)
print(guest_list[0].title() + ', come have a dinner with me.')
print(guest_list[1].title() + ', do you want a dinner with me tonight?')
print(guest_list[2].title() + ", let's go for a dinner.")
print(guest_list[-2].title() + ', do you want a dinner with me tonight?')
print(guest_list[-1].title() + ", let's go for a dinner.")

print("\nShrinking Guest List: You just found out that your new dinner table won’t"+
" arrive in time for the dinner, and you have space for only two guests.")
removed_guest01 = guest_list.pop()
removed_guest02 = guest_list.pop()
removed_guest03 = guest_list.pop()
removed_guest04 = guest_list.pop()
removed_guest05 = guest_list.pop()
print(guest_list)
print(removed_guest01.title() + " sorry, you are out of the list.")
print(removed_guest02.title() + " sorry, you are out of the list.")
print(removed_guest03.title() + " sorry, you are out of the list.")
print(removed_guest04.title() + " sorry, you are out of the list.")
print(removed_guest05.title() + " sorry, you are out of the list.")
print(guest_list[0].title() + ", you are still in the list.")
print(guest_list[1].title() + ", you are still in the list.")

del(guest_list[0])
del[guest_list[0]]
print("After delete "+ str(guest_list)+ " still in the list")