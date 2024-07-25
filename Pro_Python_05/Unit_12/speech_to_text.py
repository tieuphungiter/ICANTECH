import speech_recognition as sr
#pip install SpeechRecognition
import pyttsx3
#pip install pyttsx3
import pyaudio
#pip install pyaudio
"""
  Khi gặp lỗi ModuleNotFoundError: No module named 'distutils'
  thì phải cập nhật lại lib setuptools
  pip install setuptools
  """
# Hàm chuyển văn bản thành âm thanh
def text_to_speech(text, language='vi'):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()


# Hàm nhận diện âm thanh và chuyển thành văn bản
def speech_to_text():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Lắng nghe...")
    audio = recognizer.listen(source)
  try:
    print("Đang nhận diện...")
    text = recognizer.recognize_google(audio, language='vi')
    print("Nội dung: " + text)
    return text
  except sr.UnknownValueError:
    print("Không thể nhận diện âm thanh.")
    return ""
  except sr.RequestError as e:
    print("Lỗi trong quá trình xử lý yêu cầu; {0}".format(e))
    return ""


text_to_speech("Nice to miss you!")

while True:
  print("Hãy nói điều gì đó...")
  user_input = speech_to_text()
  if user_input.lower() == "stop":
    print("Kết thúc ứng dụng.")
    text_to_speech("Kết thúc ứng dụng.")
    break
  else:
    response = "You say: " + user_input
    print("response: " + response)
    text_to_speech(response)
