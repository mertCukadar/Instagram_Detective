import instaloader

# Get instance
L = instaloader.Instaloader()

# Login or load session
USERNAME = 'username' # input("Username: ")
PASSWORD =   "PASSWORD" # input("Password: ")




# Login
L.login(USERNAME, PASSWORD)


RECON_USERNAME = 'ogulcanfidann'

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, RECON_USERNAME)
text_storage = f"{RECON_USERNAME} falowees: \n"


# Print list of followees
for followee in profile.get_followees():
    text_storage += followee.username + "\n"



f = open(f"{RECON_USERNAME}_followees.txt", "x")
f.write(text_storage)
f.close