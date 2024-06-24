# Third party APIs
class TwitterAPI:
    def get_tweets(self):
        print("Fetching tweets from Twitter")
        stat = {"tweet": "Hello Twitter!", "likes": 10, "date": "2022-01-01"}
        return stat

class FacebookAPI:
    def get_posts(self):
        print("Fetching posts from Facebook")
        stat = {"post": "Hello Facebook!", "reactions": 5, "date": "2022-01-02"}
        return stat

class InstagramAPI:
    def get_photos(self):
        print("Fetching photos from Instagram")
        stat = {"photo": "Hello Instagram!", "likes": 15, "date": "2022-01-03"}
        return stat

# Adapter & Concrete Adapters
class SocialMediaAdapter:
    def fetch_posts(self):  # third party API와 기능 연계
        raise NotImplementedError("Subclasses must implement fetch_posts method")

class TwitterAdapter(SocialMediaAdapter):
    def __init__(self, twitter_api):
        self.twitter = twitter_api

    def fetch_posts(self):
        return self.twitter.get_tweets()

class FacebookAdapter(SocialMediaAdapter):
    def __init__(self, facebook_api):
        self.facebook = facebook_api

    def fetch_posts(self):
        return self.facebook.get_posts()

class InstagramAdapter(SocialMediaAdapter):
    def __init__(self, instagram_api):
        self.instagram = instagram_api

    def fetch_posts(self):
        return self.instagram.get_photos()

# client
def main():
    # 인자를 사용하여 각 API의 인스턴스를 생성하고 이를 어댑터에 전달
    twitter_api = TwitterAPI()
    facebook_api = FacebookAPI()
    instagram_api = InstagramAPI()

    twitter = TwitterAdapter(twitter_api)
    facebook = FacebookAdapter(facebook_api)
    instagram = InstagramAdapter(instagram_api)

    for adapter in [twitter, facebook, instagram]:
        posts = adapter.fetch_posts()
        print(posts)

if __name__ == "__main__":
    main()
