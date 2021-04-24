import requests
from requests.structures import CaseInsensitiveDict
import json

BLOG_ID = "2352119848425464545"
BASE_URL = "https://www.googleapis.com/blogger/v3/blogs/"


def blog_info_by_blog_id():

    endpoint = BASE_URL + BLOG_ID
    body = {"key": "AIzaSyB3j2J2AtsKfAL7kN-kYqYfRz8LaTVCDaA"}

    resp = requests.get(endpoint, body)
    return resp.text


def blog_info_by_blog_url():

    endpoint = BASE_URL + "byurl"
    body = {
        "url": "https://alpeshjamgade.blogspot.com/",
        "key": "AIzaSyB3j2J2AtsKfAL7kN-kYqYfRz8LaTVCDaA",
    }

    resp = requests.get(endpoint, body)
    return resp.text


def blog_info_by_userid():

    # using oauth2.0
    endpoint = "https://www.googleapis.com/blogger/v3/users/self/blogs"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"
    ] = "Bearer ya29.a0AfH6SMD5Is4DETibo7RxWpOnEUFaZviwtE57DuZZxoR0H0Caw9dmy_EvPeUo6z8A5Zotj0EbmEXghkAu4zMbFFlP090u3zNSPZ-exMKcgXsS7ydYj1CVUKUmodb9Ydgbrg6XFtNal4muejtJ4c5Khg_xeRYm"

    resp = requests.get(endpoint, headers=headers)
    return resp.text


def retrieve_blog():

    endpoint = "https://www.googleapis.com/blogger/v3/blogs/2352119848425464545/posts"
    body = {"key": "AIzaSyB3j2J2AtsKfAL7kN-kYqYfRz8LaTVCDaA"}
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"
    ] = "Bearer ya29.a0AfH6SMD5Is4DETibo7RxWpOnEUFaZviwtE57DuZZxoR0H0Caw9dmy_EvPeUo6z8A5Zotj0EbmEXghkAu4zMbFFlP090u3zNSPZ-exMKcgXsS7ydYj1CVUKUmodb9Ydgbrg6XFtNal4muejtJ4c5Khg_xeRYm"

    resp = requests.get(endpoint, headers=headers)
    return resp.text


def retrieve_post():

    endpoint = "https://www.googleapis.com/blogger/v3/blogs/2352119848425464545/posts/8737980554658636576"
    body = {"key": "AIzaSyB3j2J2AtsKfAL7kN-kYqYfRz8LaTVCDaA"}
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"
    ] = "Bearer ya29.a0AfH6SMD5Is4DETibo7RxWpOnEUFaZviwtE57DuZZxoR0H0Caw9dmy_EvPeUo6z8A5Zotj0EbmEXghkAu4zMbFFlP090u3zNSPZ-exMKcgXsS7ydYj1CVUKUmodb9Ydgbrg6XFtNal4muejtJ4c5Khg_xeRYm"

    resp = requests.get(endpoint, headers=headers)
    return resp.text


def main():
    resp = retrieve_post()
    print(resp)


if __name__ == "__main__":
    main()