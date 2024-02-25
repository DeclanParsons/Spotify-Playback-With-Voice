from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
import requests
import webbrowser




def spotify_oath(): 
    client_id = ""
    client_secret = ""
    redirect_uri = "https://localhost:3000"
    authorization_base_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"
    scope = ['user-modify-playback-state']

    global end_point
    

    #Create an OAuth2Session instance
    spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    #Redirect user to Spotify for authorization
    authorization_url, state = spotify.authorization_url(authorization_base_url)
    webbrowser.open(authorization_url)

    #Get the authorization verifier code from the callback url
    redirect_response = input('\n\nPaste the full redirect URL here: ')

    #Fetch the access token using the authorization code
    global token
    token = spotify.fetch_token(token_url, client_secret=client_secret,
                                authorization_response=redirect_response)

    import voice 
    voice.listen_microphone()



def skip_playback(): 
    end_point = 'https://api.spotify.com/v1/me/player/next'
    response = requests.post(end_point, headers={'Authorization': 'Bearer ' + token['access_token']})

    if response.status_code == 204:
        print("Skip Request Was Sucessful")
    else:
        print("Skip Request Failed")

def pause_playback(end_point):
    headers = {'Authorization': 'Bearer ' + token['access_token']}
    
    response = requests.put(end_point, headers=headers)
    
    if response.status_code == 204:
        print("Playback Changed Successfully")
    else:
        print("Failed to Change Playback")

    


#skip end_point = 'https://api.spotify.com/v1/me/player/next'