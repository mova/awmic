#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pulsectl

pulse = pulsectl.Pulse("awmic-rec")


def is_recorder(o: pulsectl.PulseSourceOutputInfo):
    pD = o.proplist
    # remove whatever pavucontrol is doing
    if "application.id" in pD:
        if pD["application.id"] == "org.PulseAudio.pavucontrol":
            return False
    # All apps record stereo
    if "channel_count" not in vars(o):
        return False
    elif o.channel_count < 1:
        return False

    return True


output_dev_list = pulse.sink_list()
players = pulse.sink_input_list()
input_dev_list = pulse.source_list()
recorders = [e for e in pulse.source_output_list() if is_recorder(e)]


def is_recording(o: pulsectl.PulseSourceOutputInfo):
    if o.mute == 1:
        return False
    if o.volume.values == [0, 0]:
        return False
    source: pulsectl.PulseSourceInfo = input_dev_list[o.source-1]
    if source.mute == 1:
        return False
    if source.volume.values == [0, 0]:
        return False

    return True
from time import sleep
import audioop
import pyaudio
chunk = 1024

stream = p.open(format=pyaudio.paInt16,channels=2, rate=44100, input=True, frames_per_buffer=chunk)


def query():
    if len(recorders) == 0:
        # Nobody recoding
        out = ""
    elif any([is_recording(r) for r in recorders]):
        # Somebody ist recording and not muted
        out = ""
    else:
        # Somebody ist recording and muted
        out = ""
    return f"<span>{out}</span>"


def toggle():
    if any([r.mute == 1 for r in recorders]):
        for r in recorders:
            pulse.mute(r, False)
    else:
        for r in recorders:
            pulse.mute(r, True)


def changeVol(by: float):
    # get the lowest volume of the recorders, then add 5% the volume
    vol = min([min(r.volume.values) for r in recorders])
    vol = max(0, min(1, vol + by))
    for r in recorders:
        if by > 0 and r.mute == 1:
            pulse.mute(r, False)
        pulse.volume_set_all_chans(r, vol)


if __name__ == "__main__":
    if sys.argv[-1] == "--query":
        print(query())
    elif sys.argv[-1] == "--raise":
        changeVol(0.07)
    elif sys.argv[-1] == "--lower":
        changeVol(-0.07)
    elif sys.argv[-1] == "--toggle":
        toggle()
    else:
        print(query())
