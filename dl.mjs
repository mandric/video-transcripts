const vidId = "DibH4GRRWQU"
//var yt = require("youtube-transcript");
//yt.YoutubeTranscript.fetchTranscript(vidId).then(console.log);

import { YoutubeTranscript } from "youtube-transcript";
YoutubeTranscript.fetchTranscript(vidId).then(console.log);

