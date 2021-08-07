from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from ibm_watson import SpeechToTextV1


# convert from  text to speech (file.mp3)
var1 = IAMAuthenticator("7VzxJ9zwoxsfljKvTmKSmaNretVc5K472tbSrDCoeyNR")
text_to_speech = TextToSpeechV1(authenticator=var1)
text_to_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba09f44a-48b7-4742-b652-5684311ee0fd")

str = "Welcome Smart Methods Company"
filename1 = "audiofile"

with open (filename1+".mp3","wb") as audiofile1:
    audiofile1.write (
        text_to_speech.synthesize(str,accept="audio/mp3").get_result().content
        )
    
# convert from  speech to text (file.txt)
var2 = IAMAuthenticator("Sx2v59yznyssqH1BDrNyyUtJ7DcKtn2T0IfWqgv5brq9")
speech_to_text = SpeechToTextV1(authenticator=var2)
speech_to_text.set_service_url("https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/82e66b67-6d4f-4dee-95c1-5453173a5a2e")

with open(filename1+".mp3","rb") as audiofile2:
     result = speech_to_text.recognize(audio=audiofile2,content_type="audio/mp3").get_result()

txt=(result['results'][0]['alternatives'][0]['transcript'])
filename2 = "txtfile.txt"
file = open(filename2,"w")
file.write(txt)
file.close();
