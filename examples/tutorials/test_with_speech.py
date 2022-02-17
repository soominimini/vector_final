from multiprocessing import Process
import threading
import time
import anki_vector
from anki_vector.events import Events
from anki_vector import util
from anki_vector import behavior
from anki_vector.util import *
from anki_vector.behavior import *
from anki_vector import connection

import asyncio

import speech_recognition as sr
import pyaudio
import wave

from anki_vector import audio as adio


wake_word_heard = False
wake_word_heard2 = False
wake_word_heard3 = False
wake_word_heard4 = False
wake_word_heard5 = False
wake_word_heard6 = False
wake_word_heard7 = False
wake_word_heard8 = False

wake_word_heard_sk = False
Face = False

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "vector.wav"

def first_bhvr():

    robot.say_text("hi i'm vector" )
    robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40')
    robot.say_text("nice to meet you")

def second_bhvr():
    time.sleep(5)
    robot.say_text("of course!")  # 오른쪽에 있는 참가자를 바라보고 있는 상황
    # Positive values turn to the left, negative values to the right.
    robot.behavior.turn_in_place(degrees(90))  # or this can be placed with remote control
    robot.behavior.drive_straight(distance_mm(200), speed_mmps(100))  # arrive on the spot
    robot.behavior.turn_in_place(degrees(-90))  # 참가자를 바라보는 것으로 끝맺음


def third_bhvr():
    time.sleep(5)
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.behavior.turn_in_place(degrees(-90))
    robot.anim.play_animation('anim_eyepose_sad_instronspect')
    robot.say_text("it seems scary..")

def fourth_bhvr():
    time.sleep(3)
    robot.say_text("okay... i will try...")
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.drive_straight(distance_mm(50), speed_mmps(10))
    robot.behavior.turn_in_place(degrees(180))
    robot.behavior.drive_straight(distance_mm(50), speed_mmps(100))
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.anim.play_animation('anim_eyepose_sad_instronspect')
    robot.say_text("i cant' do this...")
def fifth_bhvr():
    time.sleep(5)
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.say_text("okay....")
    robot.behavior.turn_in_place(degrees(90))
    # 여기에 뭔가 더 필요
    robot.anim.play_animation('anim_reacttocliff_edge_04')


    time.sleep(2)
    robot.behavior.turn_in_place(degrees(-90))
    robot.anim.play_animation('anim_eyepose_sad_instronspect')
    robot.say_text("sorry... i can't do this...")

def sixth_bhvr():
    time.sleep(6)
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.anim.play_animation('anim_eyepose_sad_instronspect')
    robot.behavior.turn_in_place(degrees(-90))
    robot.say_text("but it is too scary..")

def seventh_bhvr():
    time.sleep(6)
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.anim.play_animation('anim_eyepose_determined')
    robot.say_text("Okay I will try!")
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.drive_straight(distance_mm(100), speed_mmps(50))
    robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
    # encounter

    robot.anim.play_animation('anim_eyepose_sad_instronspect')
    robot.behavior.turn_in_place(degrees(180))
    robot.behavior.drive_straight(distance_mm(200), speed_mmps(300))  # run away
    robot.behavior.turn_in_place(degrees(90))
    robot.anim.play_animation('anim_eyepose_sad_up')
    robot.say_text("i was almost dead")

def eighth_bhvr():
    time.sleep(5)
    robot.say_text("okay! i will try again!")
    robot.behavior.turn_in_place(degrees(90))
    robot.behavior.drive_straight(distance_mm(200), speed_mmps(50))
    robot.behavior.drive_straight(distance_mm(200), speed_mmps(100))
    robot.behavior.turn_in_place(degrees(270))
    robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    robot.anim.play_animation('anim_greeting_happy_03_head_angle_40')
    robot.say_text("i did it!!")

def first():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            first_bhvr()

    except:
        pass
    second()


def second():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('------ Vector is waiting to hear "Hey Vector!" 2 ------')
    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * 5)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("CHUNK :", CHUNK, "RATE: ", RATE)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            second_bhvr()


    except:
        pass
    # robot.conn.release_control()

    third()

def third():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 3 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            third_bhvr()
    except:
        pass
    fourth()


def fourth():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 4 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            fourth_bhvr()
    except:
        pass

    fifth()


def fifth():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 5 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            fifth_bhvr()
    except:
        pass
    sixth()

def sixth():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 6 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            sixth_bhvr()
    except:
        pass

    robot.conn.request_control()
    seventh()

def seventh():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 7 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            seventh_bhvr()
    except:
        pass

    robot.conn.request_control()
    eighth()


def eighth():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('------ Vector is waiting to hear "Hey Vector!" 8 ------')

    try:
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()
        harvard = sr.AudioFile('vector.wav')
        with harvard as source:
            audio = r.record(source)
            print(type(audio))
            print(r.recognize_google(audio))
            eighth_bhvr()
    except:
        pass

    robot.conn.request_control()


if __name__ == '__main__':
    with anki_vector.Robot(config={"cert": "C:/Users/Hyunseung/.anki_vector/Vector-C1G1-00a10bb4.cert", "name": "Vector-C1G1" },requires_behavior_control=True,  cache_animation_list=True) as robot:
        first()