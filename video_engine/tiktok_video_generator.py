from moviepy.editor import (
    ImageClip,
    TextClip,
    CompositeVideoClip,
    AudioFileClip
)
import random
import os

class TikTokVideoGenerator:
    def __init__(self, assets_path="assets/", logger=None):
        self.assets_path = assets_path
        self.logger = logger

    def generate(self, design_path, text_lines, output_path="output/tiktok_video.mp4"):
        """
        Generates a TikTok-style video using:
        - design image
        - animated text
        - trending audio
        """

        # Load design
        design = ImageClip(design_path).set_duration(6).resize(height=1080)

        # Random trending audio
        audio_files = [
            "audio1.mp3",
            "audio2.mp3",
            "audio3.mp3"
        ]
        audio_path = os.path.join(self.assets_path, random.choice(audio_files))
        audio = AudioFileClip(audio_path).volumex(0.9)

        # Animated text layers
        text_clips = []
        y_pos = 200

        for line in text_lines:
            txt = (
                TextClip(line, fontsize=90, color="white", font="Arial-Bold")
                .set_position(("center", y_pos))
                .set_duration(6)
                .fadein(0.5)
                .fadeout(0.5)
            )
            text_clips.append(txt)
            y_pos += 150

        # Final video
        final = CompositeVideoClip([design] + text_clips)
        final = final.set_audio(audio)

        # Export
        final.write_videofile(output_path, fps=30)

        if self.logger:
            self.logger.info("TikTok video generated successfully.")

        return {
            "status": "video_generated",
            "output": output_path
        }
