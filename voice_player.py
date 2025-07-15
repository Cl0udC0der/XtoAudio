import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from elevenlabs import save
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import vlc

class VoicePlayer:
    def __init__(self, key: str):
        self.elevenlabs = ElevenLabs(
            api_key=key
        )
        # self.curr_audio = None

    def make_dummy_audio(self):
        curr_audio = self.elevenlabs.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
            output_format="mp3_22050_32",
            text="I'm making this up as I go!",
            model_id="eleven_turbo_v2_5",  # use the turbo model for low latency
            # Optional voice settings that allow you to customize the output
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
                speed=0.7,
            ),
        )
        print("Audio made!")
        return curr_audio

    def make_audio(self, content: str):
        curr_audio = self.elevenlabs.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
            output_format="mp3_22050_32",
            text=content,
            model_id="eleven_turbo_v2_5",  # use the turbo model for low latency
            # Optional voice settings that allow you to customize the output
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0,
            ),
        )
        print("Audio made!")
        return curr_audio


    def save_audio(self, audio) -> str:
        save_file_path = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join("audio", save_file_path)
        # Writing the audio to a file
        with open(file_path, "wb") as f:
            for chunk in audio:
                if chunk:
                    f.write(chunk)
        print(f"{file_path}: A new audio file was saved successfully!")
        return file_path

    def play_recorded(self, file):
        if file:
            play(file)
            player = vlc.MediaPlayer('file:///tmp/foo.avi')
            player.play()
            player.get_instance()  # returns the corresponding instance
            print("File Saved!")
        else: print("Invalid file!")

    def play_byte_audio(self, audio):
        play(audio)
