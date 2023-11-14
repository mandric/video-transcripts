from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter

# https://www.youtube.com/watch?v=DibH4GRRWQU
video_id = 'DibH4GRRWQU'

try:
    # Fetching the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Formatting the transcript into SRT format
    formatter = SRTFormatter()
    srt_formatted_transcript = formatter.format_transcript(transcript)

    # Printing the SRT formatted transcript
    print(srt_formatted_transcript)
except Exception as e:
    print("Error:", e)

