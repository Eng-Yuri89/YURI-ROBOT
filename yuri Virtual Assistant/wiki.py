import wolframalpha
import wikipedia
import wikipedia_cli





while True:
    usrinput = input("question:" )
    try:
        #wolframalpha
        client = wolframalpha.Client ( 'QEUXVY-VRAH5X4EA6' )
        res = client.query ( usrinput )
        answer = next ( res.results ).text
        print ( answer )
    except:
        print(wikipedia.summary(usrinput, sentences=2))