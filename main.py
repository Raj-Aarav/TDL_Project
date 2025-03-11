import os
from models.blip2 import ImageCaptioning
from models.tts import TextToSpeech
from utils.file_utils import save_text

# Define paths
IMAGE_PATH = "data/sample1.jpg"
CAPTION_PATH = "outputs/caption.txt"
AUDIO_OUTPUT_PATH = "outputs/speech_output.wav"

def main():
    # Step 1: Generate Caption from Image
    print("Generating caption for image...")
    captioning_model = ImageCaptioning()
    caption = captioning_model.generate_caption(IMAGE_PATH)
    print(f"Generated Caption: {caption}")

    # Save caption to file
    save_text(caption, CAPTION_PATH)

    # Step 2: Convert Caption to Speech
    print("Converting caption to speech...")
    tts_model = TextToSpeech()
    tts_model.generate_speech(caption, AUDIO_OUTPUT_PATH)

    print(f"Speech output saved to: {AUDIO_OUTPUT_PATH}")

if __name__ == "__main__":
    main()
