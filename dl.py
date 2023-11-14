from youtube_transcript_api import YouTubeTranscriptApi

def format_time(seconds):
    """Converts seconds to the SRT time format."""
    millisec = int((seconds - int(seconds)) * 1000)
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03}"

# Replace 'e2NMHfgODuA' with the ID of your YouTube video
video_id = 'e2NMHfgODuA'

try:
    # Fetching the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Creating an SRT formatted string
    srt_format = ""
    for i, line in enumerate(transcript, start=1):
        start_time = format_time(line['start'])
        end_time = format_time(line['start'] + line['duration'])
        text = line['text'].replace('\n', ' ')  # Replacing newline characters with spaces

        srt_format += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"

    # Printing the SRT formatted string
    print(srt_format)
except Exception as e:
    print("Error:", e)


