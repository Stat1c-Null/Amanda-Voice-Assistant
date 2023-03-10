from datetime import date
import speech_recognition as sr
import pyttsx3, pywhatkit, datetime, wikipedia, pyjokes, os, random, time, re

clear = lambda: os.system('cls')#Clean out console
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#Choose voice
engine.setProperty('rate', 150)#Set voice speed
micro = sr.Microphone()

timerOn = False
alarmOn = False

#Talk to me
def say(text):
  engine.say(text)
  engine.runAndWait()
  print(text)

#Recognize command
def take_command():
  #clear()
  try:
    with micro as source:
      listener.adjust_for_ambient_noise(source)
      print("Listening")
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      command = command.lower()
      if 'amanda' in command:
        command = command.replace('amanda', '')
        print(command)
      return command
  except:
    pass

#Make decisions based on commands
def run_amanda():
  command = take_command()
  if command is None:
    run_amanda()
    #listener.listen_in_background(micro, run_amanda)
  else:
    if 'play' in command:
      song = command.replace('play', '')
      say('playing' + song)
      pywhatkit.playonyt(song)
    elif 'set timer for' in command:
      set_timer(command)
    elif 'what time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      say('current time is ' + time)
    elif 'date' in command:
      say(f"Today's date is {date.today()}")
    elif 'who is' in command:
      person = command.replace('who is', '')
      search_wiki(person)
    elif 'what is' in command:
      item = command.replace('what is', '')
      search_wiki(item)
    elif 'joke' in command:
      jokes = ["chuck", "neutral", "twister", "all"]
      joke = random.choice(jokes)
      say(pyjokes.get_joke("en", joke))
    elif 'are you single' in command:
      phrases = ["I am in a relationship with my right hand", "I am single and ready to mingle"]
      ran = random.choice(phrases)
      say(ran)
    elif 'ugly' in command:
      say('Fuck you, you fucking cracker')
    elif 'stupid' in command:
      say('Good luck helping yourself without me, jerk')
      quit()
    elif 'you are amazing' in command:
      say('Awww I know')
    elif 'thank you' in command:
      say('Someone is nice to me finally')
    elif 'bye' or 'see you' or 'see ya' in command:
      say('It was nice to be useful for a moment, good bye')
      quit()
    else:
      say('Repeat the command, I cant understand you')

def set_timer(command):
  num = re.findall(r'\d+', command)#Extract number from string
  amount = int(num[0])
  if 'seconds' in command:
    say(f'Okay setting timer for {num} seconds')
    time.sleep(amount)
    say('Time is up buddy')
  elif 'minutes' in command:
    say(f'Okay setting timer for {num} minutes')
    mins = amount * 60
    time.sleep(mins)
  else:
    say('Sorry I am getting old, cant hear you so well, repeat yourself')

#Search wikipedia for answers
def search_wiki(target):
  try:
    say(wikipedia.summary(target, 2))
  except:
    say("Sorry wikipedia is been stupid")

while True:
  run_amanda()


