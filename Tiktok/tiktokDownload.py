import requests
import json
import os

def get_tiktok_videos(tiktok_id):
    """
    Downloads all the videos from the given TikTok profile ID.

    Args:
        tiktok_id (str): The TikTok profile ID.

    Returns:
        list: A list of the paths to the downloaded video files.
    """

    base_url = "https://www.tiktok.com/node/share/user/{}"
    first_url = base_url.format(tiktok_id)
    
    videos = []
    has_more = True
    while has_more:
        resp = requests.get(first_url)
        data = json.loads(resp.content)
        
        for video in data["data"]["itemList"]:
            video_url = video["video"]["downloadAddr"]
            video_filename = f"{tiktok_id}_{video['itemInfos']['id']}.mp4"
            videos.append(video_filename)

            with open(video_filename, "wb") as f:
                video_resp = requests.get(video_url, stream=True)
                for chunk in video_resp.iter_content(chunk_size=1024):
                    f.write(chunk)
        
        if data["data"]["hasMore"]:
            cursor = data["data"]["cursor"]
            first_url = base_url.format(f"{tiktok_id}?cursor={cursor}")
        else:
            has_more = False

    return videos

if __name__ == "__main__":
    tiktok_id = "senex_7"  # Replace with the TikTok profile ID
    videos = get_tiktok_videos(tiktok_id)
    print(f"Downloaded {len(videos)} TikTok videos from profile ID {tiktok_id}")
