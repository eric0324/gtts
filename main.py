# -*- coding: UTF-8 -*-
"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python main.py -text "艾瑞克好棒棒" -fname "my_file_name" -lang "zh-TW"
"""
import datetime
import subprocess
from argparse import ArgumentParser
from io import BytesIO

from gtts import gTTS


# [START tts_synthesize_text]
def synthesize_text(text, name, lang):
    tts=gTTS(text=text, lang=lang)
    tts.save("".join(
            [
                "output/",
                str(name),
                ".mp3",
            ]
        )
    )
    subprocess.call(["play", "output/"+str(name)+".mp3"])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-text", help="Input synthesize text", default="你好")
    parser.add_argument("-fname", help="Input file name", default="hello")
    parser.add_argument("-lang", help="Input gtts language", default="zh-TW")
    args = parser.parse_args()

    synthesize_text(args.text, args.fname, args.lang)
