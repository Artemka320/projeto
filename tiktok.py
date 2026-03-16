import requests
import time

API_TOKEN = "apify_api_2EJL1MkvEWkl1Fy5FAImh5ggzUZmXW1XsfV1"

HASHTAGS = [
    "breakingnews",
    "news",
    "startup",
    "technology",
    "ai"
]

RESULTS_PER_PAGE = 20
DELAY = 3

url = f"https://api.apify.com/v2/acts/clockworks~tiktok-scraper/run-sync-get-dataset-items?token={API_TOKEN}"


def get_videos():

    data = {
        "hashtags": HASHTAGS,
        "resultsPerPage": RESULTS_PER_PAGE
    }

    response = requests.post(url, json=data)

    try:
        return response.json()
    except:
        print("❌ erro na API")
        return []


def score(video):
    views = video.get("playCount", 0)
    likes = video.get("diggCount", 0)
    return views + likes


def scan():

    print("🚀 Scanner TikTok com API Key\n")

    videos = get_videos()

    videos = sorted(videos, key=score, reverse=True)

    for v in videos:

        creator = v.get("authorMeta", {}).get("name")
        views = v.get("playCount")
        likes = v.get("diggCount")
        link = v.get("webVideoUrl")

        print("🔥 VIDEO VIRAL")
        print("━━━━━━━━━━━━━━━━")
        print("Creator:", creator)
        print("Views:", views)
        print("Likes:", likes)
        print("Link:", link)
        print()

        time.sleep(DELAY)


scan()