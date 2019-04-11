# -*- coding: UTF-8 -*-
"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python main.py -text "艾瑞克好棒棒"
"""
import datetime
from argparse import ArgumentParser
from io import BytesIO

from gtts import gTTS


# [START tts_synthesize_text]
def synthesize_text(text, name):
    tts=gTTS(text=text, lang='zh-TW')
    tts.save("".join(
            [
                "output/",
                str(name),
                ".mp3",
            ]
        )
    )


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-text", help="positional argument 1")
    parser.add_argument("-fname", help="optional argument",)
    args = parser.parse_args()

    synthesize_text(args.text, args.fname)
