#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyttsx3


# In[3]:


pip install pyaudio


# In[1]:


import speech_recognition
import pyttsx3
import webbrowser


# In[2]:


sr = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as source:
            print("Say Something.....")
            sr.adjust_for_ambient_noise(source)
            audio = sr.listen(source)
            text = sr.recognize_google(audio)
#             text = text.lower()
            print(text)
            if(text == "how to stop"):
                print("Say stop!")
            if(text == "stop"):
                break
    except:
        print("Sorry, could not recognise.")
        print("Please try again.")
        print("To exit say stop.")
        sr = speech_recognition.Recognizer()
        continue


# In[ ]:




