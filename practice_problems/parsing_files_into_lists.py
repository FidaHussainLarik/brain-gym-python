



try:
    file_handle = open("C:/Future_Computer_Scientist/1_AI_Engineering/5_Repositories/brain-gym-python/data/mbox-short.txt")

    # We add '../data/' to the filename to access it from the /exercises folder
    # file_handle = open('../data/' + 'mbox-short.txt')
except FileNotFoundError:
    print(f"File 'mbox-short.txt' not found in the data folder.")
    quit()

# for line in file_handle:
#     line = line.rstrip()
#     if not line.startswith('From'):
#         continue
#     words = line.split()
#     # date and time
#     if len(words) > 2:
#         print(words[2]) 


# Extracting emails
# Reset file pointer to the beginning
file_handle.seek(0)


for line in file_handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    email = words[1]
    peices_of_email = email.split('@')
    print(peices_of_email[1])
