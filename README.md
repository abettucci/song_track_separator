cd demucs
pip install -r requirements.txt
python3 -m pip install -U demucs

# for Demucs
demucs PATH_TO_AUDIO_FILE_1 [PATH_TO_AUDIO_FILE_2 ...]

# If you used `pip install --user` you might need to replace demucs with python3 -m demucs
# output files saved as MP3
# use --mp3-preset to change encoder preset, 2 for best quality, 7 for fastest
python3 -m demucs --mp3 --mp3-bitrate BITRATE PATH_TO_AUDIO_FILE_1

# If your filename contain spaces don't forget to quote it !!!
demucs "my music/my favorite track.mp3"

# You can select different models with `-n` mdx_q is the quantized model, smaller but maybe a bit less accurate.
demucs -n mdx_q myfile.mp3

# If you only want to separate vocals out of an audio, use `--two-stems=vocals` (You can also set to drums or bass)
demucs --two-stems=vocals myfile.mp3