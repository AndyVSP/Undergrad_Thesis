#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 23, 2022, at 22:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Experiment2A'  # from the Builder filename that created this script
expInfo = {'participant': '', 'id': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\andyv\\Documents\\School\\Thesis\\PsychoPy\\Experiment2A\\Experiment2A.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "TitlePage"
TitlePageClock = core.Clock()
Title = visual.TextStim(win=win, name='Title',
    text='The Nonverbal Behavior Study',
    font='Times New Roman',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Authors = visual.TextStim(win=win, name='Authors',
    text='The following study is being conducted by Andrea Salazar Parra under the supervision of Dr. Michael Conway of the Psychology Department at Concordia University in Montreal, Canada.',
    font='Times New Roman',
    pos=(0, 0.2), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PressSpace = visual.TextStim(win=win, name='PressSpace',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Please keep the window in full screen and make sure your volume is turned on.\n',
    font='Times New Roman',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "IntroVid"
IntroVidClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',units='height', 
    noAudio = False,
    filename='Intro.mov',
    ori=0.0, pos=(0.5, 0.35), opacity=None,
    loop=False,
    size=[0.4, 0.3],
    depth=0.0,
    )
text_4 = visual.TextStim(win=win, name='text_4',
    text="Other's nonverbal behavior",
    font='Times New Roman',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='Everyday interaction',
    font='Times New Roman',
    pos=(0, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()
PressSpace_4 = visual.TextStim(win=win, name='PressSpace_4',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Pic_1.jpg', mask=None,
    ori=0.0, pos=(0.5, 0.35), size=[0.4, 0.3],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "Consent1"
Consent1Clock = core.Clock()
Title_2 = visual.TextStim(win=win, name='Title_2',
    text='CONSENT TO PARTICIPATE IN The Nonverbal Behavior Study',
    font='Times New Roman',
    pos=(0, 0.4), height=0.04, wrapWidth=2.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Authors_2 = visual.TextStim(win=win, name='Authors_2',
    text='I understand that I am being asked by Andrea Salazar Parra and Dr. Michael Conway, both of the Psychology Department of Concordia University, Montreal, Quebec, Canada, to participate in a study.',
    font='Times New Roman',
    pos=(0, 0.3), height=0.025, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Purpose = visual.TextStim(win=win, name='Purpose',
    text='A. PURPOSE AND PROCEDURE\nThe purpose of the study is to get my impressions of a person based on a video of an everyday interaction. The study will take approximatley 9 minutes to complete. The study is for people 18 to 35 years of age who are proficient in English.',
    font='Times New Roman',
    pos=(0, 0.2), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Browser = visual.TextStim(win=win, name='Browser',
    text='You need to access the study with either the Google Chrome, Microsoft Edge, or Firefox web browser. This study only works with those browsers. Please also run the study in Full Screen mode. The study is set up that way.',
    font='Times New Roman',
    pos=(0, 0.1), height=0.025, wrapWidth=1.5, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Conditions = visual.TextStim(win=win, name='Conditions',
    text='B.CONDITIONS OF PARTICIPATION: I understand that…\n… my participation in this study is ANONYMOUS (i.e., I cannot be indentified).\n…it is my decision to participate. I am free to withdraw my consent and discontinue my participation at any time (by pressing the Escape key and closing the tab while completing the study) without negative consequences.\n…I will be asked to provide demographic information: my age and gender.\n…once I have completed the study, I cannot ask to have my responses withdrawn.\n…the data from this study may be published in aggregate form (i.e., averaged across many participants) in a scientific journal.\n...I will receive £1.20  for participating in this study.\n',
    font='Times New Roman',
    pos=(0, -0.07), height=0.025, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
emails = visual.TextStim(win=win, name='emails',
    text='If at any time you have questions about the research, please contact Dr. Michael Conway: conway.lab.concordia@gmail.com.\n\nIf at any time you have any questions about your rights as a research participant, please contact the Research Ethics Advisor at Concordia University: oor.ethics@concordia.ca. \n',
    font='Times New Roman',
    pos=(0, -0.25), height=0.025, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
PressYN = visual.TextStim(win=win, name='PressYN',
    text='Press ‘Y’ to  agree to continue or press ‘N’ to end the program.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
agree_or_disagree = keyboard.Keyboard()

# Initialize components for Routine "Consent2"
Consent2Clock = core.Clock()
response = visual.TextStim(win=win, name='response',
    text='',
    font='Times New Roman',
    pos=(0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PressSpace2 = visual.TextStim(win=win, name='PressSpace2',
    text='',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "AgeGender"
AgeGenderClock = core.Clock()
GenderPrompt = visual.TextStim(win=win, name='GenderPrompt',
    text='Please select your gender.',
    font='Times New Roman',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
gender = visual.Slider(win=win, name='gender',
    startValue=None, size=(0.3, .03), pos=(0, .2), units=None,
    labels=['male','female','other'], ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Times New Roman', labelHeight=0.035,
    flip=False, depth=-1, readOnly=False)
AgePrompt = visual.TextStim(win=win, name='AgePrompt',
    text='Type in your age (no need to place the cursor):',
    font='Times New Roman',
    pos=(-0.2, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
what_typed = visual.TextStim(win=win, name='what_typed',
    text='',
    font='Times New Roman',
    pos=(0.25, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
missing_info = visual.TextStim(win=win, name='missing_info',
    text='',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
press_space = visual.TextStim(win=win, name='press_space',
    text='',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
age = keyboard.Keyboard()
blank = visual.TextStim(win=win, name='blank',
    text='______ years',
    font='Times New Roman',
    pos=(0.3,-0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Now move the cursor to the bottom right corner of the screen (to get it out of the way).',
    font='Times New Roman',
    pos=(0, -0.25), height=0.035, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-10.0);

# Initialize components for Routine "Transition"
TransitionClock = core.Clock()
Text = visual.TextStim(win=win, name='Text',
    text='The researcher will now explain to you in more detail what you will be doing.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PressSpace_5 = visual.TextStim(win=win, name='PressSpace_5',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
image_1 = visual.ImageStim(
    win=win,
    name='image_1', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
PressSpace_2 = visual.TextStim(win=win, name='PressSpace_2',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pressSpace = keyboard.Keyboard()
movie_2 = visual.MovieStim3(
    win=win, name='movie_2',units='height', 
    noAudio = False,
    filename='Instruction.mov',
    ori=0.0, pos=(0.5, 0.35), opacity=None,
    loop=False,
    size=[0.4, 0.3],
    depth=-3.0,
    )
text_13 = visual.TextStim(win=win, name='text_13',
    text='Teammates',
    font='Times New Roman',
    pos=(0, 0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='in a competition that did not go well',
    font='Times New Roman',
    pos=(0, 0.3), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Skipped practice  ',
    font='Times New Roman',
    pos=(0.6, 0), height=0.035, wrapWidth=2.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='Partied the night before',
    font='Times New Roman',
    pos=(0.6, -0.05), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='"You really let us down”',
    font='Times New Roman',
    pos=(-0.6, 0), height=0.035, wrapWidth=2.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='Three times',
    font='Times New Roman',
    pos=(0, -0.3), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='Silent',
    font='Times New Roman',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Video1"
Video1Clock = core.Clock()

# Initialize components for Routine "VideoTransition"
VideoTransitionClock = core.Clock()
PressSpace_6 = visual.TextStim(win=win, name='PressSpace_6',
    text='Press the spacebar to watch the video again.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Video2"
Video2Clock = core.Clock()

# Initialize components for Routine "VideoTransition_2"
VideoTransition_2Clock = core.Clock()
PressSpace_7 = visual.TextStim(win=win, name='PressSpace_7',
    text='Press the spacebar to watch the video one last time.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Video3"
Video3Clock = core.Clock()

# Initialize components for Routine "VideoTransition_3"
VideoTransition_3Clock = core.Clock()
PressSpace_8 = visual.TextStim(win=win, name='PressSpace_8',
    text='Press the spacebar to report your imperssions.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "I1_O1"
I1_O1Clock = core.Clock()
Question = visual.TextStim(win=win, name='Question',
    text='Click the option on each scale that best represents your impression of the person on the right. If you are not sure, please guess.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1 = visual.TextStim(win=win, name='Q1',
    text='',
    font='Times New Roman',
    pos=(0, 0.38), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_6 = visual.Slider(win=win, name='slider_6',
    startValue=None, size=(1, 0.02), pos=(0, 0.35), units=None,
    labels=['1\nvery\ninnappropriate', '2\nquite\ninnappropriate', '3\nsomewhat\ninappropriate', '4\nslightly\nappropriate ', '5\nsomewhat\nappropriate', '6\nquite\nappropriate', '7\nvery\nappropriate'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q_2 = visual.TextStim(win=win, name='Q_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_7 = visual.Slider(win=win, name='slider_7',
    startValue=None, size=(1, 0.02), pos=(0, 0.2), units=None,
    labels=['1\nnot at all\nlikeable', '2\na little bit\nlikeable', '3\nsomewhat\nlikeable', '4\nmoderately\nlikeable', '5\nquite\nlikeable', '6\nvery\nlikeable', '7\nextremely\nlikeable'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q4 = visual.TextStim(win=win, name='Q4',
    text='',
    font='Times New Roman',
    pos=(0, 0.08), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_8 = visual.Slider(win=win, name='slider_8',
    startValue=None, size=(1, 0.02), pos=(0, 0.05), units=None,
    labels=['1\nthinks much\nworse of them', '2\nthinks worse\nof them', '3\nthinks a little\nworse of them', '4\nthinks the same\nas before', '5\nthinks a liitle\nbetter of them', '6\nthinks\nbetter of them', '7\nthinks much\nbetter of them'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q3 = visual.TextStim(win=win, name='Q3',
    text='',
    font='Times New Roman',
    pos=(0, -0.07), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_10 = visual.Slider(win=win, name='slider_10',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nnot at all\nupset', '2\na little bit\nupset', '3\nsomewhat\nupset', '4\nmoderately\nupset', '5\nquite\nupset', '6\nvery\nupset', '7\nextremely\nupset'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Q5 = visual.TextStim(win=win, name='Q5',
    text='',
    font='Times New Roman',
    pos=(0, -0.22), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_9 = visual.Slider(win=win, name='slider_9',
    startValue=None, size=(1, 0.02), pos=(0, -0.25), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Q6 = visual.TextStim(win=win, name='Q6',
    text='',
    font='Times New Roman',
    pos=(0, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_50 = visual.Slider(win=win, name='slider_50',
    startValue=None, size=(1, 0.02), pos=(0, -0.4), units=None,
    labels=['1\nnot at all bad', '2\na little bit bad', '3\nsomewhat bad', '4\nmoderately bad', '5\nquite bad', '6\nvery bad', '7\nextremely bad'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
pressSpace_4 = visual.TextStim(win=win, name='pressSpace_4',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
key_p_2 = keyboard.Keyboard()
message_2 = visual.TextStim(win=win, name='message_2',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "I2_O1"
I2_O1Clock = core.Clock()
Question_3 = visual.TextStim(win=win, name='Question_3',
    text='Click the option on each scale that best represents your impression. If you are not sure, please give your best guess.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_3 = visual.TextStim(win=win, name='Q1_3',
    text='',
    font='Times New Roman',
    pos=(0, 0.38), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_11 = visual.Slider(win=win, name='slider_11',
    startValue=None, size=(1, 0.02), pos=(0, 0.35), units=None,
    labels=['1\nnot at all bad', '2\na little bit bad', '3\nsomewhat bad', '4\nmoderately bad', '5\nquite bad', '6\nvery bad', '7\nextremely bad'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q = visual.TextStim(win=win, name='Q',
    text='',
    font='Times New Roman',
    pos=(0, 0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_12 = visual.Slider(win=win, name='slider_12',
    startValue=None, size=(1, 0.02), pos=(0, 0.2), units=None,
    labels=['1\nnot at all\nsurprised', '2\na little bit\nsurprised', '3\nsomewhat\nsurprised', '4\nmoderately\nsurprised', '5\nquite\nsurprised', '6\nvery\nsurprised', '7\nextremely\nsurprised'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q3_2 = visual.TextStim(win=win, name='Q3_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.08), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_13 = visual.Slider(win=win, name='slider_13',
    startValue=None, size=(1, 0.02), pos=(0, 0.05), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery much', '7\na lot'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q4_2 = visual.TextStim(win=win, name='Q4_2',
    text='',
    font='Times New Roman',
    pos=(0, -0.07), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_14 = visual.Slider(win=win, name='slider_14',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Q5_2 = visual.TextStim(win=win, name='Q5_2',
    text='',
    font='Times New Roman',
    pos=(0, -0.22), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_15 = visual.Slider(win=win, name='slider_15',
    startValue=None, size=(1, 0.02), pos=(0, -0.25), units=None,
    labels=['1\nnot at all\nserious', '2\na little bit\nserious', '3\nsomewhat\nserious', '4\nmoderately\nserious', '5\nquite\nserious', '6\nvery\nserious', '7\nextremely\nserious'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Q6_2 = visual.TextStim(win=win, name='Q6_2',
    text='',
    font='Times New Roman',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_61 = visual.Slider(win=win, name='slider_61',
    startValue=None, size=(1, 0.02), pos=(0, -0.38), units=None,
    labels=['1\nnot at all\ndamaged', '2\na little bit\ndamaged', '3\nsomewhat\ndamaged', '4\nmoderately\ndamaged', '5\nquite\ndamaged', '6\nvery\ndamaged', '7\nextremely\ndamaged'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
pressSpace_5 = visual.TextStim(win=win, name='pressSpace_5',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
key_p_3 = keyboard.Keyboard()
message_3 = visual.TextStim(win=win, name='message_3',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "I1_O2"
I1_O2Clock = core.Clock()
Question_4 = visual.TextStim(win=win, name='Question_4',
    text='Click the option on each scale that best represents your impression. If you are not sure, please guess.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_4 = visual.TextStim(win=win, name='Q1_4',
    text='',
    font='Times New Roman',
    pos=(0, 0.38), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_16 = visual.Slider(win=win, name='slider_16',
    startValue=None, size=(1, 0.02), pos=(0, 0.35), units=None,
    labels=['1\nnot at all\ndamaged', '2\na little bit\ndamaged', '3\nsomewhat\ndamaged', '4\nmoderately\ndamaged', '5\nquite\ndamaged', '6\nvery\ndamaged', '7\nextremely\ndamaged'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q_3 = visual.TextStim(win=win, name='Q_3',
    text='',
    font='Times New Roman',
    pos=(0, 0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_17 = visual.Slider(win=win, name='slider_17',
    startValue=None, size=(1, 0.02), pos=(0, 0.2), units=None,
    labels=['1\nnot at all\nserious', '2\na little bit\nserious', '3\nsomewhat\nserious', '4\nmoderately\nserious', '5\nquite\nserious', '6\nvery\nserious', '7\nextremely\nserious'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q3_3 = visual.TextStim(win=win, name='Q3_3',
    text='',
    font='Times New Roman',
    pos=(0, 0.08), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_18 = visual.Slider(win=win, name='slider_18',
    startValue=None, size=(1, 0.02), pos=(0, 0.05), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q4_3 = visual.TextStim(win=win, name='Q4_3',
    text='',
    font='Times New Roman',
    pos=(0, -0.07), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_19 = visual.Slider(win=win, name='slider_19',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery much', '7\na lot'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Q5_3 = visual.TextStim(win=win, name='Q5_3',
    text='',
    font='Times New Roman',
    pos=(0, -0.22), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_20 = visual.Slider(win=win, name='slider_20',
    startValue=None, size=(1, 0.02), pos=(0, -0.25), units=None,
    labels=['1\nnot at all\nsurprised', '2\na little bit\nsurprised', '3\nsomewhat\nsurprised', '4\nmoderately\nsurprised', '5\nquite\nsurprised', '6\nvery\nsurprised', '7\nextremely\nsurprised'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Q6_3 = visual.TextStim(win=win, name='Q6_3',
    text='',
    font='Times New Roman',
    pos=(0, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_62 = visual.Slider(win=win, name='slider_62',
    startValue=None, size=(1, 0.02), pos=(0, -0.4), units=None,
    labels=['1\nnot at all bad', '2\na little bit bad', '3\nsomewhat bad', '4\nmoderately bad', '5\nquite bad', '6\nvery bad', '7\nextremely bad'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
pressSpace_6 = visual.TextStim(win=win, name='pressSpace_6',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
key_p_4 = keyboard.Keyboard()
message_4 = visual.TextStim(win=win, name='message_4',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "I2_O2"
I2_O2Clock = core.Clock()
Question_5 = visual.TextStim(win=win, name='Question_5',
    text='Click the option on each scale that best represents your impression. If you are not sure, please give your best guess.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_5 = visual.TextStim(win=win, name='Q1_5',
    text='',
    font='Times New Roman',
    pos=(0, 0.38), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_33 = visual.Slider(win=win, name='slider_33',
    startValue=None, size=(1, 0.02), pos=(0, 0.35), units=None,
    labels=['1\nnot at all bad', '2\na little bit bad', '3\nsomewhat bad', '4\nmoderately bad', '5\nquite bad', '6\nvery bad', '7\nextremely bad'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q_4 = visual.TextStim(win=win, name='Q_4',
    text='',
    font='Times New Roman',
    pos=(0, 0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_34 = visual.Slider(win=win, name='slider_34',
    startValue=None, size=(1, 0.02), pos=(0, 0.2), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\nmoderately', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q3_4 = visual.TextStim(win=win, name='Q3_4',
    text='',
    font='Times New Roman',
    pos=(0, 0.08), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_35 = visual.Slider(win=win, name='slider_35',
    startValue=None, size=(1, 0.02), pos=(0, 0.05), units=None,
    labels=['1\nnot at all\nupset', '2\na little bit\nupset', '3\nsomewhat\nupset', '4\nmoderately\nupset', '5\nquite\nupset', '6\nvery\nupset', '7\nextremely\nupset'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q4_4 = visual.TextStim(win=win, name='Q4_4',
    text='',
    font='Times New Roman',
    pos=(0, -0.07), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_36 = visual.Slider(win=win, name='slider_36',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nthinks much\nworse of them', '2\nthinks worse\nof them', '3\nthinks a little\nworse of them', '4\nthinks the same\nas before', '5\nthinks a liitle\nbetter of them', '6\nthinks\nbetter of them', '7\nthinks much\nbetter of them'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Q5_4 = visual.TextStim(win=win, name='Q5_4',
    text='',
    font='Times New Roman',
    pos=(0, -0.22), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_37 = visual.Slider(win=win, name='slider_37',
    startValue=None, size=(1, 0.02), pos=(0, -0.25), units=None,
    labels=['1\nnot at all\nlikeable', '2\na little bit\nlikeable', '3\nsomewhat\nlikeable', '4\nmoderately\nlikeable', '5\nquite\nlikeable', '6\nvery\nlikeable', '7\nextremely\nlikeable'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Q6_4 = visual.TextStim(win=win, name='Q6_4',
    text='',
    font='Times New Roman',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_63 = visual.Slider(win=win, name='slider_63',
    startValue=None, size=(1, 0.02), pos=(0, -0.38), units=None,
    labels=['1\nvery\ninnappropriate', '2\nquite\ninnappropriate', '3\nsomewhat\ninappropriate', '4\nslightly\nappropriate ', '5\nsomewhat\nappropriate', '6\nquite\nappropriate', '7\nvery\nappropriate'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
pressSpace_9 = visual.TextStim(win=win, name='pressSpace_9',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
key_p_7 = keyboard.Keyboard()
message_5 = visual.TextStim(win=win, name='message_5',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "E1_O1"
E1_O1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feelQ = visual.TextStim(win=win, name='feelQ',
    text='My impression is that the person on the right feels…',
    font='Times New Roman',
    pos=(0, 0.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Angry = visual.TextStim(win=win, name='Angry',
    text='Angry',
    font='Times New Roman',
    pos=(-0.6, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.25), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-3, readOnly=False)
Bored = visual.TextStim(win=win, name='Bored',
    text='Bored',
    font='Times New Roman',
    pos=(-0.6, 0.01), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.01), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-5, readOnly=False)
Sad = visual.TextStim(win=win, name='Sad',
    text='Sad',
    font='Times New Roman',
    pos=(-0.6, 0.13), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
slider_h = visual.Slider(win=win, name='slider_h',
    startValue=None, size=(1, .02), pos=(0.1, 0.13), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-7, readOnly=False)
Embarrassed = visual.TextStim(win=win, name='Embarrassed',
    text='Embarrassed',
    font='Times New Roman',
    pos=(-0.6, -0.11), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
slider_3 = visual.Slider(win=win, name='slider_3',
    startValue=None, size=(1, .02), pos=(0.1, -0.11), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-9, readOnly=False)
Disgusted = visual.TextStim(win=win, name='Disgusted',
    text='Disgusted',
    font='Times New Roman',
    pos=(-0.6, -0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
slider_4 = visual.Slider(win=win, name='slider_4',
    startValue=None, size=(1, .02), pos=(0.1, -0.23), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-11, readOnly=False)
Shy = visual.TextStim(win=win, name='Shy',
    text='Shy',
    font='Times New Roman',
    pos=(-0.6, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
slider_5 = visual.Slider(win=win, name='slider_5',
    startValue=None, size=(1, .02), pos=(0.1, -0.35), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-13, readOnly=False)
pressSpace_3 = visual.TextStim(win=win, name='pressSpace_3',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
key_p = keyboard.Keyboard()
message = visual.TextStim(win=win, name='message',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);

# Initialize components for Routine "E2_O1"
E2_O1Clock = core.Clock()
feelQ_2 = visual.TextStim(win=win, name='feelQ_2',
    text='My impression is that the person on the right feels…',
    font='Times New Roman',
    pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Uninterested_1 = visual.TextStim(win=win, name='Uninterested_1',
    text='Uninterested',
    font='Times New Roman',
    pos=(-0.6, 0.37), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_39 = visual.Slider(win=win, name='slider_39',
    startValue=None, size=(1, .02), pos=(0.1, 0.37), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Unhappy = visual.TextStim(win=win, name='Unhappy',
    text='Unhappy',
    font='Times New Roman',
    pos=(-0.6, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_21 = visual.Slider(win=win, name='slider_21',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.25), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Anxious_3 = visual.TextStim(win=win, name='Anxious_3',
    text='Anxious',
    font='Times New Roman',
    pos=(-0.6, 0.01), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_22 = visual.Slider(win=win, name='slider_22',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.01), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Tired_3 = visual.TextStim(win=win, name='Tired_3',
    text='Tired',
    font='Times New Roman',
    pos=(-0.6, 0.13), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_26 = visual.Slider(win=win, name='slider_26',
    startValue=None, size=(1, .02), pos=(0.1, 0.13), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Ashamed_3 = visual.TextStim(win=win, name='Ashamed_3',
    text='Ashamed',
    font='Times New Roman',
    pos=(-0.6, -0.11), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_23 = visual.Slider(win=win, name='slider_23',
    startValue=None, size=(1, .02), pos=(0.1, -0.11), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Fearful_3 = visual.TextStim(win=win, name='Fearful_3',
    text='Fearful',
    font='Times New Roman',
    pos=(-0.6, -0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_24 = visual.Slider(win=win, name='slider_24',
    startValue=None, size=(1, .02), pos=(0.1, -0.23), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
Guilty_3 = visual.TextStim(win=win, name='Guilty_3',
    text='Guilty',
    font='Times New Roman',
    pos=(-0.6, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
slider_25 = visual.Slider(win=win, name='slider_25',
    startValue=None, size=(1, .02), pos=(0.1, -0.35), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-14, readOnly=False)
pressSpace_7 = visual.TextStim(win=win, name='pressSpace_7',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
key_p_5 = keyboard.Keyboard()
message_6 = visual.TextStim(win=win, name='message_6',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# Initialize components for Routine "E1_O2"
E1_O2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feelQ_3 = visual.TextStim(win=win, name='feelQ_3',
    text='My impression is that the person on the right feels…',
    font='Times New Roman',
    pos=(0, 0.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Guilty_5 = visual.TextStim(win=win, name='Guilty_5',
    text='Guilty',
    font='Times New Roman',
    pos=(-0.6, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider_27 = visual.Slider(win=win, name='slider_27',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.25), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-3, readOnly=False)
Fearful_4 = visual.TextStim(win=win, name='Fearful_4',
    text='Fearful',
    font='Times New Roman',
    pos=(-0.6, 0.01), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
slider_28 = visual.Slider(win=win, name='slider_28',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.01), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-5, readOnly=False)
Ashamed_5 = visual.TextStim(win=win, name='Ashamed_5',
    text='Ashamed',
    font='Times New Roman',
    pos=(-0.6, 0.13), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
slider_32 = visual.Slider(win=win, name='slider_32',
    startValue=None, size=(1, .02), pos=(0.1, 0.13), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-7, readOnly=False)
Tired_6 = visual.TextStim(win=win, name='Tired_6',
    text='Tired',
    font='Times New Roman',
    pos=(-0.6, -0.11), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
slider_29 = visual.Slider(win=win, name='slider_29',
    startValue=None, size=(1, .02), pos=(0.1, -0.11), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-9, readOnly=False)
Anxious_4 = visual.TextStim(win=win, name='Anxious_4',
    text='Anxious',
    font='Times New Roman',
    pos=(-0.6, -0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
slider_30 = visual.Slider(win=win, name='slider_30',
    startValue=None, size=(1, .02), pos=(0.1, -0.23), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-11, readOnly=False)
Unhappy_4 = visual.TextStim(win=win, name='Unhappy_4',
    text='Unhappy',
    font='Times New Roman',
    pos=(-0.6, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
slider_31 = visual.Slider(win=win, name='slider_31',
    startValue=None, size=(1, .02), pos=(0.1, -0.35), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-13, readOnly=False)
pressSpace_8 = visual.TextStim(win=win, name='pressSpace_8',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
key_p_6 = keyboard.Keyboard()
message_7 = visual.TextStim(win=win, name='message_7',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);

# Initialize components for Routine "E2_O2"
E2_O2Clock = core.Clock()
feelQ_5 = visual.TextStim(win=win, name='feelQ_5',
    text='My impression is that the person on the right feels…',
    font='Times New Roman',
    pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Shy_5 = visual.TextStim(win=win, name='Shy_5',
    text='Shy',
    font='Times New Roman',
    pos=(-0.6, 0.37), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_46 = visual.Slider(win=win, name='slider_46',
    startValue=None, size=(1, .02), pos=(0.1, 0.37), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Disgusted_5 = visual.TextStim(win=win, name='Disgusted_5',
    text='Disgusted',
    font='Times New Roman',
    pos=(-0.6, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_40 = visual.Slider(win=win, name='slider_40',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.25), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Embarrassed_6 = visual.TextStim(win=win, name='Embarrassed_6',
    text='Embarrassed',
    font='Times New Roman',
    pos=(-0.6, 0.01), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_41 = visual.Slider(win=win, name='slider_41',
    startValue=None, size=(1, 0.02), pos=(0.1, 0.01), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Sad_6 = visual.TextStim(win=win, name='Sad_6',
    text='Sad',
    font='Times New Roman',
    pos=(-0.6, 0.13), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_42 = visual.Slider(win=win, name='slider_42',
    startValue=None, size=(1, .02), pos=(0.1, 0.13), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
Bored_6 = visual.TextStim(win=win, name='Bored_6',
    text='Bored',
    font='Times New Roman',
    pos=(-0.6, -0.11), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
slider_43 = visual.Slider(win=win, name='slider_43',
    startValue=None, size=(1, .02), pos=(0.1, -0.11), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-10, readOnly=False)
Angry_6 = visual.TextStim(win=win, name='Angry_6',
    text='Angry',
    font='Times New Roman',
    pos=(-0.6, -0.23), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
slider_44 = visual.Slider(win=win, name='slider_44',
    startValue=None, size=(1, .02), pos=(0.1, -0.23), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-12, readOnly=False)
Uninterested_6 = visual.TextStim(win=win, name='Uninterested_6',
    text='Uninterested',
    font='Times New Roman',
    pos=(-0.6, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
slider_45 = visual.Slider(win=win, name='slider_45',
    startValue=None, size=(1, .02), pos=(0.1, -0.35), units=None,
    labels=['1\nnot at all', '2\na little bit', '3\nsomewhat', '4\n ', '5\nquite', '6\nvery much', '7\nextremely'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-14, readOnly=False)
pressSpace_10 = visual.TextStim(win=win, name='pressSpace_10',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
key_p_8 = keyboard.Keyboard()
message_9 = visual.TextStim(win=win, name='message_9',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# Initialize components for Routine "P1_O1"
P1_O1Clock = core.Clock()
Question_6 = visual.TextStim(win=win, name='Question_6',
    text='Please describe what you think of the video.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_6 = visual.TextStim(win=win, name='Q1_6',
    text='Do you agree that this type of situation can occur in people’s lives? ',
    font='Times New Roman',
    pos=(0, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_38 = visual.Slider(win=win, name='slider_38',
    startValue=None, size=(1, 0.02), pos=(0, 0.3), units=None,
    labels=['1\nstrongly\ndisagree', '2\ndisagree', '3\nsomewhat\ndisagree', '4\n ', '5\nsomewhat\nagree', '6\nagree', '7\nstrongly\nagree'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q_5 = visual.TextStim(win=win, name='Q_5',
    text='How often do you think this type of situation might occur in people’s lives?',
    font='Times New Roman',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_47 = visual.Slider(win=win, name='slider_47',
    startValue=None, size=(1, 0.02), pos=(0, 0.1), units=None,
    labels=['1\nnever', '2\nrarely', '3\nsometimes', '4\n ', '5\noften', '6\nfrequently', '7\nall the time'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q3_5 = visual.TextStim(win=win, name='Q3_5',
    text='Given what the person was told, how plausible and realistic was the reaction you saw? ',
    font='Times New Roman',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_48 = visual.Slider(win=win, name='slider_48',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nextremely\nimplausible', '2\nvery\nimplausible', '3\nsomewhat\nimplausible', '4\n ', '5\nsomewhat\nplausible', '6\nvery\nplausible', '7\nextremely\nplausible'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q4_5 = visual.TextStim(win=win, name='Q4_5',
    text='Given what the person was told, how normal and natural was the reaction you saw?   ',
    font='Times New Roman',
    pos=(0, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_49 = visual.Slider(win=win, name='slider_49',
    startValue=None, size=(1, 0.02), pos=(0, -0.3), units=None,
    labels=['1\nnot at all normal', '2\na little normal', '3\nsomewhat normal', '4\n ', '5\nquite normal', '6\nvery normal', '7\ncompletely normal'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
pressSpace_11 = visual.TextStim(win=win, name='pressSpace_11',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
key_p_9 = keyboard.Keyboard()
message_8 = visual.TextStim(win=win, name='message_8',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "P1_O2"
P1_O2Clock = core.Clock()
Question_8 = visual.TextStim(win=win, name='Question_8',
    text='Please describe what you think of the video.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1_7 = visual.TextStim(win=win, name='Q1_7',
    text='Given what the person was told, how normal and natural was the reaction you saw? ',
    font='Times New Roman',
    pos=(0, 0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_51 = visual.Slider(win=win, name='slider_51',
    startValue=None, size=(1, 0.02), pos=(0, 0.3), units=None,
    labels=['1\nnot at all normal', '2\na little normal', '3\nsomewhat normal', '4\n ', '5\nquite normal', '6\nvery normal', '7\ncompletely normal'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-2, readOnly=False)
Q_6 = visual.TextStim(win=win, name='Q_6',
    text='Given what the person was told, how plausible and realistic was the reaction you saw? ',
    font='Times New Roman',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_52 = visual.Slider(win=win, name='slider_52',
    startValue=None, size=(1, 0.02), pos=(0, 0.1), units=None,
    labels=['1\nextremely\nimplausible', '2\nvery\nimplausible', '3\nsomewhat\nimplausible', '4\n ', '5\nsomewhat\nplausible', '6\nvery\nplausible', '7\nextremely\nplausible'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-4, readOnly=False)
Q3_6 = visual.TextStim(win=win, name='Q3_6',
    text='How often do you think this type of situation might occur in people’s lives?',
    font='Times New Roman',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
slider_53 = visual.Slider(win=win, name='slider_53',
    startValue=None, size=(1, 0.02), pos=(0, -0.1), units=None,
    labels=['1\nextremely\nimplausible', '2\nvery\nimplausible', '3\nsomewhat\nimplausible', '4\n ', '5\nsomewhat\nplausible', '6\nvery\nplausible', '7\nexteremely\nplausible'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-6, readOnly=False)
Q4_6 = visual.TextStim(win=win, name='Q4_6',
    text='Do you agree that this type of situation can occur in people’s lives? ',
    font='Times New Roman',
    pos=(0, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider_54 = visual.Slider(win=win, name='slider_54',
    startValue=None, size=(1, 0.02), pos=(0, -0.3), units=None,
    labels=['1\nstrongly\ndisagree', '2\ndisagree', '3\nsomewhat\ndisagree', '4\n ', '5\nsomewhat\nagree', '6\nagree', '7\nstrongly\nagree'], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, depth=-8, readOnly=False)
pressSpace_12 = visual.TextStim(win=win, name='pressSpace_12',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
key_p_10 = keyboard.Keyboard()
message_10 = visual.TextStim(win=win, name='message_10',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "C1_O1"
C1_O1Clock = core.Clock()
Question_9 = visual.TextStim(win=win, name='Question_9',
    text='On this page, please answer the following questions.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q_7 = visual.TextStim(win=win, name='Q_7',
    text='Was the person in the video a woman or a man?',
    font='Times New Roman',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_56 = visual.Slider(win=win, name='slider_56',
    startValue=None, size=(0.025, 0.03), pos=(-0.5, 0.15), units=None,
    labels=['Woman', 'Man'], ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=True, depth=-2, readOnly=False)
Q3_7 = visual.TextStim(win=win, name='Q3_7',
    text='3: What did the researcher tell you about what was going on in the video? Choose one. ',
    font='Times New Roman',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_57 = visual.Slider(win=win, name='slider_57',
    startValue=None, size=(0.025, 0.09), pos=(-0.5, -0.15), units=None,
    labels=['The person on the left told the person on the right that they did something good', 'The person on the left told the person on the right that they did did something bad', 'The person on the right told the person on the left that they did something good', 'The person on right told the person on the left that they did something bad'], ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=True, depth=-4, readOnly=False)
pressSpace_13 = visual.TextStim(win=win, name='pressSpace_13',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_p_11 = keyboard.Keyboard()
message_11 = visual.TextStim(win=win, name='message_11',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "C1_O2"
C1_O2Clock = core.Clock()
Question_10 = visual.TextStim(win=win, name='Question_10',
    text='On this page, please answer the following questions.',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q_8 = visual.TextStim(win=win, name='Q_8',
    text='2: What did the researcher tell you about what was going on in the video? Choose one. ',
    font='Times New Roman',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_59 = visual.Slider(win=win, name='slider_59',
    startValue=None, size=(0.025, 0.09), pos=(-0.5, 0.15), units=None,
    labels=['The person on the left told the person on the right that they did something good', 'The person on the left told the person on the right that they did did something bad', 'The person on the right told the person on the left that they did something good', 'The person on right told the person on the left that they did something bad'], ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=True, depth=-2, readOnly=False)
Q3_8 = visual.TextStim(win=win, name='Q3_8',
    text='3: Was the person in the video a woman or a man?',
    font='Times New Roman',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
slider_60 = visual.Slider(win=win, name='slider_60',
    startValue=None, size=(0.025, 0.03), pos=(-0.5, -0.15), units=None,
    labels=['Woman', 'Man'], ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='black', fillColor='white', borderColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=True, depth=-4, readOnly=False)
pressSpace_14 = visual.TextStim(win=win, name='pressSpace_14',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_p_12 = keyboard.Keyboard()
message_12 = visual.TextStim(win=win, name='message_12',
    text='',
    font='Times New Roman',
    pos=(0, -0.48), height=0.03, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for participating in this study. \n\nPlease wait while the program shuts down.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TitlePage"-------
continueRoutine = True
# update component parameters for each repeat
# ASSIGNING IMAGES AND ORDER
participant=int(expInfo['participant'])

if participant==1 or participant==10 or participant==18 or participant==29 or participant==40 or participant==48 or participant==56 or participant==60 or participant==71 or participant==76 or participant==85 or participant==96 or participant==101 or participant==111 or participant==116 or participant==124 or participant==135 or participant==140 or participant==151 or participant==153:
    image=1
    video=1
    order=1
    qtext=1
elif participant==7 or participant==16 or participant==22 or participant==25 or participant==35 or participant==44 or participant==49 or participant==63 or participant==68 or participant==80 or participant==84 or participant==92 or participant==97 or participant==107 or participant==117 or participant==127 or participant==129 or participant==142 or participant==148 or participant==159:
    image=1
    video=1
    order=2
    qtext=1
elif participant==4 or participant==12 or participant==19 or participant==30 or participant==36 or participant==47 or participant==55 or participant==62 or participant==65 or participant==75 or participant==82 or participant==89 or participant==103 or participant==105 or participant==113 or participant==128 or participant==134 or participant==137 or participant==149 or participant==158:
    image=1
    video=2
    order=1
    qtext=1
elif participant==6 or participant==14 or participant==23 or participant==26 or participant==38 or participant==42 or participant==51 or participant==58 or participant==70 or participant==78 or participant==88 or participant==94 or participant==100 or participant==110 or participant==118 or participant==121 or participant==131 or participant==144 or participant==146 or participant==154:
    image=1
    video=2
    order=2
    qtext=1
elif participant==3 or participant==15 or participant==21 or participant==32 or participant==37 or participant==45 or participant==50 or participant==64 or participant==67 or participant==74 or participant==83 or participant==90 or participant==99 or participant==108 or participant==114 or participant==122 or participant==133 or participant==139 or participant==147 or participant==160:
    image=2
    video=3
    order=1
    qtext=2
elif participant==8 or participant==11 or participant==17 or participant==27 or participant==33 or participant==41 or participant==54 or participant==59 or participant==69 or participant==77 or participant==87 or participant==95 or participant==104 or participant==112 or participant==120 or participant==126 or participant==132 or participant==143 or participant==152 or participant==155:
    image=2
    video=3
    order=2
    qtext=2
elif participant==2 or participant==9 or participant==20 or participant==28 or participant==34 or participant==43 or participant==52 or participant==61 or participant==72 or participant==79 or participant==86 or participant==91 or participant==98 or participant==106 or participant==119 or participant==125 or participant==136 or participant==141 or participant==145 or participant==156:
    image=2
    video=4
    order=1
    qtext=2
elif participant==5 or participant==13 or participant==24 or participant==31 or participant==39 or participant==46 or participant==53 or participant==57 or participant==66 or participant==73 or participant==81 or participant==93 or participant==102 or participant==109 or participant==115 or participant==123 or participant==130 or participant==138 or participant==150 or participant==157:
    image=2
    video=4
    order=2
    qtext=2


# put filenames of videos here
video_files = ['Video1_FemaleFast.mp4', 'Video2_FemaleSlow.mp4', 'Video3_MaleFast.mp4', 'Video4_MaleSlow.mp4']
image_files = ['Image1_Female.jpg', 'Image2_Male.jpg']

# put durations of videos here (in same order as in video_files list)
durations_s = [4, 9, 3, 8]

# chooses which video is played
video_played = video_files[video-1]
video_duration=durations_s[video-1]

image_shown = image_files[image-1]



key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
TitlePageComponents = [Title, Authors, PressSpace, key_resp, text_10]
for thisComponent in TitlePageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TitlePageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TitlePage"-------
while continueRoutine:
    # get current time
    t = TitlePageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TitlePageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Title* updates
    if Title.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Title.frameNStart = frameN  # exact frame index
        Title.tStart = t  # local t and not account for scr refresh
        Title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Title, 'tStartRefresh')  # time at next scr refresh
        Title.setAutoDraw(True)
    
    # *Authors* updates
    if Authors.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Authors.frameNStart = frameN  # exact frame index
        Authors.tStart = t  # local t and not account for scr refresh
        Authors.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Authors, 'tStartRefresh')  # time at next scr refresh
        Authors.setAutoDraw(True)
    
    # *PressSpace* updates
    if PressSpace.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        PressSpace.frameNStart = frameN  # exact frame index
        PressSpace.tStart = t  # local t and not account for scr refresh
        PressSpace.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressSpace, 'tStartRefresh')  # time at next scr refresh
        PressSpace.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TitlePageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TitlePage"-------
for thisComponent in TitlePageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Title.started', Title.tStartRefresh)
thisExp.addData('Title.stopped', Title.tStopRefresh)
thisExp.addData('Authors.started', Authors.tStartRefresh)
thisExp.addData('Authors.stopped', Authors.tStopRefresh)
thisExp.addData('PressSpace.started', PressSpace.tStartRefresh)
thisExp.addData('PressSpace.stopped', PressSpace.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroVid"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
IntroVidComponents = [movie, text_4, text_6, key_resp_4, PressSpace_4, image]
for thisComponent in IntroVidComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroVidClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroVid"-------
while continueRoutine:
    # get current time
    t = IntroVidClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroVidClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 13.5-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *PressSpace_4* updates
    if PressSpace_4.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        PressSpace_4.frameNStart = frameN  # exact frame index
        PressSpace_4.tStart = t  # local t and not account for scr refresh
        PressSpace_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressSpace_4, 'tStartRefresh')  # time at next scr refresh
        PressSpace_4.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroVidComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroVid"-------
for thisComponent in IntroVidComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PressSpace_4.started', PressSpace_4.tStartRefresh)
thisExp.addData('PressSpace_4.stopped', PressSpace_4.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "IntroVid" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Consent1"-------
continueRoutine = True
# update component parameters for each repeat
agree_or_disagree.keys = []
agree_or_disagree.rt = []
_agree_or_disagree_allKeys = []
# keep track of which components have finished
Consent1Components = [Title_2, Authors_2, Purpose, Browser, Conditions, emails, PressYN, agree_or_disagree]
for thisComponent in Consent1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Consent1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent1"-------
while continueRoutine:
    # get current time
    t = Consent1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Consent1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Title_2* updates
    if Title_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Title_2.frameNStart = frameN  # exact frame index
        Title_2.tStart = t  # local t and not account for scr refresh
        Title_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Title_2, 'tStartRefresh')  # time at next scr refresh
        Title_2.setAutoDraw(True)
    
    # *Authors_2* updates
    if Authors_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Authors_2.frameNStart = frameN  # exact frame index
        Authors_2.tStart = t  # local t and not account for scr refresh
        Authors_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Authors_2, 'tStartRefresh')  # time at next scr refresh
        Authors_2.setAutoDraw(True)
    
    # *Purpose* updates
    if Purpose.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Purpose.frameNStart = frameN  # exact frame index
        Purpose.tStart = t  # local t and not account for scr refresh
        Purpose.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Purpose, 'tStartRefresh')  # time at next scr refresh
        Purpose.setAutoDraw(True)
    
    # *Browser* updates
    if Browser.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Browser.frameNStart = frameN  # exact frame index
        Browser.tStart = t  # local t and not account for scr refresh
        Browser.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Browser, 'tStartRefresh')  # time at next scr refresh
        Browser.setAutoDraw(True)
    
    # *Conditions* updates
    if Conditions.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Conditions.frameNStart = frameN  # exact frame index
        Conditions.tStart = t  # local t and not account for scr refresh
        Conditions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Conditions, 'tStartRefresh')  # time at next scr refresh
        Conditions.setAutoDraw(True)
    
    # *emails* updates
    if emails.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        emails.frameNStart = frameN  # exact frame index
        emails.tStart = t  # local t and not account for scr refresh
        emails.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(emails, 'tStartRefresh')  # time at next scr refresh
        emails.setAutoDraw(True)
    
    # *PressYN* updates
    if PressYN.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        PressYN.frameNStart = frameN  # exact frame index
        PressYN.tStart = t  # local t and not account for scr refresh
        PressYN.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressYN, 'tStartRefresh')  # time at next scr refresh
        PressYN.setAutoDraw(True)
    
    # *agree_or_disagree* updates
    waitOnFlip = False
    if agree_or_disagree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        agree_or_disagree.frameNStart = frameN  # exact frame index
        agree_or_disagree.tStart = t  # local t and not account for scr refresh
        agree_or_disagree.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(agree_or_disagree, 'tStartRefresh')  # time at next scr refresh
        agree_or_disagree.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(agree_or_disagree.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(agree_or_disagree.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if agree_or_disagree.status == STARTED and not waitOnFlip:
        theseKeys = agree_or_disagree.getKeys(keyList=['y', 'n'], waitRelease=False)
        _agree_or_disagree_allKeys.extend(theseKeys)
        if len(_agree_or_disagree_allKeys):
            agree_or_disagree.keys = _agree_or_disagree_allKeys[-1].name  # just the last key pressed
            agree_or_disagree.rt = _agree_or_disagree_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Consent1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent1"-------
for thisComponent in Consent1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Title_2.started', Title_2.tStartRefresh)
thisExp.addData('Title_2.stopped', Title_2.tStopRefresh)
thisExp.addData('Authors_2.started', Authors_2.tStartRefresh)
thisExp.addData('Authors_2.stopped', Authors_2.tStopRefresh)
thisExp.addData('Purpose.started', Purpose.tStartRefresh)
thisExp.addData('Purpose.stopped', Purpose.tStopRefresh)
thisExp.addData('Browser.started', Browser.tStartRefresh)
thisExp.addData('Browser.stopped', Browser.tStopRefresh)
thisExp.addData('Conditions.started', Conditions.tStartRefresh)
thisExp.addData('Conditions.stopped', Conditions.tStopRefresh)
thisExp.addData('emails.started', emails.tStartRefresh)
thisExp.addData('emails.stopped', emails.tStopRefresh)
thisExp.addData('PressYN.started', PressYN.tStartRefresh)
thisExp.addData('PressYN.stopped', PressYN.tStopRefresh)
# check responses
if agree_or_disagree.keys in ['', [], None]:  # No response was made
    agree_or_disagree.keys = None
thisExp.addData('agree_or_disagree.keys',agree_or_disagree.keys)
if agree_or_disagree.keys != None:  # we had a response
    thisExp.addData('agree_or_disagree.rt', agree_or_disagree.rt)
thisExp.addData('agree_or_disagree.started', agree_or_disagree.tStartRefresh)
thisExp.addData('agree_or_disagree.stopped', agree_or_disagree.tStopRefresh)
thisExp.nextEntry()
# the Routine "Consent1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Consent2"-------
continueRoutine = True
# update component parameters for each repeat
# the text for 'response' text component
msg = ""

# the text for 'press_space_continue' component
space = ''

consent = True



# if they agree (if they pressed 'y')
if agree_or_disagree.keys == "y":
    
    # they continue with the study
    msg = "Thank you for agreeing to participate. Please answer a few questions about yourself."
    space = "Press the spacebar to continue."
    # consent is still True at the end


# if they disagree (if they pressed 'n')
elif agree_or_disagree.keys == "n":
    
    # the study will end here
    msg = "Thank you for your time."
    space = "Press the spacebar to quit the program."
    consent = False
    # if consent is False, then
    # quit program at the 'End 
    # Routine' tab.
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Consent2Components = [response, PressSpace2, key_resp_2]
for thisComponent in Consent2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Consent2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent2"-------
while continueRoutine:
    # get current time
    t = Consent2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Consent2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *response* updates
    if response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        response.frameNStart = frameN  # exact frame index
        response.tStart = t  # local t and not account for scr refresh
        response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
        response.setAutoDraw(True)
    if response.status == STARTED:  # only update if drawing
        response.setText(msg, log=False)
    
    # *PressSpace2* updates
    if PressSpace2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        PressSpace2.frameNStart = frameN  # exact frame index
        PressSpace2.tStart = t  # local t and not account for scr refresh
        PressSpace2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressSpace2, 'tStartRefresh')  # time at next scr refresh
        PressSpace2.setAutoDraw(True)
    if PressSpace2.status == STARTED:  # only update if drawing
        PressSpace2.setText(space, log=False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Consent2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent2"-------
for thisComponent in Consent2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if consent==False:
    quit()
thisExp.addData('response.started', response.tStartRefresh)
thisExp.addData('response.stopped', response.tStopRefresh)
thisExp.addData('PressSpace2.started', PressSpace2.tStartRefresh)
thisExp.addData('PressSpace2.stopped', PressSpace2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Consent2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AgeGender"-------
    continueRoutine = True
    # update component parameters for each repeat
    gender.reset()
    # list of numbers typed
    resp = []
    
    # what will appear on the screen (a readable version of resp)
    # the text in 'what_typed' text component
    screenText = ''
    
    # if age or gender is not filled in
    # the text in 'missing_info' text component
    ohnotext = ''
    
    # the text in 'pressSpace' text component
    press_space_text = 'Press the spacebar to continue.'
    
    # record of how many keys have been pressed
    number_keys = 0
    age.keys = []
    age.rt = []
    _age_allKeys = []
    # keep track of which components have finished
    AgeGenderComponents = [GenderPrompt, gender, AgePrompt, what_typed, missing_info, press_space, age, blank, text_7]
    for thisComponent in AgeGenderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AgeGenderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AgeGender"-------
    while continueRoutine:
        # get current time
        t = AgeGenderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AgeGenderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GenderPrompt* updates
        if GenderPrompt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            GenderPrompt.frameNStart = frameN  # exact frame index
            GenderPrompt.tStart = t  # local t and not account for scr refresh
            GenderPrompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GenderPrompt, 'tStartRefresh')  # time at next scr refresh
            GenderPrompt.setAutoDraw(True)
        
        # *gender* updates
        if gender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gender.frameNStart = frameN  # exact frame index
            gender.tStart = t  # local t and not account for scr refresh
            gender.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gender, 'tStartRefresh')  # time at next scr refresh
            gender.setAutoDraw(True)
        
        # *AgePrompt* updates
        if AgePrompt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AgePrompt.frameNStart = frameN  # exact frame index
            AgePrompt.tStart = t  # local t and not account for scr refresh
            AgePrompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgePrompt, 'tStartRefresh')  # time at next scr refresh
            AgePrompt.setAutoDraw(True)
        
        # *what_typed* updates
        if what_typed.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            what_typed.frameNStart = frameN  # exact frame index
            what_typed.tStart = t  # local t and not account for scr refresh
            what_typed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(what_typed, 'tStartRefresh')  # time at next scr refresh
            what_typed.setAutoDraw(True)
        if what_typed.status == STARTED:  # only update if drawing
            what_typed.setText(screenText, log=False)
        
        # *missing_info* updates
        if missing_info.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            missing_info.frameNStart = frameN  # exact frame index
            missing_info.tStart = t  # local t and not account for scr refresh
            missing_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(missing_info, 'tStartRefresh')  # time at next scr refresh
            missing_info.setAutoDraw(True)
        if missing_info.status == STARTED:  # only update if drawing
            missing_info.setText(ohnotext, log=False)
        
        # *press_space* updates
        if press_space.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            press_space.frameNStart = frameN  # exact frame index
            press_space.tStart = t  # local t and not account for scr refresh
            press_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_space, 'tStartRefresh')  # time at next scr refresh
            press_space.setAutoDraw(True)
        if press_space.status == STARTED:  # only update if drawing
            press_space.setText(press_space_text, log=False)
        # for testing:
        # print(age.keys, number_keys)
        if age.keys:
            # if a key press has been detected
            if len(age.keys) > number_keys:
                
                # update the number of keys pressed
                number_keys += 1
                
                # if the key pressed was 'backspace'
                if age.keys[-1] == "backspace":
                    
                    # if there are more than 0 numbers already written
                    if (len(resp) > 0):
                        
                        # remove the last character that was typed 
                        # (like backspace usually does)
                        #DOESNT NEED TO BE CHANGED IN JAVASCRIPT
                        resp.pop()
                        
                        
                        
                        # =resp.join("") IN JAVASCRIPT
                        # make resp nice to put it on the screen
                        screenText="".join(resp)
                
                # if the key pressed was 'space' 
                # (if the participant wants to continue)
                elif age.keys[-1] == 'space':
                    
                    # if there is missing information (either age or gender)
                    # if resp==[]... originally
                    if screenText=='' or not gender.getRating():
                        
                        # new text will appear asking them to fill in everything
                        ohnotext = "Please enter all requested information, then press the spacebar."
                        press_space_text = ''
                    
                    # if there is no missing information
                    else:
                        # end this routine and go to the next one
                        continueRoutine = False
                
                # if the key pressed was anything else
                # (a number in this case)
                else:
                    # add this number to 'resp' (since it was typed)
                    
                    #CHANGE THIS TO resp.push(...) IN JAVASCRIPT
                    resp.append(age.keys[-1])
                    
                    
                    
                    #TRYING =resp.join("") IN JAVASCRIPT
                    # update the text that will appear on screen
                    screenText="".join(resp)
                    
                    
        
        # *age* updates
        waitOnFlip = False
        if age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            age.frameNStart = frameN  # exact frame index
            age.tStart = t  # local t and not account for scr refresh
            age.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age, 'tStartRefresh')  # time at next scr refresh
            age.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(age.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(age.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if age.status == STARTED and not waitOnFlip:
            theseKeys = age.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'backspace', 'space'], waitRelease=False)
            _age_allKeys.extend(theseKeys)
            if len(_age_allKeys):
                age.keys = [key.name for key in _age_allKeys]  # storing all keys
                age.rt = [key.rt for key in _age_allKeys]
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AgeGenderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AgeGender"-------
    for thisComponent in AgeGenderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('GenderPrompt.started', GenderPrompt.tStartRefresh)
    trials.addData('GenderPrompt.stopped', GenderPrompt.tStopRefresh)
    trials.addData('gender.response', gender.getRating())
    trials.addData('gender.rt', gender.getRT())
    trials.addData('gender.started', gender.tStartRefresh)
    trials.addData('gender.stopped', gender.tStopRefresh)
    trials.addData('AgePrompt.started', AgePrompt.tStartRefresh)
    trials.addData('AgePrompt.stopped', AgePrompt.tStopRefresh)
    trials.addData('what_typed.started', what_typed.tStartRefresh)
    trials.addData('what_typed.stopped', what_typed.tStopRefresh)
    trials.addData('missing_info.started', missing_info.tStartRefresh)
    trials.addData('missing_info.stopped', missing_info.tStopRefresh)
    trials.addData('press_space.started', press_space.tStartRefresh)
    trials.addData('press_space.stopped', press_space.tStopRefresh)
    # check responses
    if age.keys in ['', [], None]:  # No response was made
        age.keys = None
    trials.addData('age.keys',age.keys)
    if age.keys != None:  # we had a response
        trials.addData('age.rt', age.rt)
    trials.addData('age.started', age.tStartRefresh)
    trials.addData('age.stopped', age.tStopRefresh)
    # adding data to excel file through loop
    trials.addData('age', screenText)
    #trials.addData('video_played', video_played)
    #trials.addData('order_questions', order)
    
    # ending loop
    trials.finished=True
    trials.addData('blank.started', blank.tStartRefresh)
    trials.addData('blank.stopped', blank.tStopRefresh)
    trials.addData('text_7.started', text_7.tStartRefresh)
    trials.addData('text_7.stopped', text_7.tStopRefresh)
    # the Routine "AgeGender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Transition"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    TransitionComponents = [Text, PressSpace_5, key_resp_5]
    for thisComponent in TransitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TransitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Transition"-------
    while continueRoutine:
        # get current time
        t = TransitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TransitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Text* updates
        if Text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Text.frameNStart = frameN  # exact frame index
            Text.tStart = t  # local t and not account for scr refresh
            Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Text, 'tStartRefresh')  # time at next scr refresh
            Text.setAutoDraw(True)
        
        # *PressSpace_5* updates
        if PressSpace_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_5.frameNStart = frameN  # exact frame index
            PressSpace_5.tStart = t  # local t and not account for scr refresh
            PressSpace_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_5, 'tStartRefresh')  # time at next scr refresh
            PressSpace_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TransitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Transition"-------
    for thisComponent in TransitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Text.started', Text.tStartRefresh)
    trials.addData('Text.stopped', Text.tStopRefresh)
    trials.addData('PressSpace_5.started', PressSpace_5.tStartRefresh)
    trials.addData('PressSpace_5.stopped', PressSpace_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    pressSpace.keys = []
    pressSpace.rt = []
    _pressSpace_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [image_1, PressSpace_2, pressSpace, movie_2, text_13, text_14, text_18, text_15, text_16, text_23, text_21]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_1* updates
        if image_1.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            image_1.frameNStart = frameN  # exact frame index
            image_1.tStart = t  # local t and not account for scr refresh
            image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
            image_1.setAutoDraw(True)
        if image_1.status == STARTED:  # only update if drawing
            image_1.setImage(image_shown, log=False)
        
        # *PressSpace_2* updates
        if PressSpace_2.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_2.frameNStart = frameN  # exact frame index
            PressSpace_2.tStart = t  # local t and not account for scr refresh
            PressSpace_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_2, 'tStartRefresh')  # time at next scr refresh
            PressSpace_2.setAutoDraw(True)
        
        # *pressSpace* updates
        waitOnFlip = False
        if pressSpace.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            pressSpace.frameNStart = frameN  # exact frame index
            pressSpace.tStart = t  # local t and not account for scr refresh
            pressSpace.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace, 'tStartRefresh')  # time at next scr refresh
            pressSpace.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pressSpace.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pressSpace.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pressSpace.status == STARTED and not waitOnFlip:
            theseKeys = pressSpace.getKeys(keyList=['space'], waitRelease=False)
            _pressSpace_allKeys.extend(theseKeys)
            if len(_pressSpace_allKeys):
                pressSpace.keys = _pressSpace_allKeys[-1].name  # just the last key pressed
                pressSpace.rt = _pressSpace_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *movie_2* updates
        if movie_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie_2.frameNStart = frameN  # exact frame index
            movie_2.tStart = t  # local t and not account for scr refresh
            movie_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
            movie_2.setAutoDraw(True)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 9.5-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 21-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 23.5-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            text_15.setAutoDraw(True)
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 34.5-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 36.5-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 46.5-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_1.started', image_1.tStartRefresh)
    trials.addData('image_1.stopped', image_1.tStopRefresh)
    trials.addData('PressSpace_2.started', PressSpace_2.tStartRefresh)
    trials.addData('PressSpace_2.stopped', PressSpace_2.tStopRefresh)
    # check responses
    if pressSpace.keys in ['', [], None]:  # No response was made
        pressSpace.keys = None
    trials.addData('pressSpace.keys',pressSpace.keys)
    if pressSpace.keys != None:  # we had a response
        trials.addData('pressSpace.rt', pressSpace.rt)
    trials.addData('pressSpace.started', pressSpace.tStartRefresh)
    trials.addData('pressSpace.stopped', pressSpace.tStopRefresh)
    movie_2.stop()
    trials.addData('text_13.started', text_13.tStartRefresh)
    trials.addData('text_13.stopped', text_13.tStopRefresh)
    trials.addData('text_14.started', text_14.tStartRefresh)
    trials.addData('text_14.stopped', text_14.tStopRefresh)
    trials.addData('text_18.started', text_18.tStartRefresh)
    trials.addData('text_18.stopped', text_18.tStopRefresh)
    trials.addData('text_15.started', text_15.tStartRefresh)
    trials.addData('text_15.stopped', text_15.tStopRefresh)
    trials.addData('text_16.started', text_16.tStartRefresh)
    trials.addData('text_16.stopped', text_16.tStopRefresh)
    trials.addData('text_23.started', text_23.tStartRefresh)
    trials.addData('text_23.stopped', text_23.tStopRefresh)
    trials.addData('text_21.started', text_21.tStartRefresh)
    trials.addData('text_21.stopped', text_21.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Video1"-------
    continueRoutine = True
    # update component parameters for each repeat
    movie_3 = visual.MovieStim3(
        win=win, name='movie_3',units='height', 
        noAudio = False,
        filename=video_played,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=(0.8, 0.4),
        depth=0.0,
        )
    # keep track of which components have finished
    Video1Components = [movie_3]
    for thisComponent in Video1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Video1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Video1"-------
    while continueRoutine:
        # get current time
        t = Video1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Video1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_3* updates
        if movie_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            movie_3.frameNStart = frameN  # exact frame index
            movie_3.tStart = t  # local t and not account for scr refresh
            movie_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie_3, 'tStartRefresh')  # time at next scr refresh
            movie_3.setAutoDraw(True)
        if movie_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie_3.tStartRefresh + video_duration-frameTolerance:
                # keep track of stop time/frame for later
                movie_3.tStop = t  # not accounting for scr refresh
                movie_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie_3, 'tStopRefresh')  # time at next scr refresh
                movie_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Video1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Video1"-------
    for thisComponent in Video1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie_3.stop()
    # the Routine "Video1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "VideoTransition"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    VideoTransitionComponents = [PressSpace_6, key_resp_3]
    for thisComponent in VideoTransitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VideoTransitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "VideoTransition"-------
    while continueRoutine:
        # get current time
        t = VideoTransitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VideoTransitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PressSpace_6* updates
        if PressSpace_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_6.frameNStart = frameN  # exact frame index
            PressSpace_6.tStart = t  # local t and not account for scr refresh
            PressSpace_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_6, 'tStartRefresh')  # time at next scr refresh
            PressSpace_6.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VideoTransitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "VideoTransition"-------
    for thisComponent in VideoTransitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('PressSpace_6.started', PressSpace_6.tStartRefresh)
    trials.addData('PressSpace_6.stopped', PressSpace_6.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "VideoTransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Video2"-------
    continueRoutine = True
    # update component parameters for each repeat
    movie_4 = visual.MovieStim3(
        win=win, name='movie_4',units='height', 
        noAudio = False,
        filename=video_played,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=(0.8, 0.4),
        depth=0.0,
        )
    # keep track of which components have finished
    Video2Components = [movie_4]
    for thisComponent in Video2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Video2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Video2"-------
    while continueRoutine:
        # get current time
        t = Video2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Video2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_4* updates
        if movie_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            movie_4.frameNStart = frameN  # exact frame index
            movie_4.tStart = t  # local t and not account for scr refresh
            movie_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie_4, 'tStartRefresh')  # time at next scr refresh
            movie_4.setAutoDraw(True)
        if movie_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie_4.tStartRefresh + video_duration-frameTolerance:
                # keep track of stop time/frame for later
                movie_4.tStop = t  # not accounting for scr refresh
                movie_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie_4, 'tStopRefresh')  # time at next scr refresh
                movie_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Video2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Video2"-------
    for thisComponent in Video2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie_4.stop()
    # the Routine "Video2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "VideoTransition_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    VideoTransition_2Components = [PressSpace_7, key_resp_6]
    for thisComponent in VideoTransition_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VideoTransition_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "VideoTransition_2"-------
    while continueRoutine:
        # get current time
        t = VideoTransition_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VideoTransition_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PressSpace_7* updates
        if PressSpace_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_7.frameNStart = frameN  # exact frame index
            PressSpace_7.tStart = t  # local t and not account for scr refresh
            PressSpace_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_7, 'tStartRefresh')  # time at next scr refresh
            PressSpace_7.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VideoTransition_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "VideoTransition_2"-------
    for thisComponent in VideoTransition_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('PressSpace_7.started', PressSpace_7.tStartRefresh)
    trials.addData('PressSpace_7.stopped', PressSpace_7.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    trials.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "VideoTransition_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Video3"-------
    continueRoutine = True
    # update component parameters for each repeat
    movie_5 = visual.MovieStim3(
        win=win, name='movie_5',units='height', 
        noAudio = False,
        filename=video_played,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=(0.8, 0.4),
        depth=0.0,
        )
    # keep track of which components have finished
    Video3Components = [movie_5]
    for thisComponent in Video3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Video3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Video3"-------
    while continueRoutine:
        # get current time
        t = Video3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Video3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_5* updates
        if movie_5.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            movie_5.frameNStart = frameN  # exact frame index
            movie_5.tStart = t  # local t and not account for scr refresh
            movie_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie_5, 'tStartRefresh')  # time at next scr refresh
            movie_5.setAutoDraw(True)
        if movie_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie_5.tStartRefresh + video_duration-frameTolerance:
                # keep track of stop time/frame for later
                movie_5.tStop = t  # not accounting for scr refresh
                movie_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie_5, 'tStopRefresh')  # time at next scr refresh
                movie_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Video3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Video3"-------
    for thisComponent in Video3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie_5.stop()
    # the Routine "Video3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "VideoTransition_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    VideoTransition_3Components = [PressSpace_8, key_resp_7]
    for thisComponent in VideoTransition_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VideoTransition_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "VideoTransition_3"-------
    while continueRoutine:
        # get current time
        t = VideoTransition_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VideoTransition_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PressSpace_8* updates
        if PressSpace_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_8.frameNStart = frameN  # exact frame index
            PressSpace_8.tStart = t  # local t and not account for scr refresh
            PressSpace_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_8, 'tStartRefresh')  # time at next scr refresh
            PressSpace_8.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VideoTransition_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "VideoTransition_3"-------
    for thisComponent in VideoTransition_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('PressSpace_8.started', PressSpace_8.tStartRefresh)
    trials.addData('PressSpace_8.stopped', PressSpace_8.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials.addData('key_resp_7.rt', key_resp_7.rt)
    trials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    trials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "VideoTransition_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "I1_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_6.reset()
    slider_7.reset()
    slider_8.reset()
    slider_10.reset()
    slider_9.reset()
    slider_50.reset()
    key_p_2.keys = []
    key_p_2.rt = []
    _key_p_2_allKeys = []
    number_keys_p_2 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_1 = ''
    quest_2 = ''
    quest_3 = ''
    quest_4 = ''
    quest_5 = ''
    quest_6 = ''
    # keep track of which components have finished
    I1_O1Components = [Question, Q1, slider_6, Q_2, slider_7, Q4, slider_8, Q3, slider_10, Q5, slider_9, Q6, slider_50, pressSpace_4, key_p_2, message_2]
    for thisComponent in I1_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    I1_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "I1_O1"-------
    while continueRoutine:
        # get current time
        t = I1_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=I1_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question* updates
        if Question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question.frameNStart = frameN  # exact frame index
            Question.tStart = t  # local t and not account for scr refresh
            Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
            Question.setAutoDraw(True)
        
        # *Q1* updates
        if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1.frameNStart = frameN  # exact frame index
            Q1.tStart = t  # local t and not account for scr refresh
            Q1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
            Q1.setAutoDraw(True)
        if Q1.status == STARTED:  # only update if drawing
            Q1.setText(quest_1, log=False)
        
        # *slider_6* updates
        if slider_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_6.frameNStart = frameN  # exact frame index
            slider_6.tStart = t  # local t and not account for scr refresh
            slider_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
            slider_6.setAutoDraw(True)
        
        # *Q_2* updates
        if Q_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_2.frameNStart = frameN  # exact frame index
            Q_2.tStart = t  # local t and not account for scr refresh
            Q_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_2, 'tStartRefresh')  # time at next scr refresh
            Q_2.setAutoDraw(True)
        if Q_2.status == STARTED:  # only update if drawing
            Q_2.setText(quest_2, log=False)
        
        # *slider_7* updates
        if slider_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_7.frameNStart = frameN  # exact frame index
            slider_7.tStart = t  # local t and not account for scr refresh
            slider_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_7, 'tStartRefresh')  # time at next scr refresh
            slider_7.setAutoDraw(True)
        
        # *Q4* updates
        if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4.frameNStart = frameN  # exact frame index
            Q4.tStart = t  # local t and not account for scr refresh
            Q4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
            Q4.setAutoDraw(True)
        if Q4.status == STARTED:  # only update if drawing
            Q4.setText(quest_3, log=False)
        
        # *slider_8* updates
        if slider_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_8.frameNStart = frameN  # exact frame index
            slider_8.tStart = t  # local t and not account for scr refresh
            slider_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_8, 'tStartRefresh')  # time at next scr refresh
            slider_8.setAutoDraw(True)
        
        # *Q3* updates
        if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3.frameNStart = frameN  # exact frame index
            Q3.tStart = t  # local t and not account for scr refresh
            Q3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
            Q3.setAutoDraw(True)
        if Q3.status == STARTED:  # only update if drawing
            Q3.setText(quest_4, log=False)
        
        # *slider_10* updates
        if slider_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_10.frameNStart = frameN  # exact frame index
            slider_10.tStart = t  # local t and not account for scr refresh
            slider_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_10, 'tStartRefresh')  # time at next scr refresh
            slider_10.setAutoDraw(True)
        
        # *Q5* updates
        if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q5.frameNStart = frameN  # exact frame index
            Q5.tStart = t  # local t and not account for scr refresh
            Q5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
            Q5.setAutoDraw(True)
        if Q5.status == STARTED:  # only update if drawing
            Q5.setText(quest_5, log=False)
        
        # *slider_9* updates
        if slider_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_9.frameNStart = frameN  # exact frame index
            slider_9.tStart = t  # local t and not account for scr refresh
            slider_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_9, 'tStartRefresh')  # time at next scr refresh
            slider_9.setAutoDraw(True)
        
        # *Q6* updates
        if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q6.frameNStart = frameN  # exact frame index
            Q6.tStart = t  # local t and not account for scr refresh
            Q6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
            Q6.setAutoDraw(True)
        if Q6.status == STARTED:  # only update if drawing
            Q6.setText(quest_6, log=False)
        
        # *slider_50* updates
        if slider_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_50.frameNStart = frameN  # exact frame index
            slider_50.tStart = t  # local t and not account for scr refresh
            slider_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_50, 'tStartRefresh')  # time at next scr refresh
            slider_50.setAutoDraw(True)
        
        # *pressSpace_4* updates
        if pressSpace_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_4.frameNStart = frameN  # exact frame index
            pressSpace_4.tStart = t  # local t and not account for scr refresh
            pressSpace_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_4, 'tStartRefresh')  # time at next scr refresh
            pressSpace_4.setAutoDraw(True)
        if pressSpace_4.status == STARTED:  # only update if drawing
            pressSpace_4.setText(spaceText, log=False)
        
        # *key_p_2* updates
        waitOnFlip = False
        if key_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_2.frameNStart = frameN  # exact frame index
            key_p_2.tStart = t  # local t and not account for scr refresh
            key_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_2, 'tStartRefresh')  # time at next scr refresh
            key_p_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_2.status == STARTED and not waitOnFlip:
            theseKeys = key_p_2.getKeys(keyList=['space'], waitRelease=False)
            _key_p_2_allKeys.extend(theseKeys)
            if len(_key_p_2_allKeys):
                key_p_2.keys = [key.name for key in _key_p_2_allKeys]  # storing all keys
                key_p_2.rt = [key.rt for key in _key_p_2_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p_2.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_2.keys) > number_keys_p_2:
                
                # update our count of the number of keys pressed
                number_keys_p_2 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_6.getRating() or not slider_7.getRating() or not slider_10.getRating() or not slider_8.getRating() or not slider_9.getRating() or not slider_50.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_2* updates
        if message_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_2.frameNStart = frameN  # exact frame index
            message_2.tStart = t  # local t and not account for scr refresh
            message_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_2, 'tStartRefresh')  # time at next scr refresh
            message_2.setAutoDraw(True)
        if message_2.status == STARTED:  # only update if drawing
            message_2.setText(msg_p, log=False)
        if qtext==1:
            quest_1 = 'How appropriate is her reaction in the video?'
            quest_2 = 'Based on what you saw in the video, how likeable do you think she is?'
            quest_3 = 'What does the other person think of her after her reaction?'
            quest_4 = 'How upset does she look in the video?'
            quest_5= 'Is she showing the other person how she feels?'
            quest_6= 'How does she feel about herself as a person?'
        elif qtext==2:
            quest_1 = 'How appropriate is his reaction in the video?'
            quest_2 = 'Based on what you saw in the video, how likeable do you think he is?'
            quest_3 = 'What does the other person think of him after his reaction?'
            quest_4 = 'How upset does he look in the video?'
            quest_5= 'Is he showing the other person how he feels?'
            quest_6= 'How does he feel about himself as a person?'
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in I1_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "I1_O1"-------
    for thisComponent in I1_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question.started', Question.tStartRefresh)
    trials.addData('Question.stopped', Question.tStopRefresh)
    trials.addData('Q1.started', Q1.tStartRefresh)
    trials.addData('Q1.stopped', Q1.tStopRefresh)
    trials.addData('slider_6.response', slider_6.getRating())
    trials.addData('slider_6.rt', slider_6.getRT())
    trials.addData('slider_6.started', slider_6.tStartRefresh)
    trials.addData('slider_6.stopped', slider_6.tStopRefresh)
    trials.addData('Q_2.started', Q_2.tStartRefresh)
    trials.addData('Q_2.stopped', Q_2.tStopRefresh)
    trials.addData('slider_7.response', slider_7.getRating())
    trials.addData('slider_7.rt', slider_7.getRT())
    trials.addData('slider_7.started', slider_7.tStartRefresh)
    trials.addData('slider_7.stopped', slider_7.tStopRefresh)
    trials.addData('Q4.started', Q4.tStartRefresh)
    trials.addData('Q4.stopped', Q4.tStopRefresh)
    trials.addData('slider_8.response', slider_8.getRating())
    trials.addData('slider_8.rt', slider_8.getRT())
    trials.addData('slider_8.started', slider_8.tStartRefresh)
    trials.addData('slider_8.stopped', slider_8.tStopRefresh)
    trials.addData('Q3.started', Q3.tStartRefresh)
    trials.addData('Q3.stopped', Q3.tStopRefresh)
    trials.addData('slider_10.response', slider_10.getRating())
    trials.addData('slider_10.rt', slider_10.getRT())
    trials.addData('slider_10.started', slider_10.tStartRefresh)
    trials.addData('slider_10.stopped', slider_10.tStopRefresh)
    trials.addData('Q5.started', Q5.tStartRefresh)
    trials.addData('Q5.stopped', Q5.tStopRefresh)
    trials.addData('slider_9.response', slider_9.getRating())
    trials.addData('slider_9.rt', slider_9.getRT())
    trials.addData('slider_9.started', slider_9.tStartRefresh)
    trials.addData('slider_9.stopped', slider_9.tStopRefresh)
    trials.addData('Q6.started', Q6.tStartRefresh)
    trials.addData('Q6.stopped', Q6.tStopRefresh)
    trials.addData('slider_50.response', slider_50.getRating())
    trials.addData('slider_50.rt', slider_50.getRT())
    trials.addData('slider_50.started', slider_50.tStartRefresh)
    trials.addData('slider_50.stopped', slider_50.tStopRefresh)
    trials.addData('pressSpace_4.started', pressSpace_4.tStartRefresh)
    trials.addData('pressSpace_4.stopped', pressSpace_4.tStopRefresh)
    # check responses
    if key_p_2.keys in ['', [], None]:  # No response was made
        key_p_2.keys = None
    trials.addData('key_p_2.keys',key_p_2.keys)
    if key_p_2.keys != None:  # we had a response
        trials.addData('key_p_2.rt', key_p_2.rt)
    trials.addData('key_p_2.started', key_p_2.tStartRefresh)
    trials.addData('key_p_2.stopped', key_p_2.tStopRefresh)
    trials.addData('message_2.started', message_2.tStartRefresh)
    trials.addData('message_2.stopped', message_2.tStopRefresh)
    # the Routine "I1_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "I2_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_11.reset()
    slider_12.reset()
    slider_13.reset()
    slider_14.reset()
    slider_15.reset()
    slider_61.reset()
    key_p_3.keys = []
    key_p_3.rt = []
    _key_p_3_allKeys = []
    number_keys_p_3 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_7 = ''
    quest_8 = ''
    quest_9 = ''
    quest_10 = ''
    quest_11 = ''
    quest_12 = ''
    # keep track of which components have finished
    I2_O1Components = [Question_3, Q1_3, slider_11, Q, slider_12, Q3_2, slider_13, Q4_2, slider_14, Q5_2, slider_15, Q6_2, slider_61, pressSpace_5, key_p_3, message_3]
    for thisComponent in I2_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    I2_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "I2_O1"-------
    while continueRoutine:
        # get current time
        t = I2_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=I2_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_3* updates
        if Question_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_3.frameNStart = frameN  # exact frame index
            Question_3.tStart = t  # local t and not account for scr refresh
            Question_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_3, 'tStartRefresh')  # time at next scr refresh
            Question_3.setAutoDraw(True)
        
        # *Q1_3* updates
        if Q1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1_3.frameNStart = frameN  # exact frame index
            Q1_3.tStart = t  # local t and not account for scr refresh
            Q1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1_3, 'tStartRefresh')  # time at next scr refresh
            Q1_3.setAutoDraw(True)
        if Q1_3.status == STARTED:  # only update if drawing
            Q1_3.setText(quest_7, log=False)
        
        # *slider_11* updates
        if slider_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_11.frameNStart = frameN  # exact frame index
            slider_11.tStart = t  # local t and not account for scr refresh
            slider_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_11, 'tStartRefresh')  # time at next scr refresh
            slider_11.setAutoDraw(True)
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            Q.setAutoDraw(True)
        if Q.status == STARTED:  # only update if drawing
            Q.setText(quest_8, log=False)
        
        # *slider_12* updates
        if slider_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_12.frameNStart = frameN  # exact frame index
            slider_12.tStart = t  # local t and not account for scr refresh
            slider_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_12, 'tStartRefresh')  # time at next scr refresh
            slider_12.setAutoDraw(True)
        
        # *Q3_2* updates
        if Q3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_2.frameNStart = frameN  # exact frame index
            Q3_2.tStart = t  # local t and not account for scr refresh
            Q3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_2, 'tStartRefresh')  # time at next scr refresh
            Q3_2.setAutoDraw(True)
        if Q3_2.status == STARTED:  # only update if drawing
            Q3_2.setText(quest_9, log=False)
        
        # *slider_13* updates
        if slider_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_13.frameNStart = frameN  # exact frame index
            slider_13.tStart = t  # local t and not account for scr refresh
            slider_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_13, 'tStartRefresh')  # time at next scr refresh
            slider_13.setAutoDraw(True)
        
        # *Q4_2* updates
        if Q4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4_2.frameNStart = frameN  # exact frame index
            Q4_2.tStart = t  # local t and not account for scr refresh
            Q4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4_2, 'tStartRefresh')  # time at next scr refresh
            Q4_2.setAutoDraw(True)
        if Q4_2.status == STARTED:  # only update if drawing
            Q4_2.setText(quest_10, log=False)
        
        # *slider_14* updates
        if slider_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_14.frameNStart = frameN  # exact frame index
            slider_14.tStart = t  # local t and not account for scr refresh
            slider_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_14, 'tStartRefresh')  # time at next scr refresh
            slider_14.setAutoDraw(True)
        
        # *Q5_2* updates
        if Q5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q5_2.frameNStart = frameN  # exact frame index
            Q5_2.tStart = t  # local t and not account for scr refresh
            Q5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q5_2, 'tStartRefresh')  # time at next scr refresh
            Q5_2.setAutoDraw(True)
        if Q5_2.status == STARTED:  # only update if drawing
            Q5_2.setText(quest_11, log=False)
        
        # *slider_15* updates
        if slider_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_15.frameNStart = frameN  # exact frame index
            slider_15.tStart = t  # local t and not account for scr refresh
            slider_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_15, 'tStartRefresh')  # time at next scr refresh
            slider_15.setAutoDraw(True)
        
        # *Q6_2* updates
        if Q6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q6_2.frameNStart = frameN  # exact frame index
            Q6_2.tStart = t  # local t and not account for scr refresh
            Q6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q6_2, 'tStartRefresh')  # time at next scr refresh
            Q6_2.setAutoDraw(True)
        if Q6_2.status == STARTED:  # only update if drawing
            Q6_2.setText(quest_12, log=False)
        
        # *slider_61* updates
        if slider_61.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_61.frameNStart = frameN  # exact frame index
            slider_61.tStart = t  # local t and not account for scr refresh
            slider_61.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_61, 'tStartRefresh')  # time at next scr refresh
            slider_61.setAutoDraw(True)
        
        # *pressSpace_5* updates
        if pressSpace_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_5.frameNStart = frameN  # exact frame index
            pressSpace_5.tStart = t  # local t and not account for scr refresh
            pressSpace_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_5, 'tStartRefresh')  # time at next scr refresh
            pressSpace_5.setAutoDraw(True)
        if pressSpace_5.status == STARTED:  # only update if drawing
            pressSpace_5.setText(spaceText, log=False)
        
        # *key_p_3* updates
        waitOnFlip = False
        if key_p_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_3.frameNStart = frameN  # exact frame index
            key_p_3.tStart = t  # local t and not account for scr refresh
            key_p_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_3, 'tStartRefresh')  # time at next scr refresh
            key_p_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_3.status == STARTED and not waitOnFlip:
            theseKeys = key_p_3.getKeys(keyList=['space'], waitRelease=False)
            _key_p_3_allKeys.extend(theseKeys)
            if len(_key_p_3_allKeys):
                key_p_3.keys = [key.name for key in _key_p_3_allKeys]  # storing all keys
                key_p_3.rt = [key.rt for key in _key_p_3_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p_3.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_3.keys) > number_keys_p_3:
                
                # update our count of the number of keys pressed
                number_keys_p_3 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_11.getRating() or not slider_12.getRating() or not slider_13.getRating() or not slider_14.getRating() or not slider_15.getRating() or not slider_61.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_3* updates
        if message_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_3.frameNStart = frameN  # exact frame index
            message_3.tStart = t  # local t and not account for scr refresh
            message_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_3, 'tStartRefresh')  # time at next scr refresh
            message_3.setAutoDraw(True)
        if message_3.status == STARTED:  # only update if drawing
            message_3.setText(msg_p, log=False)
        if qtext==1:
            quest_7 = 'How does she feel about what she did?'
            quest_8 = 'How surprised is she by what the other person said?'
            quest_9 = 'How much did she have to think about what was said?'
            quest_10 = 'How difficult was it for her to understand what was said?'
            quest_11 = 'In your opinion, how serious was the harm she caused?'
            quest_12 = 'In your opinion, was the relationship damaged by the harm she caused?'
        elif qtext==2:
            quest_7 = 'How does he feel about what he did?'
            quest_8 = 'How surprised is he by what the other person said?'
            quest_9 = 'How much did he have to think about what was said?'
            quest_10 = 'How difficult was it for him to understand what was said?'
            quest_11 = 'In your opinion, how serious was the harm he caused?'
            quest_12 = 'In your opinion, was the relationship damaged by the harm he caused?'
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in I2_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "I2_O1"-------
    for thisComponent in I2_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_3.started', Question_3.tStartRefresh)
    trials.addData('Question_3.stopped', Question_3.tStopRefresh)
    trials.addData('Q1_3.started', Q1_3.tStartRefresh)
    trials.addData('Q1_3.stopped', Q1_3.tStopRefresh)
    trials.addData('slider_11.response', slider_11.getRating())
    trials.addData('slider_11.rt', slider_11.getRT())
    trials.addData('slider_11.started', slider_11.tStartRefresh)
    trials.addData('slider_11.stopped', slider_11.tStopRefresh)
    trials.addData('Q.started', Q.tStartRefresh)
    trials.addData('Q.stopped', Q.tStopRefresh)
    trials.addData('slider_12.response', slider_12.getRating())
    trials.addData('slider_12.rt', slider_12.getRT())
    trials.addData('slider_12.started', slider_12.tStartRefresh)
    trials.addData('slider_12.stopped', slider_12.tStopRefresh)
    trials.addData('Q3_2.started', Q3_2.tStartRefresh)
    trials.addData('Q3_2.stopped', Q3_2.tStopRefresh)
    trials.addData('slider_13.response', slider_13.getRating())
    trials.addData('slider_13.rt', slider_13.getRT())
    trials.addData('slider_13.started', slider_13.tStartRefresh)
    trials.addData('slider_13.stopped', slider_13.tStopRefresh)
    trials.addData('Q4_2.started', Q4_2.tStartRefresh)
    trials.addData('Q4_2.stopped', Q4_2.tStopRefresh)
    trials.addData('slider_14.response', slider_14.getRating())
    trials.addData('slider_14.rt', slider_14.getRT())
    trials.addData('slider_14.started', slider_14.tStartRefresh)
    trials.addData('slider_14.stopped', slider_14.tStopRefresh)
    trials.addData('Q5_2.started', Q5_2.tStartRefresh)
    trials.addData('Q5_2.stopped', Q5_2.tStopRefresh)
    trials.addData('slider_15.response', slider_15.getRating())
    trials.addData('slider_15.rt', slider_15.getRT())
    trials.addData('slider_15.started', slider_15.tStartRefresh)
    trials.addData('slider_15.stopped', slider_15.tStopRefresh)
    trials.addData('Q6_2.started', Q6_2.tStartRefresh)
    trials.addData('Q6_2.stopped', Q6_2.tStopRefresh)
    trials.addData('slider_61.response', slider_61.getRating())
    trials.addData('slider_61.rt', slider_61.getRT())
    trials.addData('slider_61.started', slider_61.tStartRefresh)
    trials.addData('slider_61.stopped', slider_61.tStopRefresh)
    trials.addData('pressSpace_5.started', pressSpace_5.tStartRefresh)
    trials.addData('pressSpace_5.stopped', pressSpace_5.tStopRefresh)
    # check responses
    if key_p_3.keys in ['', [], None]:  # No response was made
        key_p_3.keys = None
    trials.addData('key_p_3.keys',key_p_3.keys)
    if key_p_3.keys != None:  # we had a response
        trials.addData('key_p_3.rt', key_p_3.rt)
    trials.addData('key_p_3.started', key_p_3.tStartRefresh)
    trials.addData('key_p_3.stopped', key_p_3.tStopRefresh)
    trials.addData('message_3.started', message_3.tStartRefresh)
    trials.addData('message_3.stopped', message_3.tStopRefresh)
    # the Routine "I2_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "I1_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_16.reset()
    slider_17.reset()
    slider_18.reset()
    slider_19.reset()
    slider_20.reset()
    slider_62.reset()
    key_p_4.keys = []
    key_p_4.rt = []
    _key_p_4_allKeys = []
    number_keys_p_4 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_7 = ''
    quest_8 = ''
    quest_9 = ''
    quest_10 = ''
    quest_11 = ''
    quest_12 = ''
    # keep track of which components have finished
    I1_O2Components = [Question_4, Q1_4, slider_16, Q_3, slider_17, Q3_3, slider_18, Q4_3, slider_19, Q5_3, slider_20, Q6_3, slider_62, pressSpace_6, key_p_4, message_4]
    for thisComponent in I1_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    I1_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "I1_O2"-------
    while continueRoutine:
        # get current time
        t = I1_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=I1_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_4* updates
        if Question_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_4.frameNStart = frameN  # exact frame index
            Question_4.tStart = t  # local t and not account for scr refresh
            Question_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_4, 'tStartRefresh')  # time at next scr refresh
            Question_4.setAutoDraw(True)
        
        # *Q1_4* updates
        if Q1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1_4.frameNStart = frameN  # exact frame index
            Q1_4.tStart = t  # local t and not account for scr refresh
            Q1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1_4, 'tStartRefresh')  # time at next scr refresh
            Q1_4.setAutoDraw(True)
        if Q1_4.status == STARTED:  # only update if drawing
            Q1_4.setText(quest_12, log=False)
        
        # *slider_16* updates
        if slider_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_16.frameNStart = frameN  # exact frame index
            slider_16.tStart = t  # local t and not account for scr refresh
            slider_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_16, 'tStartRefresh')  # time at next scr refresh
            slider_16.setAutoDraw(True)
        
        # *Q_3* updates
        if Q_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_3.frameNStart = frameN  # exact frame index
            Q_3.tStart = t  # local t and not account for scr refresh
            Q_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_3, 'tStartRefresh')  # time at next scr refresh
            Q_3.setAutoDraw(True)
        if Q_3.status == STARTED:  # only update if drawing
            Q_3.setText(quest_11, log=False)
        
        # *slider_17* updates
        if slider_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_17.frameNStart = frameN  # exact frame index
            slider_17.tStart = t  # local t and not account for scr refresh
            slider_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_17, 'tStartRefresh')  # time at next scr refresh
            slider_17.setAutoDraw(True)
        
        # *Q3_3* updates
        if Q3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_3.frameNStart = frameN  # exact frame index
            Q3_3.tStart = t  # local t and not account for scr refresh
            Q3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_3, 'tStartRefresh')  # time at next scr refresh
            Q3_3.setAutoDraw(True)
        if Q3_3.status == STARTED:  # only update if drawing
            Q3_3.setText(quest_10, log=False)
        
        # *slider_18* updates
        if slider_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_18.frameNStart = frameN  # exact frame index
            slider_18.tStart = t  # local t and not account for scr refresh
            slider_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_18, 'tStartRefresh')  # time at next scr refresh
            slider_18.setAutoDraw(True)
        
        # *Q4_3* updates
        if Q4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4_3.frameNStart = frameN  # exact frame index
            Q4_3.tStart = t  # local t and not account for scr refresh
            Q4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4_3, 'tStartRefresh')  # time at next scr refresh
            Q4_3.setAutoDraw(True)
        if Q4_3.status == STARTED:  # only update if drawing
            Q4_3.setText(quest_9, log=False)
        
        # *slider_19* updates
        if slider_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_19.frameNStart = frameN  # exact frame index
            slider_19.tStart = t  # local t and not account for scr refresh
            slider_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_19, 'tStartRefresh')  # time at next scr refresh
            slider_19.setAutoDraw(True)
        
        # *Q5_3* updates
        if Q5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q5_3.frameNStart = frameN  # exact frame index
            Q5_3.tStart = t  # local t and not account for scr refresh
            Q5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q5_3, 'tStartRefresh')  # time at next scr refresh
            Q5_3.setAutoDraw(True)
        if Q5_3.status == STARTED:  # only update if drawing
            Q5_3.setText(quest_8, log=False)
        
        # *slider_20* updates
        if slider_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_20.frameNStart = frameN  # exact frame index
            slider_20.tStart = t  # local t and not account for scr refresh
            slider_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_20, 'tStartRefresh')  # time at next scr refresh
            slider_20.setAutoDraw(True)
        
        # *Q6_3* updates
        if Q6_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q6_3.frameNStart = frameN  # exact frame index
            Q6_3.tStart = t  # local t and not account for scr refresh
            Q6_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q6_3, 'tStartRefresh')  # time at next scr refresh
            Q6_3.setAutoDraw(True)
        if Q6_3.status == STARTED:  # only update if drawing
            Q6_3.setText(quest_7, log=False)
        
        # *slider_62* updates
        if slider_62.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_62.frameNStart = frameN  # exact frame index
            slider_62.tStart = t  # local t and not account for scr refresh
            slider_62.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_62, 'tStartRefresh')  # time at next scr refresh
            slider_62.setAutoDraw(True)
        
        # *pressSpace_6* updates
        if pressSpace_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_6.frameNStart = frameN  # exact frame index
            pressSpace_6.tStart = t  # local t and not account for scr refresh
            pressSpace_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_6, 'tStartRefresh')  # time at next scr refresh
            pressSpace_6.setAutoDraw(True)
        if pressSpace_6.status == STARTED:  # only update if drawing
            pressSpace_6.setText(spaceText, log=False)
        
        # *key_p_4* updates
        waitOnFlip = False
        if key_p_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_4.frameNStart = frameN  # exact frame index
            key_p_4.tStart = t  # local t and not account for scr refresh
            key_p_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_4, 'tStartRefresh')  # time at next scr refresh
            key_p_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_4.status == STARTED and not waitOnFlip:
            theseKeys = key_p_4.getKeys(keyList=['space'], waitRelease=False)
            _key_p_4_allKeys.extend(theseKeys)
            if len(_key_p_4_allKeys):
                key_p_4.keys = [key.name for key in _key_p_4_allKeys]  # storing all keys
                key_p_4.rt = [key.rt for key in _key_p_4_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_4.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_4.keys) > number_keys_p_4:
                
                # update our count of the number of keys pressed
                number_keys_p_4 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_16.getRating() or not slider_17.getRating() or not slider_18.getRating() or not slider_19.getRating() or not slider_20.getRating() or not slider_62.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_4* updates
        if message_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_4.frameNStart = frameN  # exact frame index
            message_4.tStart = t  # local t and not account for scr refresh
            message_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_4, 'tStartRefresh')  # time at next scr refresh
            message_4.setAutoDraw(True)
        if message_4.status == STARTED:  # only update if drawing
            message_4.setText(msg_p, log=False)
        if qtext==1:
            quest_7 = 'How does she feel about what she did?'
            quest_8 = 'How surprised is she by what the other person said?'
            quest_9 = 'How much did she have to think about what was said?'
            quest_10 = 'How difficult was it for her to understand what was said?'
            quest_11 = 'In your opinion, how serious was the harm she caused?'
            quest_12 = 'In your opinion, was the relationship damaged by the harm she caused?'
        elif qtext==2:
            quest_7 = 'How does he feel about what he did?'
            quest_8 = 'How surprised is he by what the other person said?'
            quest_9 = 'How much did he have to think about what was said?'
            quest_10 = 'How difficult was it for him to understand what was said?'
            quest_11 = 'In your opinion, how serious was the harm he caused?'
            quest_12 = 'In your opinion, was the relationship damaged by the harm he caused?'
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in I1_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "I1_O2"-------
    for thisComponent in I1_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_4.started', Question_4.tStartRefresh)
    trials.addData('Question_4.stopped', Question_4.tStopRefresh)
    trials.addData('Q1_4.started', Q1_4.tStartRefresh)
    trials.addData('Q1_4.stopped', Q1_4.tStopRefresh)
    trials.addData('slider_16.response', slider_16.getRating())
    trials.addData('slider_16.rt', slider_16.getRT())
    trials.addData('slider_16.started', slider_16.tStartRefresh)
    trials.addData('slider_16.stopped', slider_16.tStopRefresh)
    trials.addData('Q_3.started', Q_3.tStartRefresh)
    trials.addData('Q_3.stopped', Q_3.tStopRefresh)
    trials.addData('slider_17.response', slider_17.getRating())
    trials.addData('slider_17.rt', slider_17.getRT())
    trials.addData('slider_17.started', slider_17.tStartRefresh)
    trials.addData('slider_17.stopped', slider_17.tStopRefresh)
    trials.addData('Q3_3.started', Q3_3.tStartRefresh)
    trials.addData('Q3_3.stopped', Q3_3.tStopRefresh)
    trials.addData('slider_18.response', slider_18.getRating())
    trials.addData('slider_18.rt', slider_18.getRT())
    trials.addData('slider_18.started', slider_18.tStartRefresh)
    trials.addData('slider_18.stopped', slider_18.tStopRefresh)
    trials.addData('Q4_3.started', Q4_3.tStartRefresh)
    trials.addData('Q4_3.stopped', Q4_3.tStopRefresh)
    trials.addData('slider_19.response', slider_19.getRating())
    trials.addData('slider_19.rt', slider_19.getRT())
    trials.addData('slider_19.started', slider_19.tStartRefresh)
    trials.addData('slider_19.stopped', slider_19.tStopRefresh)
    trials.addData('Q5_3.started', Q5_3.tStartRefresh)
    trials.addData('Q5_3.stopped', Q5_3.tStopRefresh)
    trials.addData('slider_20.response', slider_20.getRating())
    trials.addData('slider_20.rt', slider_20.getRT())
    trials.addData('slider_20.started', slider_20.tStartRefresh)
    trials.addData('slider_20.stopped', slider_20.tStopRefresh)
    trials.addData('Q6_3.started', Q6_3.tStartRefresh)
    trials.addData('Q6_3.stopped', Q6_3.tStopRefresh)
    trials.addData('slider_62.response', slider_62.getRating())
    trials.addData('slider_62.rt', slider_62.getRT())
    trials.addData('slider_62.started', slider_62.tStartRefresh)
    trials.addData('slider_62.stopped', slider_62.tStopRefresh)
    trials.addData('pressSpace_6.started', pressSpace_6.tStartRefresh)
    trials.addData('pressSpace_6.stopped', pressSpace_6.tStopRefresh)
    # check responses
    if key_p_4.keys in ['', [], None]:  # No response was made
        key_p_4.keys = None
    trials.addData('key_p_4.keys',key_p_4.keys)
    if key_p_4.keys != None:  # we had a response
        trials.addData('key_p_4.rt', key_p_4.rt)
    trials.addData('key_p_4.started', key_p_4.tStartRefresh)
    trials.addData('key_p_4.stopped', key_p_4.tStopRefresh)
    trials.addData('message_4.started', message_4.tStartRefresh)
    trials.addData('message_4.stopped', message_4.tStopRefresh)
    # the Routine "I1_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "I2_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_33.reset()
    slider_34.reset()
    slider_35.reset()
    slider_36.reset()
    slider_37.reset()
    slider_63.reset()
    key_p_7.keys = []
    key_p_7.rt = []
    _key_p_7_allKeys = []
    number_keys_p_7 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_1 = ''
    quest_2 = ''
    quest_3 = ''
    quest_4 = ''
    quest_5 = ''
    quest_6 = ''
    # keep track of which components have finished
    I2_O2Components = [Question_5, Q1_5, slider_33, Q_4, slider_34, Q3_4, slider_35, Q4_4, slider_36, Q5_4, slider_37, Q6_4, slider_63, pressSpace_9, key_p_7, message_5]
    for thisComponent in I2_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    I2_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "I2_O2"-------
    while continueRoutine:
        # get current time
        t = I2_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=I2_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_5* updates
        if Question_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_5.frameNStart = frameN  # exact frame index
            Question_5.tStart = t  # local t and not account for scr refresh
            Question_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_5, 'tStartRefresh')  # time at next scr refresh
            Question_5.setAutoDraw(True)
        
        # *Q1_5* updates
        if Q1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1_5.frameNStart = frameN  # exact frame index
            Q1_5.tStart = t  # local t and not account for scr refresh
            Q1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1_5, 'tStartRefresh')  # time at next scr refresh
            Q1_5.setAutoDraw(True)
        if Q1_5.status == STARTED:  # only update if drawing
            Q1_5.setText(quest_6, log=False)
        
        # *slider_33* updates
        if slider_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_33.frameNStart = frameN  # exact frame index
            slider_33.tStart = t  # local t and not account for scr refresh
            slider_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_33, 'tStartRefresh')  # time at next scr refresh
            slider_33.setAutoDraw(True)
        
        # *Q_4* updates
        if Q_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_4.frameNStart = frameN  # exact frame index
            Q_4.tStart = t  # local t and not account for scr refresh
            Q_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_4, 'tStartRefresh')  # time at next scr refresh
            Q_4.setAutoDraw(True)
        if Q_4.status == STARTED:  # only update if drawing
            Q_4.setText(quest_5, log=False)
        
        # *slider_34* updates
        if slider_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_34.frameNStart = frameN  # exact frame index
            slider_34.tStart = t  # local t and not account for scr refresh
            slider_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_34, 'tStartRefresh')  # time at next scr refresh
            slider_34.setAutoDraw(True)
        
        # *Q3_4* updates
        if Q3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_4.frameNStart = frameN  # exact frame index
            Q3_4.tStart = t  # local t and not account for scr refresh
            Q3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_4, 'tStartRefresh')  # time at next scr refresh
            Q3_4.setAutoDraw(True)
        if Q3_4.status == STARTED:  # only update if drawing
            Q3_4.setText(quest_4, log=False)
        
        # *slider_35* updates
        if slider_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_35.frameNStart = frameN  # exact frame index
            slider_35.tStart = t  # local t and not account for scr refresh
            slider_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_35, 'tStartRefresh')  # time at next scr refresh
            slider_35.setAutoDraw(True)
        
        # *Q4_4* updates
        if Q4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4_4.frameNStart = frameN  # exact frame index
            Q4_4.tStart = t  # local t and not account for scr refresh
            Q4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4_4, 'tStartRefresh')  # time at next scr refresh
            Q4_4.setAutoDraw(True)
        if Q4_4.status == STARTED:  # only update if drawing
            Q4_4.setText(quest_3, log=False)
        
        # *slider_36* updates
        if slider_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_36.frameNStart = frameN  # exact frame index
            slider_36.tStart = t  # local t and not account for scr refresh
            slider_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_36, 'tStartRefresh')  # time at next scr refresh
            slider_36.setAutoDraw(True)
        
        # *Q5_4* updates
        if Q5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q5_4.frameNStart = frameN  # exact frame index
            Q5_4.tStart = t  # local t and not account for scr refresh
            Q5_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q5_4, 'tStartRefresh')  # time at next scr refresh
            Q5_4.setAutoDraw(True)
        if Q5_4.status == STARTED:  # only update if drawing
            Q5_4.setText(quest_2, log=False)
        
        # *slider_37* updates
        if slider_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_37.frameNStart = frameN  # exact frame index
            slider_37.tStart = t  # local t and not account for scr refresh
            slider_37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_37, 'tStartRefresh')  # time at next scr refresh
            slider_37.setAutoDraw(True)
        
        # *Q6_4* updates
        if Q6_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q6_4.frameNStart = frameN  # exact frame index
            Q6_4.tStart = t  # local t and not account for scr refresh
            Q6_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q6_4, 'tStartRefresh')  # time at next scr refresh
            Q6_4.setAutoDraw(True)
        if Q6_4.status == STARTED:  # only update if drawing
            Q6_4.setText(quest_1, log=False)
        
        # *slider_63* updates
        if slider_63.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_63.frameNStart = frameN  # exact frame index
            slider_63.tStart = t  # local t and not account for scr refresh
            slider_63.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_63, 'tStartRefresh')  # time at next scr refresh
            slider_63.setAutoDraw(True)
        
        # *pressSpace_9* updates
        if pressSpace_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_9.frameNStart = frameN  # exact frame index
            pressSpace_9.tStart = t  # local t and not account for scr refresh
            pressSpace_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_9, 'tStartRefresh')  # time at next scr refresh
            pressSpace_9.setAutoDraw(True)
        if pressSpace_9.status == STARTED:  # only update if drawing
            pressSpace_9.setText(spaceText, log=False)
        
        # *key_p_7* updates
        waitOnFlip = False
        if key_p_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_7.frameNStart = frameN  # exact frame index
            key_p_7.tStart = t  # local t and not account for scr refresh
            key_p_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_7, 'tStartRefresh')  # time at next scr refresh
            key_p_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_7.status == STARTED and not waitOnFlip:
            theseKeys = key_p_7.getKeys(keyList=['space'], waitRelease=False)
            _key_p_7_allKeys.extend(theseKeys)
            if len(_key_p_7_allKeys):
                key_p_7.keys = [key.name for key in _key_p_7_allKeys]  # storing all keys
                key_p_7.rt = [key.rt for key in _key_p_7_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_7.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_7.keys) > number_keys_p_7:
                
                # update our count of the number of keys pressed
                number_keys_p_7 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_33.getRating() or not slider_34.getRating() or not slider_35.getRating() or not slider_36.getRating() or not slider_37.getRating() or not slider_63.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_5* updates
        if message_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_5.frameNStart = frameN  # exact frame index
            message_5.tStart = t  # local t and not account for scr refresh
            message_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_5, 'tStartRefresh')  # time at next scr refresh
            message_5.setAutoDraw(True)
        if message_5.status == STARTED:  # only update if drawing
            message_5.setText(msg_p, log=False)
        if qtext==1:
            quest_1 = 'How appropriate is her reaction in the video?'
            quest_2 = 'Based on what you saw in the video, how likeable do you think she is?'
            quest_3 = 'What does the other person think of her after her reaction?'
            quest_4 = 'How upset does she look in the video?'
            quest_5= 'Is she showing the other person how she feels?'
            quest_6= 'How does she feel about herself as a person?'
        elif qtext==2:
            quest_1 = 'How appropriate is his reaction in the video?'
            quest_2 = 'Based on what you saw in the video, how likeable do you think he is?'
            quest_3 = 'What does the other person think of him after his reaction?'
            quest_4 = 'How upset does he look in the video?'
            quest_5= 'Is he showing the other person how he feels?'
            quest_6= 'How does he feel about himself as a person?'
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in I2_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "I2_O2"-------
    for thisComponent in I2_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_5.started', Question_5.tStartRefresh)
    trials.addData('Question_5.stopped', Question_5.tStopRefresh)
    trials.addData('Q1_5.started', Q1_5.tStartRefresh)
    trials.addData('Q1_5.stopped', Q1_5.tStopRefresh)
    trials.addData('slider_33.response', slider_33.getRating())
    trials.addData('slider_33.rt', slider_33.getRT())
    trials.addData('slider_33.started', slider_33.tStartRefresh)
    trials.addData('slider_33.stopped', slider_33.tStopRefresh)
    trials.addData('Q_4.started', Q_4.tStartRefresh)
    trials.addData('Q_4.stopped', Q_4.tStopRefresh)
    trials.addData('slider_34.response', slider_34.getRating())
    trials.addData('slider_34.rt', slider_34.getRT())
    trials.addData('slider_34.started', slider_34.tStartRefresh)
    trials.addData('slider_34.stopped', slider_34.tStopRefresh)
    trials.addData('Q3_4.started', Q3_4.tStartRefresh)
    trials.addData('Q3_4.stopped', Q3_4.tStopRefresh)
    trials.addData('slider_35.response', slider_35.getRating())
    trials.addData('slider_35.rt', slider_35.getRT())
    trials.addData('slider_35.started', slider_35.tStartRefresh)
    trials.addData('slider_35.stopped', slider_35.tStopRefresh)
    trials.addData('Q4_4.started', Q4_4.tStartRefresh)
    trials.addData('Q4_4.stopped', Q4_4.tStopRefresh)
    trials.addData('slider_36.response', slider_36.getRating())
    trials.addData('slider_36.rt', slider_36.getRT())
    trials.addData('slider_36.started', slider_36.tStartRefresh)
    trials.addData('slider_36.stopped', slider_36.tStopRefresh)
    trials.addData('Q5_4.started', Q5_4.tStartRefresh)
    trials.addData('Q5_4.stopped', Q5_4.tStopRefresh)
    trials.addData('slider_37.response', slider_37.getRating())
    trials.addData('slider_37.rt', slider_37.getRT())
    trials.addData('slider_37.started', slider_37.tStartRefresh)
    trials.addData('slider_37.stopped', slider_37.tStopRefresh)
    trials.addData('Q6_4.started', Q6_4.tStartRefresh)
    trials.addData('Q6_4.stopped', Q6_4.tStopRefresh)
    trials.addData('slider_63.response', slider_63.getRating())
    trials.addData('slider_63.rt', slider_63.getRT())
    trials.addData('slider_63.started', slider_63.tStartRefresh)
    trials.addData('slider_63.stopped', slider_63.tStopRefresh)
    trials.addData('pressSpace_9.started', pressSpace_9.tStartRefresh)
    trials.addData('pressSpace_9.stopped', pressSpace_9.tStopRefresh)
    # check responses
    if key_p_7.keys in ['', [], None]:  # No response was made
        key_p_7.keys = None
    trials.addData('key_p_7.keys',key_p_7.keys)
    if key_p_7.keys != None:  # we had a response
        trials.addData('key_p_7.rt', key_p_7.rt)
    trials.addData('key_p_7.started', key_p_7.tStartRefresh)
    trials.addData('key_p_7.stopped', key_p_7.tStopRefresh)
    trials.addData('message_5.started', message_5.tStartRefresh)
    trials.addData('message_5.stopped', message_5.tStopRefresh)
    # the Routine "I2_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "E1_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider.reset()
    slider_2.reset()
    slider_h.reset()
    slider_3.reset()
    slider_4.reset()
    slider_5.reset()
    key_p.keys = []
    key_p.rt = []
    _key_p_allKeys = []
    number_keys_p = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_13 = ''
    
    # keep track of which components have finished
    E1_O1Components = [text_2, feelQ, Angry, slider, Bored, slider_2, Sad, slider_h, Embarrassed, slider_3, Disgusted, slider_4, Shy, slider_5, pressSpace_3, key_p, message]
    for thisComponent in E1_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    E1_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "E1_O1"-------
    while continueRoutine:
        # get current time
        t = E1_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=E1_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:  # only update if drawing
            text_2.setText(quest_13, log=False)
        
        # *feelQ* updates
        if feelQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ.frameNStart = frameN  # exact frame index
            feelQ.tStart = t  # local t and not account for scr refresh
            feelQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ, 'tStartRefresh')  # time at next scr refresh
            feelQ.setAutoDraw(True)
        
        # *Angry* updates
        if Angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Angry.frameNStart = frameN  # exact frame index
            Angry.tStart = t  # local t and not account for scr refresh
            Angry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Angry, 'tStartRefresh')  # time at next scr refresh
            Angry.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *Bored* updates
        if Bored.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bored.frameNStart = frameN  # exact frame index
            Bored.tStart = t  # local t and not account for scr refresh
            Bored.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bored, 'tStartRefresh')  # time at next scr refresh
            Bored.setAutoDraw(True)
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        
        # *Sad* updates
        if Sad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Sad.frameNStart = frameN  # exact frame index
            Sad.tStart = t  # local t and not account for scr refresh
            Sad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sad, 'tStartRefresh')  # time at next scr refresh
            Sad.setAutoDraw(True)
        
        # *slider_h* updates
        if slider_h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_h.frameNStart = frameN  # exact frame index
            slider_h.tStart = t  # local t and not account for scr refresh
            slider_h.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_h, 'tStartRefresh')  # time at next scr refresh
            slider_h.setAutoDraw(True)
        
        # *Embarrassed* updates
        if Embarrassed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Embarrassed.frameNStart = frameN  # exact frame index
            Embarrassed.tStart = t  # local t and not account for scr refresh
            Embarrassed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Embarrassed, 'tStartRefresh')  # time at next scr refresh
            Embarrassed.setAutoDraw(True)
        
        # *slider_3* updates
        if slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_3.frameNStart = frameN  # exact frame index
            slider_3.tStart = t  # local t and not account for scr refresh
            slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
            slider_3.setAutoDraw(True)
        
        # *Disgusted* updates
        if Disgusted.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Disgusted.frameNStart = frameN  # exact frame index
            Disgusted.tStart = t  # local t and not account for scr refresh
            Disgusted.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disgusted, 'tStartRefresh')  # time at next scr refresh
            Disgusted.setAutoDraw(True)
        
        # *slider_4* updates
        if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_4.frameNStart = frameN  # exact frame index
            slider_4.tStart = t  # local t and not account for scr refresh
            slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
            slider_4.setAutoDraw(True)
        
        # *Shy* updates
        if Shy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Shy.frameNStart = frameN  # exact frame index
            Shy.tStart = t  # local t and not account for scr refresh
            Shy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Shy, 'tStartRefresh')  # time at next scr refresh
            Shy.setAutoDraw(True)
        
        # *slider_5* updates
        if slider_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_5.frameNStart = frameN  # exact frame index
            slider_5.tStart = t  # local t and not account for scr refresh
            slider_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
            slider_5.setAutoDraw(True)
        
        # *pressSpace_3* updates
        if pressSpace_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_3.frameNStart = frameN  # exact frame index
            pressSpace_3.tStart = t  # local t and not account for scr refresh
            pressSpace_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_3, 'tStartRefresh')  # time at next scr refresh
            pressSpace_3.setAutoDraw(True)
        if pressSpace_3.status == STARTED:  # only update if drawing
            pressSpace_3.setText(spaceText, log=False)
        
        # *key_p* updates
        waitOnFlip = False
        if key_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p.frameNStart = frameN  # exact frame index
            key_p.tStart = t  # local t and not account for scr refresh
            key_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p, 'tStartRefresh')  # time at next scr refresh
            key_p.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p.status == STARTED and not waitOnFlip:
            theseKeys = key_p.getKeys(keyList=['space'], waitRelease=False)
            _key_p_allKeys.extend(theseKeys)
            if len(_key_p_allKeys):
                key_p.keys = [key.name for key in _key_p_allKeys]  # storing all keys
                key_p.rt = [key.rt for key in _key_p_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p.keys) > number_keys_p:
                
                # update our count of the number of keys pressed
                number_keys_p += 1
                
                # if one of the sliders is empty (missing information)
                if not slider.getRating() or not slider_2.getRating() or not slider_3.getRating() or not slider_4.getRating() or not slider_5.getRating() or not slider_h.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message* updates
        if message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message.frameNStart = frameN  # exact frame index
            message.tStart = t  # local t and not account for scr refresh
            message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message, 'tStartRefresh')  # time at next scr refresh
            message.setAutoDraw(True)
        if message.status == STARTED:  # only update if drawing
            message.setText(msg_p, log=False)
        if qtext==1:
            quest_13 = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
        elif qtext==2:
             quest_13 = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in E1_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "E1_O1"-------
    for thisComponent in E1_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    trials.addData('feelQ.started', feelQ.tStartRefresh)
    trials.addData('feelQ.stopped', feelQ.tStopRefresh)
    trials.addData('Angry.started', Angry.tStartRefresh)
    trials.addData('Angry.stopped', Angry.tStopRefresh)
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    trials.addData('slider.started', slider.tStartRefresh)
    trials.addData('slider.stopped', slider.tStopRefresh)
    trials.addData('Bored.started', Bored.tStartRefresh)
    trials.addData('Bored.stopped', Bored.tStopRefresh)
    trials.addData('slider_2.response', slider_2.getRating())
    trials.addData('slider_2.rt', slider_2.getRT())
    trials.addData('slider_2.started', slider_2.tStartRefresh)
    trials.addData('slider_2.stopped', slider_2.tStopRefresh)
    trials.addData('Sad.started', Sad.tStartRefresh)
    trials.addData('Sad.stopped', Sad.tStopRefresh)
    trials.addData('slider_h.response', slider_h.getRating())
    trials.addData('slider_h.rt', slider_h.getRT())
    trials.addData('slider_h.started', slider_h.tStartRefresh)
    trials.addData('slider_h.stopped', slider_h.tStopRefresh)
    trials.addData('Embarrassed.started', Embarrassed.tStartRefresh)
    trials.addData('Embarrassed.stopped', Embarrassed.tStopRefresh)
    trials.addData('slider_3.response', slider_3.getRating())
    trials.addData('slider_3.rt', slider_3.getRT())
    trials.addData('slider_3.started', slider_3.tStartRefresh)
    trials.addData('slider_3.stopped', slider_3.tStopRefresh)
    trials.addData('Disgusted.started', Disgusted.tStartRefresh)
    trials.addData('Disgusted.stopped', Disgusted.tStopRefresh)
    trials.addData('slider_4.response', slider_4.getRating())
    trials.addData('slider_4.rt', slider_4.getRT())
    trials.addData('slider_4.started', slider_4.tStartRefresh)
    trials.addData('slider_4.stopped', slider_4.tStopRefresh)
    trials.addData('Shy.started', Shy.tStartRefresh)
    trials.addData('Shy.stopped', Shy.tStopRefresh)
    trials.addData('slider_5.response', slider_5.getRating())
    trials.addData('slider_5.rt', slider_5.getRT())
    trials.addData('slider_5.started', slider_5.tStartRefresh)
    trials.addData('slider_5.stopped', slider_5.tStopRefresh)
    trials.addData('pressSpace_3.started', pressSpace_3.tStartRefresh)
    trials.addData('pressSpace_3.stopped', pressSpace_3.tStopRefresh)
    # check responses
    if key_p.keys in ['', [], None]:  # No response was made
        key_p.keys = None
    trials.addData('key_p.keys',key_p.keys)
    if key_p.keys != None:  # we had a response
        trials.addData('key_p.rt', key_p.rt)
    trials.addData('key_p.started', key_p.tStartRefresh)
    trials.addData('key_p.stopped', key_p.tStopRefresh)
    trials.addData('message.started', message.tStartRefresh)
    trials.addData('message.stopped', message.tStopRefresh)
    # the Routine "E1_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "E2_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_39.reset()
    slider_21.reset()
    slider_22.reset()
    slider_26.reset()
    slider_23.reset()
    slider_24.reset()
    slider_25.reset()
    key_p_5.keys = []
    key_p_5.rt = []
    _key_p_5_allKeys = []
    number_keys_p_5 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with questions on the video.'
    # keep track of which components have finished
    E2_O1Components = [feelQ_2, Uninterested_1, slider_39, Unhappy, slider_21, Anxious_3, slider_22, Tired_3, slider_26, Ashamed_3, slider_23, Fearful_3, slider_24, Guilty_3, slider_25, pressSpace_7, key_p_5, message_6]
    for thisComponent in E2_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    E2_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "E2_O1"-------
    while continueRoutine:
        # get current time
        t = E2_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=E2_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feelQ_2* updates
        if feelQ_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ_2.frameNStart = frameN  # exact frame index
            feelQ_2.tStart = t  # local t and not account for scr refresh
            feelQ_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ_2, 'tStartRefresh')  # time at next scr refresh
            feelQ_2.setAutoDraw(True)
        
        # *Uninterested_1* updates
        if Uninterested_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Uninterested_1.frameNStart = frameN  # exact frame index
            Uninterested_1.tStart = t  # local t and not account for scr refresh
            Uninterested_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Uninterested_1, 'tStartRefresh')  # time at next scr refresh
            Uninterested_1.setAutoDraw(True)
        
        # *slider_39* updates
        if slider_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_39.frameNStart = frameN  # exact frame index
            slider_39.tStart = t  # local t and not account for scr refresh
            slider_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_39, 'tStartRefresh')  # time at next scr refresh
            slider_39.setAutoDraw(True)
        
        # *Unhappy* updates
        if Unhappy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Unhappy.frameNStart = frameN  # exact frame index
            Unhappy.tStart = t  # local t and not account for scr refresh
            Unhappy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Unhappy, 'tStartRefresh')  # time at next scr refresh
            Unhappy.setAutoDraw(True)
        
        # *slider_21* updates
        if slider_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_21.frameNStart = frameN  # exact frame index
            slider_21.tStart = t  # local t and not account for scr refresh
            slider_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_21, 'tStartRefresh')  # time at next scr refresh
            slider_21.setAutoDraw(True)
        
        # *Anxious_3* updates
        if Anxious_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Anxious_3.frameNStart = frameN  # exact frame index
            Anxious_3.tStart = t  # local t and not account for scr refresh
            Anxious_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Anxious_3, 'tStartRefresh')  # time at next scr refresh
            Anxious_3.setAutoDraw(True)
        
        # *slider_22* updates
        if slider_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_22.frameNStart = frameN  # exact frame index
            slider_22.tStart = t  # local t and not account for scr refresh
            slider_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_22, 'tStartRefresh')  # time at next scr refresh
            slider_22.setAutoDraw(True)
        
        # *Tired_3* updates
        if Tired_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tired_3.frameNStart = frameN  # exact frame index
            Tired_3.tStart = t  # local t and not account for scr refresh
            Tired_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tired_3, 'tStartRefresh')  # time at next scr refresh
            Tired_3.setAutoDraw(True)
        
        # *slider_26* updates
        if slider_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_26.frameNStart = frameN  # exact frame index
            slider_26.tStart = t  # local t and not account for scr refresh
            slider_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_26, 'tStartRefresh')  # time at next scr refresh
            slider_26.setAutoDraw(True)
        
        # *Ashamed_3* updates
        if Ashamed_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ashamed_3.frameNStart = frameN  # exact frame index
            Ashamed_3.tStart = t  # local t and not account for scr refresh
            Ashamed_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ashamed_3, 'tStartRefresh')  # time at next scr refresh
            Ashamed_3.setAutoDraw(True)
        
        # *slider_23* updates
        if slider_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_23.frameNStart = frameN  # exact frame index
            slider_23.tStart = t  # local t and not account for scr refresh
            slider_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_23, 'tStartRefresh')  # time at next scr refresh
            slider_23.setAutoDraw(True)
        
        # *Fearful_3* updates
        if Fearful_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fearful_3.frameNStart = frameN  # exact frame index
            Fearful_3.tStart = t  # local t and not account for scr refresh
            Fearful_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fearful_3, 'tStartRefresh')  # time at next scr refresh
            Fearful_3.setAutoDraw(True)
        
        # *slider_24* updates
        if slider_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_24.frameNStart = frameN  # exact frame index
            slider_24.tStart = t  # local t and not account for scr refresh
            slider_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_24, 'tStartRefresh')  # time at next scr refresh
            slider_24.setAutoDraw(True)
        
        # *Guilty_3* updates
        if Guilty_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Guilty_3.frameNStart = frameN  # exact frame index
            Guilty_3.tStart = t  # local t and not account for scr refresh
            Guilty_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Guilty_3, 'tStartRefresh')  # time at next scr refresh
            Guilty_3.setAutoDraw(True)
        
        # *slider_25* updates
        if slider_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_25.frameNStart = frameN  # exact frame index
            slider_25.tStart = t  # local t and not account for scr refresh
            slider_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_25, 'tStartRefresh')  # time at next scr refresh
            slider_25.setAutoDraw(True)
        
        # *pressSpace_7* updates
        if pressSpace_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_7.frameNStart = frameN  # exact frame index
            pressSpace_7.tStart = t  # local t and not account for scr refresh
            pressSpace_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_7, 'tStartRefresh')  # time at next scr refresh
            pressSpace_7.setAutoDraw(True)
        if pressSpace_7.status == STARTED:  # only update if drawing
            pressSpace_7.setText(spaceText, log=False)
        
        # *key_p_5* updates
        waitOnFlip = False
        if key_p_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_5.frameNStart = frameN  # exact frame index
            key_p_5.tStart = t  # local t and not account for scr refresh
            key_p_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_5, 'tStartRefresh')  # time at next scr refresh
            key_p_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_5.status == STARTED and not waitOnFlip:
            theseKeys = key_p_5.getKeys(keyList=['space'], waitRelease=False)
            _key_p_5_allKeys.extend(theseKeys)
            if len(_key_p_5_allKeys):
                key_p_5.keys = [key.name for key in _key_p_5_allKeys]  # storing all keys
                key_p_5.rt = [key.rt for key in _key_p_5_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p_5.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_5.keys) > number_keys_p_5:
                
                # update our count of the number of keys pressed
                number_keys_p_5 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_21.getRating() or not slider_22.getRating() or not slider_23.getRating() or not slider_24.getRating() or not slider_25.getRating() or not slider_26.getRating() or not slider_39.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_6* updates
        if message_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_6.frameNStart = frameN  # exact frame index
            message_6.tStart = t  # local t and not account for scr refresh
            message_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_6, 'tStartRefresh')  # time at next scr refresh
            message_6.setAutoDraw(True)
        if message_6.status == STARTED:  # only update if drawing
            message_6.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in E2_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "E2_O1"-------
    for thisComponent in E2_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feelQ_2.started', feelQ_2.tStartRefresh)
    trials.addData('feelQ_2.stopped', feelQ_2.tStopRefresh)
    trials.addData('Uninterested_1.started', Uninterested_1.tStartRefresh)
    trials.addData('Uninterested_1.stopped', Uninterested_1.tStopRefresh)
    trials.addData('slider_39.response', slider_39.getRating())
    trials.addData('slider_39.rt', slider_39.getRT())
    trials.addData('slider_39.started', slider_39.tStartRefresh)
    trials.addData('slider_39.stopped', slider_39.tStopRefresh)
    trials.addData('Unhappy.started', Unhappy.tStartRefresh)
    trials.addData('Unhappy.stopped', Unhappy.tStopRefresh)
    trials.addData('slider_21.response', slider_21.getRating())
    trials.addData('slider_21.rt', slider_21.getRT())
    trials.addData('slider_21.started', slider_21.tStartRefresh)
    trials.addData('slider_21.stopped', slider_21.tStopRefresh)
    trials.addData('Anxious_3.started', Anxious_3.tStartRefresh)
    trials.addData('Anxious_3.stopped', Anxious_3.tStopRefresh)
    trials.addData('slider_22.response', slider_22.getRating())
    trials.addData('slider_22.rt', slider_22.getRT())
    trials.addData('slider_22.started', slider_22.tStartRefresh)
    trials.addData('slider_22.stopped', slider_22.tStopRefresh)
    trials.addData('Tired_3.started', Tired_3.tStartRefresh)
    trials.addData('Tired_3.stopped', Tired_3.tStopRefresh)
    trials.addData('slider_26.response', slider_26.getRating())
    trials.addData('slider_26.rt', slider_26.getRT())
    trials.addData('slider_26.started', slider_26.tStartRefresh)
    trials.addData('slider_26.stopped', slider_26.tStopRefresh)
    trials.addData('Ashamed_3.started', Ashamed_3.tStartRefresh)
    trials.addData('Ashamed_3.stopped', Ashamed_3.tStopRefresh)
    trials.addData('slider_23.response', slider_23.getRating())
    trials.addData('slider_23.rt', slider_23.getRT())
    trials.addData('slider_23.started', slider_23.tStartRefresh)
    trials.addData('slider_23.stopped', slider_23.tStopRefresh)
    trials.addData('Fearful_3.started', Fearful_3.tStartRefresh)
    trials.addData('Fearful_3.stopped', Fearful_3.tStopRefresh)
    trials.addData('slider_24.response', slider_24.getRating())
    trials.addData('slider_24.rt', slider_24.getRT())
    trials.addData('slider_24.started', slider_24.tStartRefresh)
    trials.addData('slider_24.stopped', slider_24.tStopRefresh)
    trials.addData('Guilty_3.started', Guilty_3.tStartRefresh)
    trials.addData('Guilty_3.stopped', Guilty_3.tStopRefresh)
    trials.addData('slider_25.response', slider_25.getRating())
    trials.addData('slider_25.rt', slider_25.getRT())
    trials.addData('slider_25.started', slider_25.tStartRefresh)
    trials.addData('slider_25.stopped', slider_25.tStopRefresh)
    trials.addData('pressSpace_7.started', pressSpace_7.tStartRefresh)
    trials.addData('pressSpace_7.stopped', pressSpace_7.tStopRefresh)
    # check responses
    if key_p_5.keys in ['', [], None]:  # No response was made
        key_p_5.keys = None
    trials.addData('key_p_5.keys',key_p_5.keys)
    if key_p_5.keys != None:  # we had a response
        trials.addData('key_p_5.rt', key_p_5.rt)
    trials.addData('key_p_5.started', key_p_5.tStartRefresh)
    trials.addData('key_p_5.stopped', key_p_5.tStopRefresh)
    trials.addData('message_6.started', message_6.tStartRefresh)
    trials.addData('message_6.stopped', message_6.tStopRefresh)
    # the Routine "E2_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "E1_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_27.reset()
    slider_28.reset()
    slider_32.reset()
    slider_29.reset()
    slider_30.reset()
    slider_31.reset()
    key_p_6.keys = []
    key_p_6.rt = []
    _key_p_6_allKeys = []
    number_keys_p_6 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with your impressions.'
    quest_13 = ''
    
    # keep track of which components have finished
    E1_O2Components = [text_5, feelQ_3, Guilty_5, slider_27, Fearful_4, slider_28, Ashamed_5, slider_32, Tired_6, slider_29, Anxious_4, slider_30, Unhappy_4, slider_31, pressSpace_8, key_p_6, message_7]
    for thisComponent in E1_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    E1_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "E1_O2"-------
    while continueRoutine:
        # get current time
        t = E1_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=E1_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:  # only update if drawing
            text_5.setText(quest_13, log=False)
        
        # *feelQ_3* updates
        if feelQ_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ_3.frameNStart = frameN  # exact frame index
            feelQ_3.tStart = t  # local t and not account for scr refresh
            feelQ_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ_3, 'tStartRefresh')  # time at next scr refresh
            feelQ_3.setAutoDraw(True)
        
        # *Guilty_5* updates
        if Guilty_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Guilty_5.frameNStart = frameN  # exact frame index
            Guilty_5.tStart = t  # local t and not account for scr refresh
            Guilty_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Guilty_5, 'tStartRefresh')  # time at next scr refresh
            Guilty_5.setAutoDraw(True)
        
        # *slider_27* updates
        if slider_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_27.frameNStart = frameN  # exact frame index
            slider_27.tStart = t  # local t and not account for scr refresh
            slider_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_27, 'tStartRefresh')  # time at next scr refresh
            slider_27.setAutoDraw(True)
        
        # *Fearful_4* updates
        if Fearful_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fearful_4.frameNStart = frameN  # exact frame index
            Fearful_4.tStart = t  # local t and not account for scr refresh
            Fearful_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fearful_4, 'tStartRefresh')  # time at next scr refresh
            Fearful_4.setAutoDraw(True)
        
        # *slider_28* updates
        if slider_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_28.frameNStart = frameN  # exact frame index
            slider_28.tStart = t  # local t and not account for scr refresh
            slider_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_28, 'tStartRefresh')  # time at next scr refresh
            slider_28.setAutoDraw(True)
        
        # *Ashamed_5* updates
        if Ashamed_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ashamed_5.frameNStart = frameN  # exact frame index
            Ashamed_5.tStart = t  # local t and not account for scr refresh
            Ashamed_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ashamed_5, 'tStartRefresh')  # time at next scr refresh
            Ashamed_5.setAutoDraw(True)
        
        # *slider_32* updates
        if slider_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_32.frameNStart = frameN  # exact frame index
            slider_32.tStart = t  # local t and not account for scr refresh
            slider_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_32, 'tStartRefresh')  # time at next scr refresh
            slider_32.setAutoDraw(True)
        
        # *Tired_6* updates
        if Tired_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tired_6.frameNStart = frameN  # exact frame index
            Tired_6.tStart = t  # local t and not account for scr refresh
            Tired_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tired_6, 'tStartRefresh')  # time at next scr refresh
            Tired_6.setAutoDraw(True)
        
        # *slider_29* updates
        if slider_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_29.frameNStart = frameN  # exact frame index
            slider_29.tStart = t  # local t and not account for scr refresh
            slider_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_29, 'tStartRefresh')  # time at next scr refresh
            slider_29.setAutoDraw(True)
        
        # *Anxious_4* updates
        if Anxious_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Anxious_4.frameNStart = frameN  # exact frame index
            Anxious_4.tStart = t  # local t and not account for scr refresh
            Anxious_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Anxious_4, 'tStartRefresh')  # time at next scr refresh
            Anxious_4.setAutoDraw(True)
        
        # *slider_30* updates
        if slider_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_30.frameNStart = frameN  # exact frame index
            slider_30.tStart = t  # local t and not account for scr refresh
            slider_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_30, 'tStartRefresh')  # time at next scr refresh
            slider_30.setAutoDraw(True)
        
        # *Unhappy_4* updates
        if Unhappy_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Unhappy_4.frameNStart = frameN  # exact frame index
            Unhappy_4.tStart = t  # local t and not account for scr refresh
            Unhappy_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Unhappy_4, 'tStartRefresh')  # time at next scr refresh
            Unhappy_4.setAutoDraw(True)
        
        # *slider_31* updates
        if slider_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_31.frameNStart = frameN  # exact frame index
            slider_31.tStart = t  # local t and not account for scr refresh
            slider_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_31, 'tStartRefresh')  # time at next scr refresh
            slider_31.setAutoDraw(True)
        
        # *pressSpace_8* updates
        if pressSpace_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_8.frameNStart = frameN  # exact frame index
            pressSpace_8.tStart = t  # local t and not account for scr refresh
            pressSpace_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_8, 'tStartRefresh')  # time at next scr refresh
            pressSpace_8.setAutoDraw(True)
        if pressSpace_8.status == STARTED:  # only update if drawing
            pressSpace_8.setText(spaceText, log=False)
        
        # *key_p_6* updates
        waitOnFlip = False
        if key_p_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_6.frameNStart = frameN  # exact frame index
            key_p_6.tStart = t  # local t and not account for scr refresh
            key_p_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_6, 'tStartRefresh')  # time at next scr refresh
            key_p_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_6.status == STARTED and not waitOnFlip:
            theseKeys = key_p_6.getKeys(keyList=['space'], waitRelease=False)
            _key_p_6_allKeys.extend(theseKeys)
            if len(_key_p_6_allKeys):
                key_p_6.keys = [key.name for key in _key_p_6_allKeys]  # storing all keys
                key_p_6.rt = [key.rt for key in _key_p_6_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_6.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_6.keys) > number_keys_p_6:
                
                # update our count of the number of keys pressed
                number_keys_p_6 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_27.getRating() or not slider_28.getRating() or not slider_29.getRating() or not slider_30.getRating() or not slider_31.getRating() or not slider_32.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_7* updates
        if message_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_7.frameNStart = frameN  # exact frame index
            message_7.tStart = t  # local t and not account for scr refresh
            message_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_7, 'tStartRefresh')  # time at next scr refresh
            message_7.setAutoDraw(True)
        if message_7.status == STARTED:  # only update if drawing
            message_7.setText(msg_p, log=False)
        if qtext==1:
            quest_13 = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
        elif qtext==2:
             quest_13 = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in E1_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "E1_O2"-------
    for thisComponent in E1_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    trials.addData('feelQ_3.started', feelQ_3.tStartRefresh)
    trials.addData('feelQ_3.stopped', feelQ_3.tStopRefresh)
    trials.addData('Guilty_5.started', Guilty_5.tStartRefresh)
    trials.addData('Guilty_5.stopped', Guilty_5.tStopRefresh)
    trials.addData('slider_27.response', slider_27.getRating())
    trials.addData('slider_27.rt', slider_27.getRT())
    trials.addData('slider_27.started', slider_27.tStartRefresh)
    trials.addData('slider_27.stopped', slider_27.tStopRefresh)
    trials.addData('Fearful_4.started', Fearful_4.tStartRefresh)
    trials.addData('Fearful_4.stopped', Fearful_4.tStopRefresh)
    trials.addData('slider_28.response', slider_28.getRating())
    trials.addData('slider_28.rt', slider_28.getRT())
    trials.addData('slider_28.started', slider_28.tStartRefresh)
    trials.addData('slider_28.stopped', slider_28.tStopRefresh)
    trials.addData('Ashamed_5.started', Ashamed_5.tStartRefresh)
    trials.addData('Ashamed_5.stopped', Ashamed_5.tStopRefresh)
    trials.addData('slider_32.response', slider_32.getRating())
    trials.addData('slider_32.rt', slider_32.getRT())
    trials.addData('slider_32.started', slider_32.tStartRefresh)
    trials.addData('slider_32.stopped', slider_32.tStopRefresh)
    trials.addData('Tired_6.started', Tired_6.tStartRefresh)
    trials.addData('Tired_6.stopped', Tired_6.tStopRefresh)
    trials.addData('slider_29.response', slider_29.getRating())
    trials.addData('slider_29.rt', slider_29.getRT())
    trials.addData('slider_29.started', slider_29.tStartRefresh)
    trials.addData('slider_29.stopped', slider_29.tStopRefresh)
    trials.addData('Anxious_4.started', Anxious_4.tStartRefresh)
    trials.addData('Anxious_4.stopped', Anxious_4.tStopRefresh)
    trials.addData('slider_30.response', slider_30.getRating())
    trials.addData('slider_30.rt', slider_30.getRT())
    trials.addData('slider_30.started', slider_30.tStartRefresh)
    trials.addData('slider_30.stopped', slider_30.tStopRefresh)
    trials.addData('Unhappy_4.started', Unhappy_4.tStartRefresh)
    trials.addData('Unhappy_4.stopped', Unhappy_4.tStopRefresh)
    trials.addData('slider_31.response', slider_31.getRating())
    trials.addData('slider_31.rt', slider_31.getRT())
    trials.addData('slider_31.started', slider_31.tStartRefresh)
    trials.addData('slider_31.stopped', slider_31.tStopRefresh)
    trials.addData('pressSpace_8.started', pressSpace_8.tStartRefresh)
    trials.addData('pressSpace_8.stopped', pressSpace_8.tStopRefresh)
    # check responses
    if key_p_6.keys in ['', [], None]:  # No response was made
        key_p_6.keys = None
    trials.addData('key_p_6.keys',key_p_6.keys)
    if key_p_6.keys != None:  # we had a response
        trials.addData('key_p_6.rt', key_p_6.rt)
    trials.addData('key_p_6.started', key_p_6.tStartRefresh)
    trials.addData('key_p_6.stopped', key_p_6.tStopRefresh)
    trials.addData('message_7.started', message_7.tStartRefresh)
    trials.addData('message_7.stopped', message_7.tStopRefresh)
    # the Routine "E1_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "E2_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_46.reset()
    slider_40.reset()
    slider_41.reset()
    slider_42.reset()
    slider_43.reset()
    slider_44.reset()
    slider_45.reset()
    key_p_8.keys = []
    key_p_8.rt = []
    _key_p_8_allKeys = []
    number_keys_p_8 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with questions on the video.'
    # keep track of which components have finished
    E2_O2Components = [feelQ_5, Shy_5, slider_46, Disgusted_5, slider_40, Embarrassed_6, slider_41, Sad_6, slider_42, Bored_6, slider_43, Angry_6, slider_44, Uninterested_6, slider_45, pressSpace_10, key_p_8, message_9]
    for thisComponent in E2_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    E2_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "E2_O2"-------
    while continueRoutine:
        # get current time
        t = E2_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=E2_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feelQ_5* updates
        if feelQ_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ_5.frameNStart = frameN  # exact frame index
            feelQ_5.tStart = t  # local t and not account for scr refresh
            feelQ_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ_5, 'tStartRefresh')  # time at next scr refresh
            feelQ_5.setAutoDraw(True)
        
        # *Shy_5* updates
        if Shy_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Shy_5.frameNStart = frameN  # exact frame index
            Shy_5.tStart = t  # local t and not account for scr refresh
            Shy_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Shy_5, 'tStartRefresh')  # time at next scr refresh
            Shy_5.setAutoDraw(True)
        
        # *slider_46* updates
        if slider_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_46.frameNStart = frameN  # exact frame index
            slider_46.tStart = t  # local t and not account for scr refresh
            slider_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_46, 'tStartRefresh')  # time at next scr refresh
            slider_46.setAutoDraw(True)
        
        # *Disgusted_5* updates
        if Disgusted_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Disgusted_5.frameNStart = frameN  # exact frame index
            Disgusted_5.tStart = t  # local t and not account for scr refresh
            Disgusted_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disgusted_5, 'tStartRefresh')  # time at next scr refresh
            Disgusted_5.setAutoDraw(True)
        
        # *slider_40* updates
        if slider_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_40.frameNStart = frameN  # exact frame index
            slider_40.tStart = t  # local t and not account for scr refresh
            slider_40.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_40, 'tStartRefresh')  # time at next scr refresh
            slider_40.setAutoDraw(True)
        
        # *Embarrassed_6* updates
        if Embarrassed_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Embarrassed_6.frameNStart = frameN  # exact frame index
            Embarrassed_6.tStart = t  # local t and not account for scr refresh
            Embarrassed_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Embarrassed_6, 'tStartRefresh')  # time at next scr refresh
            Embarrassed_6.setAutoDraw(True)
        
        # *slider_41* updates
        if slider_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_41.frameNStart = frameN  # exact frame index
            slider_41.tStart = t  # local t and not account for scr refresh
            slider_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_41, 'tStartRefresh')  # time at next scr refresh
            slider_41.setAutoDraw(True)
        
        # *Sad_6* updates
        if Sad_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Sad_6.frameNStart = frameN  # exact frame index
            Sad_6.tStart = t  # local t and not account for scr refresh
            Sad_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sad_6, 'tStartRefresh')  # time at next scr refresh
            Sad_6.setAutoDraw(True)
        
        # *slider_42* updates
        if slider_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_42.frameNStart = frameN  # exact frame index
            slider_42.tStart = t  # local t and not account for scr refresh
            slider_42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_42, 'tStartRefresh')  # time at next scr refresh
            slider_42.setAutoDraw(True)
        
        # *Bored_6* updates
        if Bored_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bored_6.frameNStart = frameN  # exact frame index
            Bored_6.tStart = t  # local t and not account for scr refresh
            Bored_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bored_6, 'tStartRefresh')  # time at next scr refresh
            Bored_6.setAutoDraw(True)
        
        # *slider_43* updates
        if slider_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_43.frameNStart = frameN  # exact frame index
            slider_43.tStart = t  # local t and not account for scr refresh
            slider_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_43, 'tStartRefresh')  # time at next scr refresh
            slider_43.setAutoDraw(True)
        
        # *Angry_6* updates
        if Angry_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Angry_6.frameNStart = frameN  # exact frame index
            Angry_6.tStart = t  # local t and not account for scr refresh
            Angry_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Angry_6, 'tStartRefresh')  # time at next scr refresh
            Angry_6.setAutoDraw(True)
        
        # *slider_44* updates
        if slider_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_44.frameNStart = frameN  # exact frame index
            slider_44.tStart = t  # local t and not account for scr refresh
            slider_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_44, 'tStartRefresh')  # time at next scr refresh
            slider_44.setAutoDraw(True)
        
        # *Uninterested_6* updates
        if Uninterested_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Uninterested_6.frameNStart = frameN  # exact frame index
            Uninterested_6.tStart = t  # local t and not account for scr refresh
            Uninterested_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Uninterested_6, 'tStartRefresh')  # time at next scr refresh
            Uninterested_6.setAutoDraw(True)
        
        # *slider_45* updates
        if slider_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_45.frameNStart = frameN  # exact frame index
            slider_45.tStart = t  # local t and not account for scr refresh
            slider_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_45, 'tStartRefresh')  # time at next scr refresh
            slider_45.setAutoDraw(True)
        
        # *pressSpace_10* updates
        if pressSpace_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_10.frameNStart = frameN  # exact frame index
            pressSpace_10.tStart = t  # local t and not account for scr refresh
            pressSpace_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_10, 'tStartRefresh')  # time at next scr refresh
            pressSpace_10.setAutoDraw(True)
        if pressSpace_10.status == STARTED:  # only update if drawing
            pressSpace_10.setText(spaceText, log=False)
        
        # *key_p_8* updates
        waitOnFlip = False
        if key_p_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_8.frameNStart = frameN  # exact frame index
            key_p_8.tStart = t  # local t and not account for scr refresh
            key_p_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_8, 'tStartRefresh')  # time at next scr refresh
            key_p_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_8.status == STARTED and not waitOnFlip:
            theseKeys = key_p_8.getKeys(keyList=['space'], waitRelease=False)
            _key_p_8_allKeys.extend(theseKeys)
            if len(_key_p_8_allKeys):
                key_p_8.keys = [key.name for key in _key_p_8_allKeys]  # storing all keys
                key_p_8.rt = [key.rt for key in _key_p_8_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_8.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_8.keys) > number_keys_p_8:
                
                # update our count of the number of keys pressed
                number_keys_p_8 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_40.getRating() or not slider_41.getRating() or not slider_42.getRating() or not slider_43.getRating() or not slider_44.getRating() or not slider_45.getRating() or not slider_46.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please report all your impressions, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_9* updates
        if message_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_9.frameNStart = frameN  # exact frame index
            message_9.tStart = t  # local t and not account for scr refresh
            message_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_9, 'tStartRefresh')  # time at next scr refresh
            message_9.setAutoDraw(True)
        if message_9.status == STARTED:  # only update if drawing
            message_9.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in E2_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "E2_O2"-------
    for thisComponent in E2_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feelQ_5.started', feelQ_5.tStartRefresh)
    trials.addData('feelQ_5.stopped', feelQ_5.tStopRefresh)
    trials.addData('Shy_5.started', Shy_5.tStartRefresh)
    trials.addData('Shy_5.stopped', Shy_5.tStopRefresh)
    trials.addData('slider_46.response', slider_46.getRating())
    trials.addData('slider_46.rt', slider_46.getRT())
    trials.addData('slider_46.started', slider_46.tStartRefresh)
    trials.addData('slider_46.stopped', slider_46.tStopRefresh)
    trials.addData('Disgusted_5.started', Disgusted_5.tStartRefresh)
    trials.addData('Disgusted_5.stopped', Disgusted_5.tStopRefresh)
    trials.addData('slider_40.response', slider_40.getRating())
    trials.addData('slider_40.rt', slider_40.getRT())
    trials.addData('slider_40.started', slider_40.tStartRefresh)
    trials.addData('slider_40.stopped', slider_40.tStopRefresh)
    trials.addData('Embarrassed_6.started', Embarrassed_6.tStartRefresh)
    trials.addData('Embarrassed_6.stopped', Embarrassed_6.tStopRefresh)
    trials.addData('slider_41.response', slider_41.getRating())
    trials.addData('slider_41.rt', slider_41.getRT())
    trials.addData('slider_41.started', slider_41.tStartRefresh)
    trials.addData('slider_41.stopped', slider_41.tStopRefresh)
    trials.addData('Sad_6.started', Sad_6.tStartRefresh)
    trials.addData('Sad_6.stopped', Sad_6.tStopRefresh)
    trials.addData('slider_42.response', slider_42.getRating())
    trials.addData('slider_42.rt', slider_42.getRT())
    trials.addData('slider_42.started', slider_42.tStartRefresh)
    trials.addData('slider_42.stopped', slider_42.tStopRefresh)
    trials.addData('Bored_6.started', Bored_6.tStartRefresh)
    trials.addData('Bored_6.stopped', Bored_6.tStopRefresh)
    trials.addData('slider_43.response', slider_43.getRating())
    trials.addData('slider_43.rt', slider_43.getRT())
    trials.addData('slider_43.started', slider_43.tStartRefresh)
    trials.addData('slider_43.stopped', slider_43.tStopRefresh)
    trials.addData('Angry_6.started', Angry_6.tStartRefresh)
    trials.addData('Angry_6.stopped', Angry_6.tStopRefresh)
    trials.addData('slider_44.response', slider_44.getRating())
    trials.addData('slider_44.rt', slider_44.getRT())
    trials.addData('slider_44.started', slider_44.tStartRefresh)
    trials.addData('slider_44.stopped', slider_44.tStopRefresh)
    trials.addData('Uninterested_6.started', Uninterested_6.tStartRefresh)
    trials.addData('Uninterested_6.stopped', Uninterested_6.tStopRefresh)
    trials.addData('slider_45.response', slider_45.getRating())
    trials.addData('slider_45.rt', slider_45.getRT())
    trials.addData('slider_45.started', slider_45.tStartRefresh)
    trials.addData('slider_45.stopped', slider_45.tStopRefresh)
    trials.addData('pressSpace_10.started', pressSpace_10.tStartRefresh)
    trials.addData('pressSpace_10.stopped', pressSpace_10.tStopRefresh)
    # check responses
    if key_p_8.keys in ['', [], None]:  # No response was made
        key_p_8.keys = None
    trials.addData('key_p_8.keys',key_p_8.keys)
    if key_p_8.keys != None:  # we had a response
        trials.addData('key_p_8.rt', key_p_8.rt)
    trials.addData('key_p_8.started', key_p_8.tStartRefresh)
    trials.addData('key_p_8.stopped', key_p_8.tStopRefresh)
    trials.addData('message_9.started', message_9.tStartRefresh)
    trials.addData('message_9.stopped', message_9.tStopRefresh)
    # the Routine "E2_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "P1_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_38.reset()
    slider_47.reset()
    slider_48.reset()
    slider_49.reset()
    key_p_9.keys = []
    key_p_9.rt = []
    _key_p_9_allKeys = []
    number_keys_p_9 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with the last questions on the video.'
    # keep track of which components have finished
    P1_O1Components = [Question_6, Q1_6, slider_38, Q_5, slider_47, Q3_5, slider_48, Q4_5, slider_49, pressSpace_11, key_p_9, message_8]
    for thisComponent in P1_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    P1_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "P1_O1"-------
    while continueRoutine:
        # get current time
        t = P1_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=P1_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_6* updates
        if Question_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_6.frameNStart = frameN  # exact frame index
            Question_6.tStart = t  # local t and not account for scr refresh
            Question_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_6, 'tStartRefresh')  # time at next scr refresh
            Question_6.setAutoDraw(True)
        
        # *Q1_6* updates
        if Q1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1_6.frameNStart = frameN  # exact frame index
            Q1_6.tStart = t  # local t and not account for scr refresh
            Q1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1_6, 'tStartRefresh')  # time at next scr refresh
            Q1_6.setAutoDraw(True)
        
        # *slider_38* updates
        if slider_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_38.frameNStart = frameN  # exact frame index
            slider_38.tStart = t  # local t and not account for scr refresh
            slider_38.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_38, 'tStartRefresh')  # time at next scr refresh
            slider_38.setAutoDraw(True)
        
        # *Q_5* updates
        if Q_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_5.frameNStart = frameN  # exact frame index
            Q_5.tStart = t  # local t and not account for scr refresh
            Q_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_5, 'tStartRefresh')  # time at next scr refresh
            Q_5.setAutoDraw(True)
        
        # *slider_47* updates
        if slider_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_47.frameNStart = frameN  # exact frame index
            slider_47.tStart = t  # local t and not account for scr refresh
            slider_47.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_47, 'tStartRefresh')  # time at next scr refresh
            slider_47.setAutoDraw(True)
        
        # *Q3_5* updates
        if Q3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_5.frameNStart = frameN  # exact frame index
            Q3_5.tStart = t  # local t and not account for scr refresh
            Q3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_5, 'tStartRefresh')  # time at next scr refresh
            Q3_5.setAutoDraw(True)
        
        # *slider_48* updates
        if slider_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_48.frameNStart = frameN  # exact frame index
            slider_48.tStart = t  # local t and not account for scr refresh
            slider_48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_48, 'tStartRefresh')  # time at next scr refresh
            slider_48.setAutoDraw(True)
        
        # *Q4_5* updates
        if Q4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4_5.frameNStart = frameN  # exact frame index
            Q4_5.tStart = t  # local t and not account for scr refresh
            Q4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4_5, 'tStartRefresh')  # time at next scr refresh
            Q4_5.setAutoDraw(True)
        
        # *slider_49* updates
        if slider_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_49.frameNStart = frameN  # exact frame index
            slider_49.tStart = t  # local t and not account for scr refresh
            slider_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_49, 'tStartRefresh')  # time at next scr refresh
            slider_49.setAutoDraw(True)
        
        # *pressSpace_11* updates
        if pressSpace_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_11.frameNStart = frameN  # exact frame index
            pressSpace_11.tStart = t  # local t and not account for scr refresh
            pressSpace_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_11, 'tStartRefresh')  # time at next scr refresh
            pressSpace_11.setAutoDraw(True)
        if pressSpace_11.status == STARTED:  # only update if drawing
            pressSpace_11.setText(spaceText, log=False)
        
        # *key_p_9* updates
        waitOnFlip = False
        if key_p_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_9.frameNStart = frameN  # exact frame index
            key_p_9.tStart = t  # local t and not account for scr refresh
            key_p_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_9, 'tStartRefresh')  # time at next scr refresh
            key_p_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_9.status == STARTED and not waitOnFlip:
            theseKeys = key_p_9.getKeys(keyList=['space'], waitRelease=False)
            _key_p_9_allKeys.extend(theseKeys)
            if len(_key_p_9_allKeys):
                key_p_9.keys = [key.name for key in _key_p_9_allKeys]  # storing all keys
                key_p_9.rt = [key.rt for key in _key_p_9_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p_9.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_9.keys) > number_keys_p_9:
                
                # update our count of the number of keys pressed
                number_keys_p_9 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_38.getRating() or not slider_47.getRating() or not slider_48.getRating() or not slider_49.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please enter all requested information, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_8* updates
        if message_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_8.frameNStart = frameN  # exact frame index
            message_8.tStart = t  # local t and not account for scr refresh
            message_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_8, 'tStartRefresh')  # time at next scr refresh
            message_8.setAutoDraw(True)
        if message_8.status == STARTED:  # only update if drawing
            message_8.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in P1_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "P1_O1"-------
    for thisComponent in P1_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_6.started', Question_6.tStartRefresh)
    trials.addData('Question_6.stopped', Question_6.tStopRefresh)
    trials.addData('Q1_6.started', Q1_6.tStartRefresh)
    trials.addData('Q1_6.stopped', Q1_6.tStopRefresh)
    trials.addData('slider_38.response', slider_38.getRating())
    trials.addData('slider_38.rt', slider_38.getRT())
    trials.addData('slider_38.started', slider_38.tStartRefresh)
    trials.addData('slider_38.stopped', slider_38.tStopRefresh)
    trials.addData('Q_5.started', Q_5.tStartRefresh)
    trials.addData('Q_5.stopped', Q_5.tStopRefresh)
    trials.addData('slider_47.response', slider_47.getRating())
    trials.addData('slider_47.rt', slider_47.getRT())
    trials.addData('slider_47.started', slider_47.tStartRefresh)
    trials.addData('slider_47.stopped', slider_47.tStopRefresh)
    trials.addData('Q3_5.started', Q3_5.tStartRefresh)
    trials.addData('Q3_5.stopped', Q3_5.tStopRefresh)
    trials.addData('slider_48.response', slider_48.getRating())
    trials.addData('slider_48.rt', slider_48.getRT())
    trials.addData('slider_48.started', slider_48.tStartRefresh)
    trials.addData('slider_48.stopped', slider_48.tStopRefresh)
    trials.addData('Q4_5.started', Q4_5.tStartRefresh)
    trials.addData('Q4_5.stopped', Q4_5.tStopRefresh)
    trials.addData('slider_49.response', slider_49.getRating())
    trials.addData('slider_49.rt', slider_49.getRT())
    trials.addData('slider_49.started', slider_49.tStartRefresh)
    trials.addData('slider_49.stopped', slider_49.tStopRefresh)
    trials.addData('pressSpace_11.started', pressSpace_11.tStartRefresh)
    trials.addData('pressSpace_11.stopped', pressSpace_11.tStopRefresh)
    # check responses
    if key_p_9.keys in ['', [], None]:  # No response was made
        key_p_9.keys = None
    trials.addData('key_p_9.keys',key_p_9.keys)
    if key_p_9.keys != None:  # we had a response
        trials.addData('key_p_9.rt', key_p_9.rt)
    trials.addData('key_p_9.started', key_p_9.tStartRefresh)
    trials.addData('key_p_9.stopped', key_p_9.tStopRefresh)
    trials.addData('message_8.started', message_8.tStartRefresh)
    trials.addData('message_8.stopped', message_8.tStopRefresh)
    # the Routine "P1_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "P1_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_51.reset()
    slider_52.reset()
    slider_53.reset()
    slider_54.reset()
    key_p_10.keys = []
    key_p_10.rt = []
    _key_p_10_allKeys = []
    number_keys_p_10 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to continue with the last questions on the video.'
    # keep track of which components have finished
    P1_O2Components = [Question_8, Q1_7, slider_51, Q_6, slider_52, Q3_6, slider_53, Q4_6, slider_54, pressSpace_12, key_p_10, message_10]
    for thisComponent in P1_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    P1_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "P1_O2"-------
    while continueRoutine:
        # get current time
        t = P1_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=P1_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_8* updates
        if Question_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_8.frameNStart = frameN  # exact frame index
            Question_8.tStart = t  # local t and not account for scr refresh
            Question_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_8, 'tStartRefresh')  # time at next scr refresh
            Question_8.setAutoDraw(True)
        
        # *Q1_7* updates
        if Q1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q1_7.frameNStart = frameN  # exact frame index
            Q1_7.tStart = t  # local t and not account for scr refresh
            Q1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q1_7, 'tStartRefresh')  # time at next scr refresh
            Q1_7.setAutoDraw(True)
        
        # *slider_51* updates
        if slider_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_51.frameNStart = frameN  # exact frame index
            slider_51.tStart = t  # local t and not account for scr refresh
            slider_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_51, 'tStartRefresh')  # time at next scr refresh
            slider_51.setAutoDraw(True)
        
        # *Q_6* updates
        if Q_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_6.frameNStart = frameN  # exact frame index
            Q_6.tStart = t  # local t and not account for scr refresh
            Q_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_6, 'tStartRefresh')  # time at next scr refresh
            Q_6.setAutoDraw(True)
        
        # *slider_52* updates
        if slider_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_52.frameNStart = frameN  # exact frame index
            slider_52.tStart = t  # local t and not account for scr refresh
            slider_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_52, 'tStartRefresh')  # time at next scr refresh
            slider_52.setAutoDraw(True)
        
        # *Q3_6* updates
        if Q3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_6.frameNStart = frameN  # exact frame index
            Q3_6.tStart = t  # local t and not account for scr refresh
            Q3_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_6, 'tStartRefresh')  # time at next scr refresh
            Q3_6.setAutoDraw(True)
        
        # *slider_53* updates
        if slider_53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_53.frameNStart = frameN  # exact frame index
            slider_53.tStart = t  # local t and not account for scr refresh
            slider_53.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_53, 'tStartRefresh')  # time at next scr refresh
            slider_53.setAutoDraw(True)
        
        # *Q4_6* updates
        if Q4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q4_6.frameNStart = frameN  # exact frame index
            Q4_6.tStart = t  # local t and not account for scr refresh
            Q4_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q4_6, 'tStartRefresh')  # time at next scr refresh
            Q4_6.setAutoDraw(True)
        
        # *slider_54* updates
        if slider_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_54.frameNStart = frameN  # exact frame index
            slider_54.tStart = t  # local t and not account for scr refresh
            slider_54.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_54, 'tStartRefresh')  # time at next scr refresh
            slider_54.setAutoDraw(True)
        
        # *pressSpace_12* updates
        if pressSpace_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_12.frameNStart = frameN  # exact frame index
            pressSpace_12.tStart = t  # local t and not account for scr refresh
            pressSpace_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_12, 'tStartRefresh')  # time at next scr refresh
            pressSpace_12.setAutoDraw(True)
        if pressSpace_12.status == STARTED:  # only update if drawing
            pressSpace_12.setText(spaceText, log=False)
        
        # *key_p_10* updates
        waitOnFlip = False
        if key_p_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_10.frameNStart = frameN  # exact frame index
            key_p_10.tStart = t  # local t and not account for scr refresh
            key_p_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_10, 'tStartRefresh')  # time at next scr refresh
            key_p_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_10.status == STARTED and not waitOnFlip:
            theseKeys = key_p_10.getKeys(keyList=['space'], waitRelease=False)
            _key_p_10_allKeys.extend(theseKeys)
            if len(_key_p_10_allKeys):
                key_p_10.keys = [key.name for key in _key_p_10_allKeys]  # storing all keys
                key_p_10.rt = [key.rt for key in _key_p_10_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_10.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_10.keys) > number_keys_p_10:
                
                # update our count of the number of keys pressed
                number_keys_p_10 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_51.getRating() or not slider_52.getRating() or not slider_53.getRating() or not slider_54.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please enter all requested information, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_10* updates
        if message_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_10.frameNStart = frameN  # exact frame index
            message_10.tStart = t  # local t and not account for scr refresh
            message_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_10, 'tStartRefresh')  # time at next scr refresh
            message_10.setAutoDraw(True)
        if message_10.status == STARTED:  # only update if drawing
            message_10.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in P1_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "P1_O2"-------
    for thisComponent in P1_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_8.started', Question_8.tStartRefresh)
    trials.addData('Question_8.stopped', Question_8.tStopRefresh)
    trials.addData('Q1_7.started', Q1_7.tStartRefresh)
    trials.addData('Q1_7.stopped', Q1_7.tStopRefresh)
    trials.addData('slider_51.response', slider_51.getRating())
    trials.addData('slider_51.rt', slider_51.getRT())
    trials.addData('slider_51.started', slider_51.tStartRefresh)
    trials.addData('slider_51.stopped', slider_51.tStopRefresh)
    trials.addData('Q_6.started', Q_6.tStartRefresh)
    trials.addData('Q_6.stopped', Q_6.tStopRefresh)
    trials.addData('slider_52.response', slider_52.getRating())
    trials.addData('slider_52.rt', slider_52.getRT())
    trials.addData('slider_52.started', slider_52.tStartRefresh)
    trials.addData('slider_52.stopped', slider_52.tStopRefresh)
    trials.addData('Q3_6.started', Q3_6.tStartRefresh)
    trials.addData('Q3_6.stopped', Q3_6.tStopRefresh)
    trials.addData('slider_53.response', slider_53.getRating())
    trials.addData('slider_53.rt', slider_53.getRT())
    trials.addData('slider_53.started', slider_53.tStartRefresh)
    trials.addData('slider_53.stopped', slider_53.tStopRefresh)
    trials.addData('Q4_6.started', Q4_6.tStartRefresh)
    trials.addData('Q4_6.stopped', Q4_6.tStopRefresh)
    trials.addData('slider_54.response', slider_54.getRating())
    trials.addData('slider_54.rt', slider_54.getRT())
    trials.addData('slider_54.started', slider_54.tStartRefresh)
    trials.addData('slider_54.stopped', slider_54.tStopRefresh)
    trials.addData('pressSpace_12.started', pressSpace_12.tStartRefresh)
    trials.addData('pressSpace_12.stopped', pressSpace_12.tStopRefresh)
    # check responses
    if key_p_10.keys in ['', [], None]:  # No response was made
        key_p_10.keys = None
    trials.addData('key_p_10.keys',key_p_10.keys)
    if key_p_10.keys != None:  # we had a response
        trials.addData('key_p_10.rt', key_p_10.rt)
    trials.addData('key_p_10.started', key_p_10.tStartRefresh)
    trials.addData('key_p_10.stopped', key_p_10.tStopRefresh)
    trials.addData('message_10.started', message_10.tStartRefresh)
    trials.addData('message_10.stopped', message_10.tStopRefresh)
    # the Routine "P1_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "C1_O1"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_56.reset()
    slider_57.reset()
    key_p_11.keys = []
    key_p_11.rt = []
    _key_p_11_allKeys = []
    number_keys_p_11 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to end the experiment.'
    # keep track of which components have finished
    C1_O1Components = [Question_9, Q_7, slider_56, Q3_7, slider_57, pressSpace_13, key_p_11, message_11]
    for thisComponent in C1_O1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    C1_O1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "C1_O1"-------
    while continueRoutine:
        # get current time
        t = C1_O1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=C1_O1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_9* updates
        if Question_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_9.frameNStart = frameN  # exact frame index
            Question_9.tStart = t  # local t and not account for scr refresh
            Question_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_9, 'tStartRefresh')  # time at next scr refresh
            Question_9.setAutoDraw(True)
        
        # *Q_7* updates
        if Q_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_7.frameNStart = frameN  # exact frame index
            Q_7.tStart = t  # local t and not account for scr refresh
            Q_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_7, 'tStartRefresh')  # time at next scr refresh
            Q_7.setAutoDraw(True)
        
        # *slider_56* updates
        if slider_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_56.frameNStart = frameN  # exact frame index
            slider_56.tStart = t  # local t and not account for scr refresh
            slider_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_56, 'tStartRefresh')  # time at next scr refresh
            slider_56.setAutoDraw(True)
        
        # *Q3_7* updates
        if Q3_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_7.frameNStart = frameN  # exact frame index
            Q3_7.tStart = t  # local t and not account for scr refresh
            Q3_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_7, 'tStartRefresh')  # time at next scr refresh
            Q3_7.setAutoDraw(True)
        
        # *slider_57* updates
        if slider_57.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_57.frameNStart = frameN  # exact frame index
            slider_57.tStart = t  # local t and not account for scr refresh
            slider_57.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_57, 'tStartRefresh')  # time at next scr refresh
            slider_57.setAutoDraw(True)
        
        # *pressSpace_13* updates
        if pressSpace_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_13.frameNStart = frameN  # exact frame index
            pressSpace_13.tStart = t  # local t and not account for scr refresh
            pressSpace_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_13, 'tStartRefresh')  # time at next scr refresh
            pressSpace_13.setAutoDraw(True)
        if pressSpace_13.status == STARTED:  # only update if drawing
            pressSpace_13.setText(spaceText, log=False)
        
        # *key_p_11* updates
        waitOnFlip = False
        if key_p_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_11.frameNStart = frameN  # exact frame index
            key_p_11.tStart = t  # local t and not account for scr refresh
            key_p_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_11, 'tStartRefresh')  # time at next scr refresh
            key_p_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_11.status == STARTED and not waitOnFlip:
            theseKeys = key_p_11.getKeys(keyList=['space'], waitRelease=False)
            _key_p_11_allKeys.extend(theseKeys)
            if len(_key_p_11_allKeys):
                key_p_11.keys = [key.name for key in _key_p_11_allKeys]  # storing all keys
                key_p_11.rt = [key.rt for key in _key_p_11_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 2:
            continueRoutine = False
        
        if key_p_11.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_11.keys) > number_keys_p_11:
                
                # update our count of the number of keys pressed
                number_keys_p_11 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_56.getRating() or not slider_57.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please enter all requested information, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_11* updates
        if message_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_11.frameNStart = frameN  # exact frame index
            message_11.tStart = t  # local t and not account for scr refresh
            message_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_11, 'tStartRefresh')  # time at next scr refresh
            message_11.setAutoDraw(True)
        if message_11.status == STARTED:  # only update if drawing
            message_11.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in C1_O1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "C1_O1"-------
    for thisComponent in C1_O1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_9.started', Question_9.tStartRefresh)
    trials.addData('Question_9.stopped', Question_9.tStopRefresh)
    trials.addData('Q_7.started', Q_7.tStartRefresh)
    trials.addData('Q_7.stopped', Q_7.tStopRefresh)
    trials.addData('slider_56.response', slider_56.getRating())
    trials.addData('slider_56.rt', slider_56.getRT())
    trials.addData('slider_56.started', slider_56.tStartRefresh)
    trials.addData('slider_56.stopped', slider_56.tStopRefresh)
    trials.addData('Q3_7.started', Q3_7.tStartRefresh)
    trials.addData('Q3_7.stopped', Q3_7.tStopRefresh)
    trials.addData('slider_57.response', slider_57.getRating())
    trials.addData('slider_57.rt', slider_57.getRT())
    trials.addData('slider_57.started', slider_57.tStartRefresh)
    trials.addData('slider_57.stopped', slider_57.tStopRefresh)
    trials.addData('pressSpace_13.started', pressSpace_13.tStartRefresh)
    trials.addData('pressSpace_13.stopped', pressSpace_13.tStopRefresh)
    # check responses
    if key_p_11.keys in ['', [], None]:  # No response was made
        key_p_11.keys = None
    trials.addData('key_p_11.keys',key_p_11.keys)
    if key_p_11.keys != None:  # we had a response
        trials.addData('key_p_11.rt', key_p_11.rt)
    trials.addData('key_p_11.started', key_p_11.tStartRefresh)
    trials.addData('key_p_11.stopped', key_p_11.tStopRefresh)
    trials.addData('message_11.started', message_11.tStartRefresh)
    trials.addData('message_11.stopped', message_11.tStopRefresh)
    # the Routine "C1_O1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "C1_O2"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_59.reset()
    slider_60.reset()
    key_p_12.keys = []
    key_p_12.rt = []
    _key_p_12_allKeys = []
    number_keys_p_12 = 0
    msg_p= ''
    spaceText= 'Press the spacebar to end the experiment.'
    # keep track of which components have finished
    C1_O2Components = [Question_10, Q_8, slider_59, Q3_8, slider_60, pressSpace_14, key_p_12, message_12]
    for thisComponent in C1_O2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    C1_O2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "C1_O2"-------
    while continueRoutine:
        # get current time
        t = C1_O2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=C1_O2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_10* updates
        if Question_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_10.frameNStart = frameN  # exact frame index
            Question_10.tStart = t  # local t and not account for scr refresh
            Question_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_10, 'tStartRefresh')  # time at next scr refresh
            Question_10.setAutoDraw(True)
        
        # *Q_8* updates
        if Q_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_8.frameNStart = frameN  # exact frame index
            Q_8.tStart = t  # local t and not account for scr refresh
            Q_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_8, 'tStartRefresh')  # time at next scr refresh
            Q_8.setAutoDraw(True)
        
        # *slider_59* updates
        if slider_59.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_59.frameNStart = frameN  # exact frame index
            slider_59.tStart = t  # local t and not account for scr refresh
            slider_59.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_59, 'tStartRefresh')  # time at next scr refresh
            slider_59.setAutoDraw(True)
        
        # *Q3_8* updates
        if Q3_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q3_8.frameNStart = frameN  # exact frame index
            Q3_8.tStart = t  # local t and not account for scr refresh
            Q3_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q3_8, 'tStartRefresh')  # time at next scr refresh
            Q3_8.setAutoDraw(True)
        
        # *slider_60* updates
        if slider_60.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_60.frameNStart = frameN  # exact frame index
            slider_60.tStart = t  # local t and not account for scr refresh
            slider_60.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_60, 'tStartRefresh')  # time at next scr refresh
            slider_60.setAutoDraw(True)
        
        # *pressSpace_14* updates
        if pressSpace_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_14.frameNStart = frameN  # exact frame index
            pressSpace_14.tStart = t  # local t and not account for scr refresh
            pressSpace_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_14, 'tStartRefresh')  # time at next scr refresh
            pressSpace_14.setAutoDraw(True)
        if pressSpace_14.status == STARTED:  # only update if drawing
            pressSpace_14.setText(spaceText, log=False)
        
        # *key_p_12* updates
        waitOnFlip = False
        if key_p_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_p_12.frameNStart = frameN  # exact frame index
            key_p_12.tStart = t  # local t and not account for scr refresh
            key_p_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_p_12, 'tStartRefresh')  # time at next scr refresh
            key_p_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_p_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_p_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_p_12.status == STARTED and not waitOnFlip:
            theseKeys = key_p_12.getKeys(keyList=['space'], waitRelease=False)
            _key_p_12_allKeys.extend(theseKeys)
            if len(_key_p_12_allKeys):
                key_p_12.keys = [key.name for key in _key_p_12_allKeys]  # storing all keys
                key_p_12.rt = [key.rt for key in _key_p_12_allKeys]
        # if 'order' is two, then we skip
        # the routine altogether
        if order == 1:
            continueRoutine = False
        
        if key_p_12.keys: #!=[]
            # if a key has been pressed
            #
            # (has to be the spacebar, its
            # the only one allowed)
            #
            # (the participant wants to 
            # continue to the next routine)
            if len(key_p_12.keys) > number_keys_p_12:
                
                # update our count of the number of keys pressed
                number_keys_p_12 += 1
                
                # if one of the sliders is empty (missing information)
                if not slider_59.getRating() or not slider_60.getRating():
                    
                    # ask participant to fill in everything 
                    msg_p = 'Please enter all requested information, then press the spacebar.'
                    spaceText = ''
                    
                    # and change the colour of the text
                    #textColour_i = [-0.820,-0.098,0.435]
                    
                    # if no information is missing
                else:
                    # end routine and continue with the study
                    continueRoutine = False        
                    #key_i.keys[-1] == 'space'
                    
        
        
        
        
        
        # *message_12* updates
        if message_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message_12.frameNStart = frameN  # exact frame index
            message_12.tStart = t  # local t and not account for scr refresh
            message_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message_12, 'tStartRefresh')  # time at next scr refresh
            message_12.setAutoDraw(True)
        if message_12.status == STARTED:  # only update if drawing
            message_12.setText(msg_p, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in C1_O2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "C1_O2"-------
    for thisComponent in C1_O2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_10.started', Question_10.tStartRefresh)
    trials.addData('Question_10.stopped', Question_10.tStopRefresh)
    trials.addData('Q_8.started', Q_8.tStartRefresh)
    trials.addData('Q_8.stopped', Q_8.tStopRefresh)
    trials.addData('slider_59.response', slider_59.getRating())
    trials.addData('slider_59.rt', slider_59.getRT())
    trials.addData('slider_59.started', slider_59.tStartRefresh)
    trials.addData('slider_59.stopped', slider_59.tStopRefresh)
    trials.addData('Q3_8.started', Q3_8.tStartRefresh)
    trials.addData('Q3_8.stopped', Q3_8.tStopRefresh)
    trials.addData('slider_60.response', slider_60.getRating())
    trials.addData('slider_60.rt', slider_60.getRT())
    trials.addData('slider_60.started', slider_60.tStartRefresh)
    trials.addData('slider_60.stopped', slider_60.tStopRefresh)
    trials.addData('pressSpace_14.started', pressSpace_14.tStartRefresh)
    trials.addData('pressSpace_14.stopped', pressSpace_14.tStopRefresh)
    # check responses
    if key_p_12.keys in ['', [], None]:  # No response was made
        key_p_12.keys = None
    trials.addData('key_p_12.keys',key_p_12.keys)
    if key_p_12.keys != None:  # we had a response
        trials.addData('key_p_12.rt', key_p_12.rt)
    trials.addData('key_p_12.started', key_p_12.tStartRefresh)
    trials.addData('key_p_12.stopped', key_p_12.tStopRefresh)
    trials.addData('message_12.started', message_12.tStartRefresh)
    trials.addData('message_12.stopped', message_12.tStopRefresh)
    # the Routine "C1_O2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
