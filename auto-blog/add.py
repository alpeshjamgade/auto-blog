import requests
from requests.structures import CaseInsensitiveDict
import json

BLOG_ID = "2352119848425464545"
BASE_URL = "https://www.googleapis.com/blogger/v3/blogs/"


def add_post(title, content):

    endpoint = "https://www.googleapis.com/blogger/v3/blogs/2352119848425464545/posts/"

    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": title,
        "content": content,
    }

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"
    ] = "Bearer ya29.a0AfH6SMDvtro1NpGbdC4kesTv5mNZ5nTU6aTTp9VKhEBLhY7LDNcLlVx3X1P5-4DnHLLYByEX7eLlpqwkoKg7PmXRRiOdklvqt8qQQOQDmSsjCfBfK9LpdSRxcobhmbFvmY5AfcIvpmSkFWaf5aLwyeHJ2AWh"

    resp = requests.post(endpoint, headers=headers, data=json.dumps(body))
    return resp.text


def main():

    title, content = input().split()
    resp = add_post(title, content)
    print(resp)


if __name__ == "__main__":
    main()
