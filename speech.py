import azure.cognitiveservices.speech as speechsdk

def recognize_speech():
    speech_config = speechsdk.SpeechConfig(subscription="<Your_Azure_Subscription_Key>", region="<Your_Azure_Region>")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))

# Call this function in your lesson input to assist students with writing
recognize_speech()
