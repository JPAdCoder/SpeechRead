import azure.cognitiveservices.speech as speechsdk

if __name__ == '__main__':
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_key = "6f424bb3f0c649b2a8bd8bdf24890a23"
    service_region = "eastasia"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaochenNeural"

    text = "你好，这是晓辰。"

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("file.wav")
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
