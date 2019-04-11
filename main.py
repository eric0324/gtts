"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python main.py --text "艾瑞克好棒棒"
"""
import argparse
import datetime

from gtts import gTTS


# [START tts_synthesize_text]
def synthesize_text(text):
    tts=gTTS(text=text, lang='zh-TW')
    tts.save("".join(
            [
                "output/",
                str(datetime.datetime.now()),
                str(text),
                ".mp3",
            ]
        )
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text',
                       help='The text from which to synthesize speech.')
    args = parser.parse_args()
    synthesize_text(args.text)
