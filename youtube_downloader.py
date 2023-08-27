from pytube import YouTube

def download_video(video_url, output_path='.'):
    try:
        # Create a YouTube object
        youtube = YouTube(video_url)
        
        # Get the highest resolution stream available
        video_stream = youtube.streams.get_highest_resolution()
        
        # Download the video
        video_stream.download(output_path)
        
        print("Download complete!")
    
    except Exception as e:
        print("An error occurred:", str(e))

def get_video_quality_links(video_url):
    try:
        # Create a YouTube object
        youtube = YouTube(video_url)
        
        # Get available streams (different quality options)
        streams = youtube.streams.all()
        
        # Extract quality and link information
        quality_links = [(stream.resolution, stream.url) for stream in streams if stream.resolution is not None]
        
        return quality_links
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Provide the YouTube video link and download location
video_url = "https://www.youtube.com/watch?v=TgnOhl2eoKk"
output_folder = "downloaded_videos"

# download_video(video_url, output_folder)
print(get_video_quality_links(video_url))
