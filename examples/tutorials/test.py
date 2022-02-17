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

def first():
    evt = threading.Event()

    # robot.conn.request_control()
    async def first_wake(event_type, event):
        await robot.conn.request_control()

        global wake_word_heard
        if not wake_word_heard:
            print(robot.conn.requires_behavior_control)
            wake_word_heard = True
            time.sleep(5)
            await robot.say_text("hi i'm vector" )
            # await robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40')
            # await asyncio.wrap_future(robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_40'))
            await robot.say_text("nice to meet you")
            evt.set()

    robot.events.subscribe(first_wake, Events.wake_word)

    print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')
    print(evt._flag)

    try:
        robot.conn.release_control()
        print(robot.conn.requires_behavior_control)
        if not evt.wait(timeout=60):
            first_wake()
            print("F")
        print("after wait")
    except:
        pass
    # robot.conn.release_control()
    robot.conn.request_control()
    robot.events.unsubscribe(first_wake, Events.wake_word)
    second()


def second():
    evt2 = threading.Event()
    print("////////////")
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

            evt2.set()

    robot.events.subscribe(second_wake, anki_vector.events.Events.wake_word)


    print('------ Vector is waiting to hear "Hey Vector!" 2 ------')
    # robot.requires_behavior_control = True
    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt2.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    # robot.conn.release_control()
    robot.conn.request_control()
    robot.events.unsubscribe(second_wake, Events.wake_word)
    third()

def third():
    evt3 = threading.Event()
    print("////////////")
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
            evt3.set()


    robot.events.subscribe(third_wake, anki_vector.events.Events.wake_word)


    print('------ Vector is waiting to hear "Hey Vector!" 3 ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt3.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    # robot.conn.release_control()
    robot.conn.request_control()
    robot.events.unsubscribe(third_wake, Events.wake_word)
    fourth()


def fourth():
    evt4 = threading.Event()
    print("////////////")
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
            evt4.set()


    robot.events.subscribe(fourth_wake, anki_vector.events.Events.wake_word)

    print('------ Vector is waiting to hear "Hey Vector!" 4 ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt4.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    # robot.conn.release_control()
    robot.conn.request_control()
    robot.events.unsubscribe(fourth_wake, anki_vector.events.Events.wake_word)
    fifth()


def fifth():
    evt5 = threading.Event()
    print("////////////")
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
            evt5.set()

    robot.events.subscribe(fifth_wake, anki_vector.events.Events.wake_word)
    print('------ Vector is waiting to hear "Hey Vector!" 5 ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt5.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    robot.conn.release_control()
    robot.events.unsubscribe(fifth_wake, anki_vector.events.Events.wake_word)
    sixth()

def sixth():
    evt6 = threading.Event()

    async def sixth_wake(event_type, event):
        await robot.conn.request_control()
        global wake_word_heard6
        if not wake_word_heard6:
            wake_word_heard6 = True
            time.sleep(6)
            await robot.behavior.turn_in_place(degrees(90))
            await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
            await robot.anim.play_animation('anim_eyepose_sad_instronspect')
            await robot.behavior.turn_in_place(degrees(-90))
            await robot.say_text("but it is too scary..")
            evt6.set()

    robot.events.subscribe(sixth_wake, anki_vector.events.Events.wake_word)


    print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt6.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    robot.conn.release_control()
    robot.events.unsubscribe(sixth_wake, anki_vector.events.Events.wake_word)
    seventh()

def seventh():
    evt7 = threading.Event()

    async def seventh_wake(event_type, event):
        await robot.conn.request_control()
        global wake_word_heard7
        if not wake_word_heard7:
            wake_word_heard7 = True
            time.sleep(6)
            await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
            await robot.anim.play_animation('anim_eyepose_determined')
            await robot.say_text("Okay I will try!")
            await robot.behavior.turn_in_place(degrees(90))
            await robot.behavior.drive_straight(distance_mm(100), speed_mmps(50))
            await robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
            # encounter


            await robot.anim.play_animation('anim_eyepose_sad_instronspect')
            await robot.behavior.turn_in_place(degrees(180))
            await robot.behavior.drive_straight(distance_mm(200), speed_mmps(300))  # run away
            await robot.behavior.turn_in_place(degrees(90))
            await robot.anim.play_animation('anim_eyepose_sad_up')
            await robot.say_text("i was almost dead")
            evt7.set()

    robot.events.subscribe(seventh_wake, anki_vector.events.Events.wake_word)


    print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt7.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    robot.conn.release_control()
    robot.events.unsubscribe(seventh_wake, anki_vector.events.Events.wake_word)
    eighth()


def eighth():
    evt8 = threading.Event()

    async def eighth_wake(event_type, event):
        await robot.conn.request_control()
        global wake_word_heard8
        if not wake_word_heard8:
            wake_word_heard8 = True
            time.sleep(5)
            await robot.say_text("okay! i will try again!")
            await robot.behavior.turn_in_place(degrees(90))
            await robot.behavior.drive_straight(distance_mm(200), speed_mmps(50))
            await robot.behavior.drive_straight(distance_mm(200), speed_mmps(100))
            await robot.behavior.turn_in_place(degrees(270))
            await robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
            await robot.anim.play_animation('anim_greeting_happy_03_head_angle_40')
            await robot.say_text("i did it!!")
            evt8.set()

    robot.events.subscribe(eighth_wake, anki_vector.events.Events.wake_word)


    print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

    try:
        robot.conn.release_control()
        time.sleep(10)
        if not evt8.wait(timeout=60):
            print('------ Vector never heard "Hey Vector!" ------')
    except:
        pass
    robot.conn.release_control()
    robot.events.unsubscribe(eighth_wake, anki_vector.events.Events.wake_word)


if __name__ == '__main__':
    with anki_vector.Robot(config={"cert": "C:/Users/Hyunseung/.anki_vector/Vector-C1G1-00a10bb4.cert", "name": "Vector-C1G1" },requires_behavior_control=True,enable_face_detection=True, cache_animation_list=False) as robot:
        first()