import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import os

engine = pyttsx3.init( 'sapi5' )                #Creating object for text to Audio
voices = engine.getProperty( 'voices' )         #Setting up the things with engine
engine.setProperty( 'voice', voices[0].id  )    #0 for Male and 1 for Female, Show -> print( voices )


def setup():
    r = sr.Recognizer()  # Making Recognizer object, we will use it with source Input i.e., source VAR

    with sr.Microphone() as source:  # Setting the source of Input
        r.pause_threshold = 1

        # r.listen( source ) means Start listening to the source( Microphone ) and put the Audio input as string
        # in audio var.
        audio = r.listen(source)

        return r, audio

def ask( pausethreshold = 1 ):
    r, audio = setup()
    r.pause_threshold = pausethreshold
    print("Listening...")
    print("Recognizing")
    query = r.recognize_google(audio, language="en-in")  # We are recognizing whatever input we gave.
    print(f"User Said : {query}\n")
    return query.lower()

def wishme( name ):
    jarvis_msg = ""
    time_data = datetime.datetime.now()

    if( time_data.hour >4 and time_data.hour<12 ):
        jarvis_msg = "Good Morning"

    elif( time_data.hour >= 12 and time_data.hour < 15 ):
        jarvis_msg = "Good Afternoon"

    elif( time_data.hour >= 15 and time_data.hour < 19 ):
        jarvis_msg = "Good Evening"

    else:
        jarvis_msg = "Good Night"

    print( f"{jarvis_msg} { name }" )
    speak( f"{jarvis_msg} { name }" )
    speak( "How may i help you ?" )

def time():
    time_data = datetime.datetime.now()
    msg = ""

    if( time_data.hour >= 12 ):
        msg = f"{time_data.hour - 12} : { time_data.minute } : { time_data.second } PM"
    else:
        msg = f"{time_data.hour} : { time_data.minute } : { time_data.second } AM"

    msg = f"{msg}, { time_data.day } "

    month = time_data.month

    if( month == 1 ):
        msg = msg + "JAN"

    elif( month == 2 ):
        msg = msg + "FEB"

    elif (month == 3):
        msg = msg + "MAR"

    elif (month == 4):
        msg = msg + "APR"

    elif (month == 5):
        msg = msg + "MAY"

    elif (month == 6):
        msg = msg + "JUNE"

    elif (month == 7):
        msg = msg + "JULY"

    elif (month == 8):
        msg = msg + "AUG"

    elif (month == 9):
        msg = msg + "SEP"

    elif (month == 10):
        msg = msg + "OCT"

    elif (month == 11):
        msg = msg + "NOV"

    elif (month == 12):
        msg = msg + "DEC"

    msg = f"{ msg } { time_data.year }"

    return msg

def speak( audio ):
    engine.say( audio )     #Convert text to Audio
    engine.runAndWait()     #Event to Run and then, wait for next Command

def takecommand():
    try:
        query = ask()

        if( ('wikipedia' in query) or ('wiki' in query) ):
            speak( "Noted Sir, Searching Wikipedia...")
            query = query.replace( "wikipedia", "" )

            print( "Noted Sir, Searching Wikipedia..." )

            if( 'wiki' in query ):
                query = query.replace( "wiki", "" )
            else:
                query = query.replace( 'wikipedia', "" )

            result = wiki.summary( query, sentences = 2 )
            print( f"result = ", end='' )

            result = result.split( "." )

            for i in result:
                print( i )

            speak( result )

        elif( 'youtube' in query ):
            speak( "Opening Youtube" )
            webbrowser.open( "www.youtube.com" )
            return None

        elif ('google' in query):
            speak("Opening Google")
            webbrowser.open("www.google.co.in")
            return None

        elif (("open" in query) and ("facebook" in query)):
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com/")

        elif ( ("open" in query) and ("bsnl" in query) ):
            speak("Opening UPE - BSNL Tender Website")
            webbrowser.open( "http://210.212.53.115/tender/tender.asp" )
            return None

        elif( ( "open" in query ) and ("file" in query ) and ( "explorer" in query ) ):
            path = r"C:"
            webbrowser.open(path)

            while( True ):
                speak( f"Pause Threshold is { 5 }" )
                query = ask( pausethreshold=5 ).split(' ')

                print( f"query = { query }" )

                if( ( "close" in query ) and ("file" in query ) and ( "explorer" in query ) ):
                    break

                else:
                    files = list( os.listdir( path ) )
                    count = 0

                    file_flag = False
                    file_name = ""

                    for i in files:
                        if( i.lower() in query ):
                            file_flag = True
                            file_name = i

                        if( count%10 == 0 ):
                            print()

                        print( i, end=', ' )
                        count = count + 1

                    print( f"Total number of files = { len( files ) }" )

                    if( file_flag ):
                        path = path + '\\' + file_name

                    else:
                        speak("There is no such Files or Folder, Pleasse Try Again !")

        elif( ( "time" in query ) ):
            time = datetime.datetime.now().strftime("%H : %H : %S")
            speak( f"The Time is { time }" )

        elif( ( "play" in query ) and ( "video" in query ) ):
            print(1)

            path = r"C:\Users\gauta\Desktop\Pytohn Harshit"

            files = os.listdir( path )

            if( len( files ) >0 ):

                speak( "There are Following Files," )
                for i in files:
                    print(i)

                while( True ):
                    speak("Pause Threshold is 5 seconds")
                    try:
                        query = ask( pausethreshold = 5 )

                        if( ("go" in query ) and ( "back" in query ) ):
                            break
                        else:
                            music_found = False
                            music_name = ""

                            if( 'play' in query ):
                                query = query.replace( "play", "" )

                            print( f"query = { query }" )

                            file_count = 0
                            temp_files = []

                            for i in files:
                                if( ( query in i.lower() )  ):
                                    music_name = i
                                    music_found = True
                                    temp_files.append( i )
                                    file_count = file_count + 1

                            if( file_count == 0 ):
                                speak(f"Sorry Sir, There no file of name { query }")

                            elif( file_count == 1 ):
                                music_found = True
                                music_name = i
                                os.startfile(path + '\\' + i)
                                print(f"Video Path = {path + '.' + i}")

                            else:
                                while( True ):
                                    attempt = 0
                                    try :
                                        attempt = attempt + 1
                                        if( attempt == 3 ):
                                            speak("Sir, Reached Maximum Attempt. Please Try Again.")

                                        else:
                                            attempt = attempt + 1
                                            speak(f"Sir, There are {file_count} files, Can you be more specific ?")
                                            speak(f"There are following names, ")

                                            for i in temp_files:
                                                print(i)

                                            query = ask(pausethreshold=5)

                                            for i in temp_files:
                                                if( query in i.lower().replace( '  ', ' ' ) ):
                                                    music_found = True
                                                    music_name = i
                                                    os.startfile(path + '\\' + i)
                                                    print(f"Video Path = {path + '.' + i}")
                                                    music_found = True
                                                    break

                                                else:
                                                    music_found = False

                                            if( music_found == False ):
                                                speak("Wrong name sir, Please try again")

                                            else:
                                                speak(f"Playing video {music_name}")
                                                break

                                    except Exception as e:
                                        print( "Sorry Sir, Time Out. Try Again ! " )
                                        speak("Sorry Sir, Time Out. Try Again ! ")

                            if (music_found == True):
                                break


                    except Exception as e:
                        print(f"e = {type(e)}, Pardon !")
                        return None

            else:
                speak("Empty File Sir. Try Again !")

        elif( ( "open" in query ) and ( "pycharm" in query ) ):
            print( "Opening Pycharm" )
            speak("Opening Pycharm")
            a = os.startfile( r"C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.4\bin\pycharm64.exe" )

        elif( ( "open" in query ) and ( "python" in query ) ):
            speak("Opening Python")
            os.startfile( r"C:\Users\gauta\AppData\Local\Programs\Python\Python37\python.exe")

        elif (("shut" in query) and ("down" in query) and ("jarvis" in query)):
            speak(f"Good Bye Sir, See you soon")
            return 0

    except Exception as e:
        print( f"Pardon sir, I am waiting for the command" )
        speak( f"Pardon sir, I am waiting for the command" )
        return  None

if( __name__ == "__main__" ):
    #name = input("Enter your name = ")

    wishme( "" )
    while(True):
        print("""Option Available,
                    1. Time, 2. Ask Wikipedia, 3.Open Youtube
                    4. Open Google, 5.Open BSNL Website
                    6. Open Facebook""")
        if( takecommand() == 0 ):
            break