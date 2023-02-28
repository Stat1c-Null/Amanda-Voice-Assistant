from datetime import date
import speech_recognition as sr
import pyttsx3, pywhatkit, datetime, wikipedia, pyjokes, os

clear = lambda: os.system('cls')#Clean out console
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#Choose voice
engine.setProperty('rate', 150)#Set voice speed
recog = sr.Recognizer()
micro = sr.Microphone()

def talk(text):
  engine.say(text)
  engine.runAndWait()
  print(text)

def take_command():
  #clear()
  try:
    with micro as source:
      recog.adjust_for_ambient_noise(source)
      #recog.listen_in_background(micro)
      print("Listening")
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      command = command.lower()
      if 'amanda' in command:
        command = command.replace('amanda', '')
        print(command)
      #Check if voice request is empty
      return command
  except:
    pass

def run_amanda():
  command = take_command()
  if command is None:
    run_amanda()
    #recog.listen_in_background(micro, run_amanda)
  else:
    if 'play' in command:
      song = command.replace('play', '')
      talk('playing' + song)
      #pywhatkit.playonyt(song)
      #TODO: OPEN SPOTIFY AND PLAY A SONG
    elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      talk('current time is ' + time)
    elif 'date' in command:
      talk(f"Today's date is {date.today()}")
    elif 'who is' in command:
      person = command.replace('who is', '')
      search_wiki(person)
    elif 'what is' in command:
      item = command.replace('what is', '')
      search_wiki(item)
    elif 'joke' in command:
      talk(pyjokes.get_joke())
    elif 'are you single' in command:
      talk('I am in a relationship with my right hand')
    elif 'ugly' in command:
      talk('Fuck you, you fucking cracker')
    elif 'stupid' in command:
      talk('Good luck helping yourself without me, jerk')
    elif 'thank you' in command:
      talk('Someone is nice to me finally')
    else:
      talk('Repeat the command, I cant understand you')

def search_wiki(target):
  try:
    talk(wikipedia.summary(target, 2))
  except:
    talk("Sorry wikipedia is been stupid")

while True:
  run_amanda()


