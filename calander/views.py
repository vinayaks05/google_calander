import os
import google_apis_oauth

from django.shortcuts import HttpResponseRedirect

# The url where the google oauth should redirect
# after a successful login.
REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'

# Authorization scopes required
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path of the "client_id.json" file
JSON_FILEPATH = os.path.join(os.getcwd(), 'client_id.json')

def GoogleCalendarInitView():
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)

def GoogleCalendarRedirectView():
    try:
        # Get user credentials
        credentials = google_apis_oauth.get_crendentials_from_callback(
            request,
            JSON_FILEPATH,
            SCOPES,
            REDIRECT_URI
        )

        #convert to string
        stringified_token = google_apis_oauth.stringify_credentials(
            credentials)
    except exceptions.InvalidLoginException:
        # This exception is raised
        return 0
