# import pyttsx3
import speech_recognition
# import PyAudio

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)
    # robot_ear.adjust_for_ambient_noise(mic)


try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print("you:" + you)



# if you == "":
#     robot_brain = "I can't hear you, try again"
# elif you == "hello":
#     robot_brain = "hello world"
# elif you == "today":
#     robot_brain = "thu 6"
# else:
#     robot_brain = "I'm fine thank you and you"
#
# print(robot_brain)
#
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()