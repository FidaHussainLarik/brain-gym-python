email = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

print(f"Original email: ",email)

start_indx = email.find('@')
end_indx = email.find(" ",start_indx)

new_email = email[start_indx+1 : end_indx]

print(f"New email: ",new_email)

