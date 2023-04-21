import instaloader

class Instaloader_Class:
    def __init__(self):
        self.L = instaloader.Instaloader()

    def login(self, username, password):
        self.L.login(username, password)

    def download(self, RECON_USERNAME):
        self.L.download_profile(RECON_USERNAME, profile_pic_only=True)
        
    def collect_followees(self, username , password , RECON_USERNAME):

        self.login(username, password)

        profile = instaloader.Profile.from_username(self.L.context, username)
        text_storage = f"{RECON_USERNAME} falowees: \n"
        for followee in profile.get_followees():
            text_storage += followee.username + "\n"

        f = open(f"{RECON_USERNAME}/{RECON_USERNAME}_followees.txt", "x")
        f.write(text_storage)
        f.close
    
