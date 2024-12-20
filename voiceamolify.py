import boto3

def synthesize_jarvis_voice(text, voice_id="Brian", rate="medium", pitch="medium", volume="medium"):
    """
    Synthesize speech with Amazon Polly to create a Jarvis-like voice.
    
    Parameters:
    - text: The text to be converted to speech.
    - voice_id: The voice ID (e.g., Brian for UK English).
    - rate: Speaking rate (e.g., x-slow, slow, medium, fast, x-fast).
    - pitch: Pitch adjustment (e.g., x-low, low, medium, high, x-high).
    - volume: Volume adjustment (e.g., silent, x-soft, soft, medium, loud, x-loud).
    
    Returns:
    - None (saves the audio to a file).
    """
    # Create SSML with desired properties
    ssml_text = f"""
    <speak>
        <prosody rate='{rate}' pitch='{pitch}' volume='{volume}'>
            {text}
        </prosody>
    </speak>
    """

    # Initialize Amazon Polly client
    polly = boto3.client("polly")

    # Request synthesis
    response = polly.synthesize_speech(
        Text=ssml_text,
        OutputFormat="mp3",
        VoiceId=voice_id,
        TextType="ssml"
    )

    # Save the audio stream to a file
    audio_file = "jarvis_like_speech.mp3"
    with open(audio_file, "wb") as file:
        file.write(response["AudioStream"].read())

    print(f"Audio saved as {audio_file}")


if __name__ == "__main__":
    # Example text
    text_to_speak = (
        "Hello, I am your personal assistant. "
        "I am here to help you with anything you need. "
        "Let us proceed with precision and efficiency."
    )

    # Customize the Jarvis-like voice properties
    synthesize_jarvis_voice(
        text=text_to_speak,
        rate="medium",
        pitch="medium",
        volume="medium"
    )





