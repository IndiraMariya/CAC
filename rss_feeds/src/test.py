import base64
from urllib.request import urlopen


# List of image URLs to check
image_urls = [
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/0e377123-Palestine-protest-extra-credit.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_IN_CRIME.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/nj_cpv_plant.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/8e2c4506-a113-48a7-998e-ee0c13a8039f/d325d06a-5499-4527-b522-cd5da19dee9e/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/16717fe2-9b4e-4c03-9f44-c13ab88bce4f/835e7508-76f4-4575-a1b6-9dfeed7c2355/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/schooner_grace_bailey.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_FL_WEATHER.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_IA_GENERAL.png?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/6ce759ea-5278-4c82-96f8-06cd25c25536/78e62510-b99b-4c12-9906-7373ca36f0cf/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_MI_CRIME.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/05/1200/675/alabama-graphic.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/a4dd4258-Police.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/crime-scene.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_IN_GENERAL.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/man-with-dog.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_MO_CRIME.png?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/b2cc10cc-236a-4688-8c02-b998d93a9727/c0b7c574-28bc-4e17-9c3a-6e58a8d33469/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2022/06/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_IA_GENERAL.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/05/1200/675/ALL_CUSTOM_FS_LOCAL_NEWS_WA_GENERAL.png?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/tiktok.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/1200/675/kmsp-police-shooting-3.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/edcd92c5-baa7-40c2-a0bc-b87e7052eb76/fc7d01a2-b6db-4731-b5e0-f62f3962eee8/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/10/896/500/Kaitlin-Armstrong-split.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/e3161939-7455-400d-bf7e-2449f02a23c8/58927c2a-4238-4a95-ba96-71cb58af5de8/1280x720/match/896/500/image.jpg?ve=1&tl=1",
    "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/08/1200/675/ALL_CUSTOM"
]

for image_url in image_urls:
    try:
        # Attempt to decode the image data as base64
        with urlopen(image_url) as response:
            image_data = response.read()
            decoded_image_data = base64.b64decode(image_data)
        print("YES")
    except Exception as e:
        print(f"NO")
