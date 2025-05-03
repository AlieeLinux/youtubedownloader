import os
import asyncio

delfile = '/tmp/21.png'
delfile2 = "/tmp/imafile.webp"

async def removes():
    for keycontext in os.listdir("/tmp"):
        if keycontext == '21.png':
            os.remove(f"{delfile}")
        elif keycontext == 'imafile.flac':
            os.remove(delfile2)
        elif keycontext == 'pske.flac':
            os.remove("/tmp/pske.flac")
        elif keycontext == "pske.mp3":
            os.remove("/tmp/pske.mp3")


#magic wahahahah
print("type the youtube link you want to download. \n")

link = input('>>')

namemusi = input("name of the music\n >>")
namemusic = f'"{namemusi}"'

flink = f'{link}'
print("Downloading the thumbnail")

async def download_thumbnail():
    os.system(f"/usr/bin/yt-dlp --cookies-from-browser firefox  '{flink}' --embed-thumbnail --no-download  -o /tmp/imafile &")

async def download_flac():
    os.system(f'yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format flac "{flink}" --embed-metadata --parse-metadata "playlist_index:%(track_number)s" -o /tmp/pske')

def ffmpeg_function():
    os.system(f"ffmpeg -i /tmp/pske.flac -i /tmp/21.png -c:a libopus -b:a 350k -sample_fmt 24 -f opus {namemusic}")

#    os.system(f"ffmpeg -i /tmp/pske.flac -i /tmp/21.png -c:a libopus -b:a 400k -c:v png -map 0:0 -map 1:0  {namemusic}")
#    os.system(f"ffmpeg -i /tmp/pske.opus -i /tmp/21.png -map 1:0 -map 0:0 -c copy {namemusic}")

async def main():
    await removes()
    await asyncio.gather(download_thumbnail(), download_flac())


asyncio.run(main())
ffmpeg_function()
print("success :)")
