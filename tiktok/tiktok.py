import asyncio
from TikTokApi import TikTokApi
import time

# hashtags que queremos monitorizar
HASHTAGS = [
    # noticias
    "breakingnews",
    "news",
    "noticias",
    "worldnews",
    "ultimahora",

    # startups
    "startup",
    "startuplife",
    "startupfounder",
    "startupbusiness",

    # empreendedorismo
    "entrepreneur",
    "entrepreneurship",
    "business",
    "sidehustle",

    # tecnologia
    "tech",
    "technology",
    "ai",
    "programming",
    "coding",
    "innovation"
]

VIDEOS_PER_HASHTAG = 5
DELAY_BETWEEN_VIDEOS = 3


async def scan():

    print("\n🌍 =======================================")
    print("🚀  SCANNER DE TENDÊNCIAS DO TIKTOK")
    print("📰  Notícias | Startups | Tech")
    print("🌍 =======================================\n")

    async with TikTokApi() as api:

        await api.create_sessions(num_sessions=1)

        videos = []

        for tag in HASHTAGS:

            print(f"🔎 A procurar vídeos para #{tag}\n")

            async for video in api.hashtag(name=tag).videos(count=VIDEOS_PER_HASHTAG):

                data = video.as_dict

                stats = data.get("stats", {})
                author = data.get("author", {})

                videos.append({
                    "creator": author.get("uniqueId"),
                    "likes": stats.get("diggCount"),
                    "views": stats.get("playCount"),
                    "link": f"https://www.tiktok.com/@{author.get('uniqueId')}/video/{data.get('id')}"
                })

        # ordenar por popularidade
        videos.sort(key=lambda x: (x["views"] + x["likes"]), reverse=True)

        for v in videos:

            print("🔥 VIDEO POPULAR DETECTADO")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"👤 Criador: {v['creator']}")
            print(f"❤️ Likes: {v['likes']}")
            print(f"👀 Views: {v['views']}")
            print(f"🔗 Link: {v['link']}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

            time.sleep(DELAY_BETWEEN_VIDEOS)


asyncio.run(scan())