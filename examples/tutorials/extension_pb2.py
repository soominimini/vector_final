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

'''
211017
'''
evt = threading.Event()
evt2 = threading.Event()
evt3 = threading.Event()
evt4 = threading.Event()
evt5 = threading.Event()
evt6 = threading.Event()


async def first_wake(event_type, event):
    print("first")
    await robot.conn.request_control()

    global wake_word_heard
    if not wake_word_heard:
        print(robot.conn.requires_behavior_control)
        wake_word_heard = True
        time.sleep(5)
        await robot.say_text("hi i'm vector")
        # await robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40')
        # await asyncio.wrap_future(robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40'))
        await robot.say_text("nice to meet you")
        robot.conn.release_control()

    print("end of first function")
    evt.set()

async def second_wake(event_type, event):
    await robot.conn.request_control()
    print("sec")
    global wake_word_heard2
    if not wake_word_heard2:
        wake_word_heard2 = True
        time.sleep(5)
        await robot.say_text("of course!")  #오른쪽에 있는 참가자를 바라보고 있는 상황
        #Positive values turn to the left, negative values to the right.
        await robot.behavior.turn_in_place(degrees(90))  # or this can be placed with remote control
        await robot.behavior.drive_straight(distance_mm(200), speed_mmps(100)) # arrive on the spot
        await robot.behavior.turn_in_place(degrees(-90)) # 참가자를 바라보는 것으로 끝맺음

        robot.conn.release_control()
    evt2.set()

async def third_wake(event_type, event):
    await robot.conn.request_control()
    print("third")
    global wake_word_heard3
    if not wake_word_heard3:
        wake_word_heard3 = True
        time.sleep(5)
        await robot.behavior.turn_in_place(degrees(90))
        await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
        await robot.behavior.turn_in_place(degrees(-90))
        await robot.anim.play_animation('anim_eyepose_sad_instronspect')
        await robot.say_text("it seems scary..")
        robot.conn.release_control()

    evt3.set()

async def fourth_wake(event_type, event):
    await robot.conn.request_control()
    print("fourth")
    global wake_word_heard4
    if not wake_word_heard4:
        wake_word_heard4 = True
        time.sleep(5)
        await robot.say_text("okay... i will try...")
        await robot.behavior.turn_in_place(degrees(90))
        await robot.behavior.set_head_angle(degrees(45.0))
        await robot.behavior.drive_straight(distance_mm(50), speed_mmps(10))
        await robot.behavior.turn_in_place(degrees(180))
        await robot.behavior.drive_straight(distance_mm(50), speed_mmps(100))
        await robot.behavior.turn_in_place(degrees(90))
        await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
        await robot.anim.play_animation('anim_eyepose_sad_instronspect')
        await robot.say_text("i cant' do this...")
        robot.conn.release_control()
    evt4.set()


async def fifth_wake(event_type, event):
    await robot.conn.request_control()
    print("fifth")
    global wake_word_heard5
    if not wake_word_heard5:
        wake_word_heard5 = True
        time.sleep(5)
        await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
        await robot.say_text("okay....")
        await robot.behavior.turn_in_place(degrees(90))
        #여기에 뭔가 더 필요
        await robot.anim.play_animation('anim_reacttocliff_edge_04')
        time.sleep(2)
        await robot.behavior.turn_in_place(degrees(-90))
        await robot.anim.play_animation('anim_eyepose_sad_instronspect')
        await robot.say_text("sorry... i can't do this...")
        robot.conn.release_control()
    evt5.set()

if __name__ == '__main__':
    with anki_vector.Robot(requires_behavior_control=True,enable_face_detection=True, cache_animation_list=False) as robot:
        print(callable(first_wake))
        robot.conn.release_control()

        try:
            robot.events.subscribe(first_wake, Events.wake_word)
            print(robot.conn.requires_behavior_control)
            time.sleep(5)
            print("after wait")
            robot.events.unsubscribe(first_wake, anki_vector.events.Events.wake_word)
        except:
            pass

        print("robot control two",robot.conn.requires_behavior_control)

        print('------ Vector is waiting to hear "Hey Vector!" 2 ------')
        # robot.requires_behavior_control = True
        try:
            if evt.is_set():
                robot.events.subscribe(second_wake, Events.wake_word)

            robot.events.unsubscribe(second_wake, Events.wake_word)
        except:
            pass

        print('------ Vector is waiting to hear "Hey Vector!" 2 ------')
        # robot.requires_behavior_control = True
        try:
            robot.events.subscribe(third_wake, anki_vector.events.Events.wake_word)
            time.sleep(10)
            robot.events.unsubscribe(third_wake, anki_vector.events.Events.wake_word)
        except:
            pass

        print('------ Vector is waiting to hear "Hey Vector!" 4 ------')

        try:
            robot.events.subscribe(fourth_wake, anki_vector.events.Events.wake_word)
            time.sleep(10)
            robot.events.unsubscribe(fourth_wake, anki_vector.events.Events.wake_word)
        except:
            pass

        print('------ Vector is waiting to hear "Hey Vector!" 5 ------')

        try:
            robot.events.subscribe(fifth_wake, anki_vector.events.Events.wake_word)
            time.sleep(10)
            robot.events.unsubscribe(fifth_wake, anki_vector.events.Events.wake_word)
        except:
            pass
