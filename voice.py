import speech_recognition as sr
import spot_oath


def keyword_detected():
    print("Keyword detected! Running your function...")

def listen_microphone():
    skip_keyword = 'skip'
    pause_keyword = 'pause'
    play_keyword = 'play'

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=None)
                text = recognizer.recognize_google(audio)
                
                if skip_keyword in text.lower():#skip song
                    spot_oath.skip_playback()

                elif pause_keyword in text.lower():#pause song 
                    print("trying to pause")
                    spot_oath.pause_playback("https://api.spotify.com/v1/me/player/pause")
                    
                elif play_keyword in text.lower():
                    print("Trying to play")
                    spot_oath.pause_playback("https://api.spotify.com/v1/me/player/play")

                
            except sr.UnknownValueError:
                print("Could not understand audio")
                listen_microphone()
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            