from TTS.api import TTS

class TextToSpeech:
    def __init__(self):
        """ Load the Coqui TTS model """
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    def generate_speech(self, text, output_path="outputs/speech_output.wav"):
        """ Convert text into speech and save it as a WAV file """
        self.tts.tts_to_file(text=text, file_path=output_path)
