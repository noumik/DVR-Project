# DVR-Project

1. Your MP4 video with hardcoded subtitles should be in the same folder as this program.
2. Download FFmpeg (https://ffmpeg.org/) and place it in the same folder as this program.
3. Run 1cropvideo.cmd to crop your video so that only the area where subtitles appear is left. Depending on your video, you may need to edit this file to select the correct area. If subtitles appear at the top and bottom of the video, skip this step.
4. Run 2getTimings.py, 2getTimingsTopAndBottom.py, or 2getTimingsTopAndBottomContinuous.py, depending on the style of the hardcoded subtitles.
      
      a. 2getTimings.py - Assumes the subtitles appear at the bottom of the screen with a solid background, which disappears every time the subtitle changes.
      
      b. 2getTimingsTopAndBottom.py - Assumes the subtitles can appear either at the top or bottom of the screen with a solid background, which disappears every time the subtitle changes.
      
      c. 2getTimingsTopAndBottomContinuous.py - Assumes the subtitles can appear either at the top or bottom of the screen with a solid background, which always stays on the screen even as the subtitles change.
5. Run 3formatTimings.py to put the extracted timings in the SRT format.
6. Run 4getFrames.py (subtitles only at the bottom of the video) or 4getFramesTopBottom.py (subtitles at the top and bottom of the video) depending on the style of subtitle.
7. A frame with each subtitle will be placed in a new folder called 'frames'.
8. Use this program, PNG2SRT (https://github.com/Zarxrax/png2srt) , to OCR the frames. It will output a completed SRT subtitle file.
