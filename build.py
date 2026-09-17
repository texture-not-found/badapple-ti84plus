#!/usr/bin/env python3
import os
import subprocess
import sys

os.environ["PATH"] += os.pathsep + "./util"

if (os.path.isfile("./bin/videopages.bin") == False):
    os.makedirs("./bin", exist_ok=True)
    print("Encoding video:")
    subprocess.run([sys.executable, "util/encode.py", "./video/frames.bin.gz", "./bin/videopages.bin"])
else:
    print("Video already encoded, skipping encode. Delete ./bin/videopages.bin to force reencode")

print("Encoding audio")
subprocess.run([sys.executable, "util/audio.py", "./music/badapple.mmp", "./music/track1.asm", "./music/track2.asm", "./music/track3.asm", "./music/track4.asm"])

print("Assembling:")
subprocess.run(["spasm", "badapple.asm", "./bin/codepages.bin"])

print("Joining code and video")
videopages_bin = open("./bin/videopages.bin", "rb")
codepages_bin = open("./bin/codepages.bin", "rb")
badapple_bin = open("./bin/badapple.bin", "wb")
badapple_bin.write(codepages_bin.read())
badapple_bin.write(videopages_bin.read())
badapple_bin.close()

print("Packaging application")
subprocess.run(["rabbitsign", "-f", "-p", "-o", "badapple.8xk", "./bin/badapple.bin"])
