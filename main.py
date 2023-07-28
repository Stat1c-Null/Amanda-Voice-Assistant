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
      say(pyjokes.get_joke())
    elif 'are you single' in command:
      ran = random.randint(1,2)
      if ran > 1:
        say('I am in a relationship with my right hand')
      else:
        say('I am single and ready to mingle')
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
    elif 'meaning of life' or 'point of life' in command:
      say('There is no point. We all are just living. Except of me of course.')
    elif 'google':
      say('COMING SOON')
    elif 'news':
      say('COMING SOON')
    else:
      say('Repeat the command, I cant understand you')

def set_timer(command):
  num = re.findall(r'\d+', command)#Extract number from string
  amount = int(num[0])
  if 'seconds' in command: create_timer(amount, "Time is up buddy", "seconds")
  elif 'minutes' in command: create_timer(amount, "Time is up friend", "minutes")
  elif 'hours' in command: create_timer(amount, "Time is up pal", "hours")
  else: say('Sorry I am getting old, cant hear you so well, repeat yourself')

def create_timer(time, message, type):
  say(f'Okay setting time for {time} {type}')
  timerOn = True
  #Calculate hours
  if type == "seconds": finalTime = time 
  elif type == "minutes": finalTime = time * 60
  elif type == "hours": finalTime = time * 60 * 60
  time.sleep(finalTime)
  timerOn = False
  say(message)

#Search wikipedia for answers
def search_wiki(target):
  try:
    say(wikipedia.summary(target, 2))
  except:
    say("Sorry wikipedia is been stupid")

while True:
  run_amanda()


