# Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = 'reasons_like_programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("The reasons that why you like programming: \n")
    print("The reasons that why you like programming(enter q to quit): ")
    count = 1
    while True:
        reasons = input("Reason " + str(count) + ": ")
        if reasons == 'q':
            break
        else:
            file_object.write(str(count) + ":" + reasons + ".\n")
            count += 1