import os
from pydub import AudioSegment

# Define the path to the separated tracks
separated_tracks_path = "path_to_separated_tracks"

# Load each track
vocal = AudioSegment.from_file(os.path.join(separated_tracks_path, "vocals.mp3")) #o .wav
bass = AudioSegment.from_file(os.path.join(separated_tracks_path, "bass.mp3")) #o .wav
drums = AudioSegment.from_file(os.path.join(separated_tracks_path, "drums.mp3")) #o .wav
other = AudioSegment.from_file(os.path.join(separated_tracks_path, "other.mp3")) #o .wav

# Combine tracks without the guitar
combined = vocal.overlay(bass).overlay(drums).overlay(other)

# Export the combined track
combined.export("output_without_guitar.mp3", format="mp3")