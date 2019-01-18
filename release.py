#!/usr/bin/env python3
import vapoursynth as vs

core = vs.get_core()
video = core.std.BlankClip(format=vs.YUV420P10, length=1000, color=[128, 190, 128]) 
video = core.sub.Subtitle(video, "WTF???", 0, 500, style="sans-serif,200,&H00FF00FF")
video.set_output()
