import requests
from requests.structures import CaseInsensitiveDict
import json

BLOG_ID = "2352119848425464545"
BASE_URL = "https://www.googleapis.com/blogger/v3/blogs/"


def delete_post(post_id):

    endpoint = "https://www.googleapis.com/blogger/v3/blogs/2352119848425464545/posts/{post_id}".format(
        post_id=post_id
    )

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"
    ] = "Bearer ya29.a0AfH6SMD5Is4DETibo7RxWpOnEUFaZviwtE57DuZZxoR0H0Caw9dmy_EvPeUo6z8A5Zotj0EbmEXghkAu4zMbFFlP090u3zNSPZ-exMKcgXsS7ydYj1CVUKUmodb9Ydgbrg6XFtNal4muejtJ4c5Khg_xeRYm"

    resp = requests.delete(endpoint, headers=headers)
    return resp.text


def main():

    post_id = input("Enter the post_id of a post you want to delete: ")
    resp = delete_post(post_id)
    print(resp)


if __name__ == "__main__":
    main()
