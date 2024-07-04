import random
import array

lowercase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

uppercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

specialchars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

#length input from user
Length = int(input("Enter length of password : "))

# combines all the character arrays above to form one array
COMBINED_LIST = numbers + uppercase_char + lowercase_char + specialchars

# randomly select at least one character from each character set above
random_digit = random.choice(numbers)
random_upper = random.choice(uppercase_char)
random_lower = random.choice(lowercase_char)
random_symbol = random.choice(specialchars)

# password of given length
temporarypassword = random_digit + random_upper + random_lower + random_symbol

for x in range(Length - 4):
	temporarypasswords = temporarypassword + random.choice(COMBINED_LIST)

	#using array package5

	temp_pass_list = array.array('u', temporarypassword)
	random.shuffle(temp_pass_list)

#to form a password
password = ""
for x in temp_pass_list:
		password = password + x
		
# print out password
print("THE GENERATED PASSWORD WAS :",password)