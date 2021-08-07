# STT-TTS
from ibm_watson import TextToSpeechV1
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
استخدام الصفوف المطلوبة المطلوبة لتنفيذ البرنامج من المكتبات ibm_watson و ibm_cloud_sdk_core   

بعد انشاء حساب عل ى موقع ibm واستخدام خدمات تحويل النص الى كلام والعكس يتم الحصول على سلسلة نصية خاصة بالخدمة 
var1 = IAMAuthenticator("7VzxJ9zwoxsfljKvTmKSmaNretVc5K472tbSrDCoeyNR")
تمرير وسيط سلسلة نصية الخاصة بالخدمة للطريقة وحفظ النتيجة في متحول 
text_to_speech = TextToSpeechV1(authenticator=var1)
text_to_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba09f44a-48b7-4742-b652-5684311ee0fd")
 تمرير وسيط رابط url خاص بالخدمة كوسيط أيضا 
str = "Welcome Smart Methods Company"
filename1 = "audiofile"

with open (filename1+".mp3","wb") as audiofile1:
  )  audiofile1.write
        text_to_speech.synthesize(str,accept="audio/mp3").get_result().content
       (
انشاء ملف صوتي باسم audiofile وحفظ النص الموجود ضمن المتحول str  ك تسجيل صوتي mp3 
with open(filename1+".mp3","rb") as audiofile2:
  result = speech_to_text.recognize(audio=audiofile2,content_type="audio/mp3").get_result()
تحويل الملف الصوتي ذو الاسم المخزن ضمن المتحول filename1 الى نص 
txt=(result['results'][0]['alternatives'][0]['transcript'])
filename2 = "txtfile.txt"
file = open(filename2,"w")
file.write(txt)
file.close()
تخزين النص المخزن صمن المتحول result الى ملف نصي
