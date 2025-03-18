import os
from models.blip2 import ImageCaptioning
from models.tts import TextToSpeech
from utils.file_utils import save_text
from models.context_expander import ContextExpander
#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

# Define paths
IMAGE_PATH = "data/eif.jpeg"
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

    # Step 4: Caption becomes a little big like conversation
    print("Expanding caption with AI...")
    expander = ContextExpander()
    expanded_caption = expander.expand_caption(caption)
    # print(f"Expanded Caption: {expanded_caption}")

    # Save expanded caption to file
    save_text(expanded_caption, CAPTION_PATH)
    

    # Step 3: Convert Caption to Speech
    print("Converting caption to speech...")
    tts_model = TextToSpeech()
    tts_model.generate_speech(expanded_caption, AUDIO_OUTPUT_PATH)

    print(f"Speech output saved to: {AUDIO_OUTPUT_PATH}")

if __name__ == "__main__":
    main()
