import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery

CLIENT_SECRET = "client_secret.json"
SCOPE = "https://www.googleapis.com/auth/blogger"
STORAGE = Storage("credentials.storage")

# Start the OAuth flow to retrieve credentials
def authorize_credentials():
    # Fetch credentials from storage
    credentials = STORAGE.get()
    # If the credentials doesn't exist in the storage location then run the flow
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, STORAGE, http=http)
    return credentials


def authorize():
    credentials = authorize_credentials()
    print(credentials)


# def get_pages_from_jobs():
#     credentials = authorize_credentials()
#     http = credentials.authorize(httplib2.Http())
#     discoveryUrl = ('https://www.googleapis.com/blogger/')
#     service = discovery.build('blogger', 'v3', http=http, discoveryServiceUrl=discoveryUrl)
#     users = service.users()
#     # Retrieve this user's profile information
#     thisuser = users.get(userId='self').execute()
#     print('This user\'s display name is: %s' % thisuser['displayName'])
#     page=service.pages()
#     onepage=page.get(blogId='2352119848425464545',pageId='6211901358272467149').execute()
#     print("this will show specific onepage", onepage)
#     cities=['united states','India','Aus','brazil']
#     for item in cities:
#         title="title for "+item
#         payload={
#             "content": "<div dir=\"ltr\" style=\"text-align: left;\" trbidi=\"on\">\nEspeciallySports is a sports news portal aims at bringing the latest sports news for the fans that cover MMA, WWE, UFC, Cricket, Football, etc&nbsp;</div>\n",
#         "title": title
#         }


def main():
    authorize()


if __name__ == "__main__":
    main()