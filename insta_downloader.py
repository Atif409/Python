import instaloader

def download_reels(profile_username, download_folder):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, profile_username)

    for post in profile.get_posts():
        if post.is_video and post.typename == 'GraphVideo':
            L.download_post(post, target=download_folder)

# Provide the Instagram profile username and download folder path
profile_username = input("Enter Instagram Profile Name: ")
download_folder = input("Enter Folder Name To Save Videos: ")

download_reels(profile_username, download_folder)