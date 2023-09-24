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
expName = 'Experiment1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\andyv\\Documents\\School\\Thesis\\PsychoPy\\Experiment1\\Experiment1.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
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
    text='The Nonverbal Behaviour Study',
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
About1 = visual.TextStim(win=win, name='About1',
    text='We are interested in knowing about ',
    font='Times New Roman',
    pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
About2 = visual.TextStim(win=win, name='About2',
    text='how people perceive nonverbal behaviour,',
    font='Times New Roman',
    pos=(0, 0.065), height=0.035, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
About3 = visual.TextStim(win=win, name='About3',
    text='which can include facial expressions, and other body motion.',
    font='Times New Roman',
    pos=(0, 0.03), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Description1 = visual.TextStim(win=win, name='Description1',
    text='In this study you are being asked to ',
    font='Times New Roman',
    pos=(0, -0.04), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Description2 = visual.TextStim(win=win, name='Description2',
    text='look at a photo of an everyday situation and give us your impressions.',
    font='Times New Roman',
    pos=(0, -0.08), height=0.035, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
Description3 = visual.TextStim(win=win, name='Description3',
    text=' Please read the consent form on the following page. ',
    font='Times New Roman',
    pos=(0, -0.2), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
PressSpace = visual.TextStim(win=win, name='PressSpace',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Consent1"
Consent1Clock = core.Clock()
Title_2 = visual.TextStim(win=win, name='Title_2',
    text='CONSENT TO PARTICIPATE IN The Nonverbal Behaviour Study',
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
    text='A. PURPOSE AND PROCEDURE\nThe purpose of the study is to get my impressions of a photo of an everyday situation. The study will take approximatley 13 minutes to complete. The study is for people 18 to 35 years of age who are proficient in English.',
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
    text='B.CONDITIONS OF PARTICIPATION: I understand that…\n… my participation in this study is CONFIDENTIAL (i.e., the researchers wll be able to identify me but my identity will not be disclosed).\n…it is my decision to participate. I am free to withdraw my consent and discontinue my participation at any time (by pressing the Escape key and closing the tab while completing the study) without negative consequences.\n…I will be asked to provide demographic information: my age and gender.\n…once I have completed the study, I cannot ask to have my responses withdrawn.\n…the data from this study may be published in aggregate form (i.e., averaged across many participants) in a scientific journal.\n...I will receive 0.5 credits for participating in this study.\n',
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
    text='Press the ‘Y’ key to agree to continue.\nPress the ‘N’ key to disagree and exit the program.',
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
    pos=(0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
what_typed = visual.TextStim(win=win, name='what_typed',
    text='',
    font='Times New Roman',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
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
    text='__________ years',
    font='Times New Roman',
    pos=(0.05,-0.11), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Now move the cursor to the bottom right corner of the screen (to get it out of the way).',
    font='Times New Roman',
    pos=(0, -0.25), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-10.0);

# Initialize components for Routine "Conway1"
Conway1Clock = core.Clock()
Title_3 = visual.TextStim(win=win, name='Title_3',
    text="We need to remind you that you can't participate in this study if you've taken courses with Dr. Michael Conway because he might have mentioned this research.\n",
    font='Times New Roman',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PressYN_2 = visual.TextStim(win=win, name='PressYN_2',
    text="Press the 'Y' key to continue.\n\nPress the 'N' key to leave the experiment.",
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
agree_or_disagree_2 = keyboard.Keyboard()

# Initialize components for Routine "Conway2"
Conway2Clock = core.Clock()
response_2 = visual.TextStim(win=win, name='response_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PressSpace2_2 = visual.TextStim(win=win, name='PressSpace2_2',
    text='',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
PressSpace_2 = visual.TextStim(win=win, name='PressSpace_2',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
pressSpace = keyboard.Keyboard()

# Initialize components for Routine "Picture"
PictureClock = core.Clock()
picture = visual.ImageStim(
    win=win,
    name='picture', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
PressSpace_3 = visual.TextStim(win=win, name='PressSpace_3',
    text='Please form an impression of what is going on and when you are ready press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pressSpace_2 = keyboard.Keyboard()

# Initialize components for Routine "OpenQ_2"
OpenQ_2Clock = core.Clock()
OpenQuestion_2 = visual.TextStim(win=win, name='OpenQuestion_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.4), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox_2 = visual.TextBox2(
     win, text=None, font='Times New Roman',
     pos=(0, -0.05),     letterHeight=0.04,
     size=(1.25, 0.4), borderWidth=1.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=True,
     editable=True,
     name='textbox_2',
     autoLog=True,
)
button_2 = visual.ButtonStim(win, 
    text='Click here to continue.', font='Times New Roman',
    pos=(0.4, -0.4),
    letterHeight=0.025,
    size=(0.35, 0.07), borderWidth=0.0,
    fillColor='lightgrey', borderColor='black',
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2'
)
button_2.buttonClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please type your answers in the box.\nYou can write in full sentences or point form. Do not worry about spelling, grammar, or punctuation.\n',
    font='Times New Roman',
    pos=(0, 0.25), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Questionnaire1"
Questionnaire1Clock = core.Clock()
Question_2 = visual.TextStim(win=win, name='Question_2',
    text='',
    font='Times New Roman',
    pos=(0, 0.45), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feelQ = visual.TextStim(win=win, name='feelQ',
    text='',
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

# Initialize components for Routine "Q1_2"
Q1_2Clock = core.Clock()
feelQ_2 = visual.TextStim(win=win, name='feelQ_2',
    text='',
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

# Initialize components for Routine "Q2"
Q2Clock = core.Clock()
Question_7 = visual.TextStim(win=win, name='Question_7',
    text='',
    font='Times New Roman',
    pos=(0, 0.45), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feelQ_3 = visual.TextStim(win=win, name='feelQ_3',
    text='',
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

# Initialize components for Routine "Q2_3"
Q2_3Clock = core.Clock()
feelQ_5 = visual.TextStim(win=win, name='feelQ_5',
    text='',
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

if participant==5 or participant==21 or participant==35 or participant==55 or participant==72 or participant==87 or participant==100:
    image=1
    order=1
    qtext=1
elif participant==15 or participant==25 or participant==46 or participant==63 or participant==75 or participant==91 or participant==108:
    image=1
    order=2
    qtext=1
elif participant==4 or participant==17 or participant==44 or participant==58 or participant==83 or participant==102 or participant==110:
    image=2
    order=1
    qtext=1
elif participant==9 or participant==29 or participant==39 or participant==51 or participant==68 or participant==77 or participant==94:
    image=2
    order=2
    qtext=1
elif participant==2 or participant==18 or participant==32 or participant==33 or participant==52 or participant==76 or participant==81:
    image=3
    order=1
    qtext=1
elif participant==14 or participant==45 or participant==57 or participant==65 or participant==96 or participant==104 or participant==105:
    image=3
    order=2
    qtext=1
elif participant==11 or participant==26 or participant==43 or participant==61 or participant==79 or participant==97 or participant==112:
    image=4
    order=1
    qtext=1
elif participant==7 or participant==23 or participant==37 or participant==54 or participant==69 or participant==86 or participant==92:
    image=4
    order=2
    qtext=1
elif participant==6 or participant==24 or participant==36 or participant==56 or participant==64 or participant==90 or participant==101:
    image=5
    order=1
    qtext=2
elif participant==13 or participant==28 or participant==42 or participant==66 or participant==73 or participant==88 or participant==107:
    image=5
    order=2
    qtext=2
elif participant==3 or participant==20 or participant==47 or participant==59 or participant==78 or participant==93 or participant==98:
    image=6
    order=1
    qtext=2
elif participant==12 or participant==31 or participant==38 or participant==49 or participant==70 or participant==82 or participant==109:
    image=6
    order=2
    qtext=2
elif participant==8 or participant==22 or participant==40 or participant==50 or participant==67 or participant==85 or participant==103:
    image=7
    order=1
    qtext=2
elif participant==16 or participant==30 or participant==41 or participant==60 or participant==74 or participant==95 or participant==106:
    image=7
    order=2
    qtext=2
elif participant==1 or participant==19 or participant==34 or participant==53 or participant==71 or participant==84 or participant==99:
    image=8
    order=1
    qtext=2
elif participant==10 or participant==27 or participant==48 or participant==62 or participant==80 or participant==89 or participant==111:
    image=8
    order=2
    qtext=2
    
# put filenames of images here
image_files = ['Image1_FemaleAudience1.png', 'Image2_FemaleAudience2.png', 'Image3_FemaleSolo1.png', 'Image4_FemaleSolo2.png', 'Image5_MaleAudience1.png', 'Image6_MaleAudience2.png', 'Image7_MaleSolo1.png', 'Image8_MaleSolo2.png']

# put image dimensions here (in same order as in image_files list)
img_size = [[1, 0.6], [1,0.6], [0.75,0.6], [0.75,0.6], [1,0.6], [1,0.6], [0.75,0.6], [0.8,0.6]]

#img_position = [[0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1]]

img_pos_x = [0, 0, 0, 0, 0, 0, 0, 0]
img_pos_y = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# chooses which image is played
image_shown = image_files[image-1]
image_size=img_size[image-1]
#image_position = img_position[image-1]
image_x = img_pos_x[image-1]
image_y = img_pos_y[image-1]
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
TitlePageComponents = [Title, Authors, About1, About2, About3, Description1, Description2, Description3, PressSpace, key_resp]
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
    
    # *About1* updates
    if About1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        About1.frameNStart = frameN  # exact frame index
        About1.tStart = t  # local t and not account for scr refresh
        About1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(About1, 'tStartRefresh')  # time at next scr refresh
        About1.setAutoDraw(True)
    
    # *About2* updates
    if About2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        About2.frameNStart = frameN  # exact frame index
        About2.tStart = t  # local t and not account for scr refresh
        About2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(About2, 'tStartRefresh')  # time at next scr refresh
        About2.setAutoDraw(True)
    
    # *About3* updates
    if About3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        About3.frameNStart = frameN  # exact frame index
        About3.tStart = t  # local t and not account for scr refresh
        About3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(About3, 'tStartRefresh')  # time at next scr refresh
        About3.setAutoDraw(True)
    
    # *Description1* updates
    if Description1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Description1.frameNStart = frameN  # exact frame index
        Description1.tStart = t  # local t and not account for scr refresh
        Description1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Description1, 'tStartRefresh')  # time at next scr refresh
        Description1.setAutoDraw(True)
    
    # *Description2* updates
    if Description2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Description2.frameNStart = frameN  # exact frame index
        Description2.tStart = t  # local t and not account for scr refresh
        Description2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Description2, 'tStartRefresh')  # time at next scr refresh
        Description2.setAutoDraw(True)
    
    # *Description3* updates
    if Description3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Description3.frameNStart = frameN  # exact frame index
        Description3.tStart = t  # local t and not account for scr refresh
        Description3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Description3, 'tStartRefresh')  # time at next scr refresh
        Description3.setAutoDraw(True)
    
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
thisExp.addData('About1.started', About1.tStartRefresh)
thisExp.addData('About1.stopped', About1.tStopRefresh)
thisExp.addData('About2.started', About2.tStartRefresh)
thisExp.addData('About2.stopped', About2.tStopRefresh)
thisExp.addData('About3.started', About3.tStartRefresh)
thisExp.addData('About3.stopped', About3.tStopRefresh)
thisExp.addData('Description1.started', Description1.tStartRefresh)
thisExp.addData('Description1.stopped', Description1.tStopRefresh)
thisExp.addData('Description2.started', Description2.tStartRefresh)
thisExp.addData('Description2.stopped', Description2.tStopRefresh)
thisExp.addData('Description3.started', Description3.tStartRefresh)
thisExp.addData('Description3.stopped', Description3.tStopRefresh)
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
# the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Conway1"-------
    continueRoutine = True
    # update component parameters for each repeat
    agree_or_disagree_2.keys = []
    agree_or_disagree_2.rt = []
    _agree_or_disagree_2_allKeys = []
    # keep track of which components have finished
    Conway1Components = [Title_3, PressYN_2, agree_or_disagree_2]
    for thisComponent in Conway1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Conway1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Conway1"-------
    while continueRoutine:
        # get current time
        t = Conway1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Conway1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Title_3* updates
        if Title_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Title_3.frameNStart = frameN  # exact frame index
            Title_3.tStart = t  # local t and not account for scr refresh
            Title_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Title_3, 'tStartRefresh')  # time at next scr refresh
            Title_3.setAutoDraw(True)
        
        # *PressYN_2* updates
        if PressYN_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressYN_2.frameNStart = frameN  # exact frame index
            PressYN_2.tStart = t  # local t and not account for scr refresh
            PressYN_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressYN_2, 'tStartRefresh')  # time at next scr refresh
            PressYN_2.setAutoDraw(True)
        
        # *agree_or_disagree_2* updates
        waitOnFlip = False
        if agree_or_disagree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            agree_or_disagree_2.frameNStart = frameN  # exact frame index
            agree_or_disagree_2.tStart = t  # local t and not account for scr refresh
            agree_or_disagree_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(agree_or_disagree_2, 'tStartRefresh')  # time at next scr refresh
            agree_or_disagree_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(agree_or_disagree_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(agree_or_disagree_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if agree_or_disagree_2.status == STARTED and not waitOnFlip:
            theseKeys = agree_or_disagree_2.getKeys(keyList=['y', 'n'], waitRelease=False)
            _agree_or_disagree_2_allKeys.extend(theseKeys)
            if len(_agree_or_disagree_2_allKeys):
                agree_or_disagree_2.keys = _agree_or_disagree_2_allKeys[-1].name  # just the last key pressed
                agree_or_disagree_2.rt = _agree_or_disagree_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Conway1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Conway1"-------
    for thisComponent in Conway1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Title_3.started', Title_3.tStartRefresh)
    trials.addData('Title_3.stopped', Title_3.tStopRefresh)
    trials.addData('PressYN_2.started', PressYN_2.tStartRefresh)
    trials.addData('PressYN_2.stopped', PressYN_2.tStopRefresh)
    # check responses
    if agree_or_disagree_2.keys in ['', [], None]:  # No response was made
        agree_or_disagree_2.keys = None
    trials.addData('agree_or_disagree_2.keys',agree_or_disagree_2.keys)
    if agree_or_disagree_2.keys != None:  # we had a response
        trials.addData('agree_or_disagree_2.rt', agree_or_disagree_2.rt)
    trials.addData('agree_or_disagree_2.started', agree_or_disagree_2.tStartRefresh)
    trials.addData('agree_or_disagree_2.stopped', agree_or_disagree_2.tStopRefresh)
    # the Routine "Conway1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Conway2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # the text for 'response' text component
    msg = ""
    
    # the text for 'press_space_continue' component
    space = ''
    
    continueStudy = True
    
    
    
    # if they agree (if they pressed 'y')
    if agree_or_disagree_2.keys == "y":
        
        # they continue with the study
        continueRoutine = False
        #msg = "You will now be direc."
        #space = "Press the spacebar to continue."
        # consent is still True at the end
    
    
    # if they disagree (if they pressed 'n')
    elif agree_or_disagree_2.keys == "n":
        
        # the study will end here
        msg = "Thank you for your time."
        space = "Press the spacebar to quit the program."
        continueStudy = False
        # if consent is False, then
        # quit program at the 'End 
        # Routine' tab.
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Conway2Components = [response_2, PressSpace2_2, key_resp_3]
    for thisComponent in Conway2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Conway2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Conway2"-------
    while continueRoutine:
        # get current time
        t = Conway2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Conway2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response_2* updates
        if response_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            response_2.setAutoDraw(True)
        if response_2.status == STARTED:  # only update if drawing
            response_2.setText(msg, log=False)
        
        # *PressSpace2_2* updates
        if PressSpace2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace2_2.frameNStart = frameN  # exact frame index
            PressSpace2_2.tStart = t  # local t and not account for scr refresh
            PressSpace2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace2_2, 'tStartRefresh')  # time at next scr refresh
            PressSpace2_2.setAutoDraw(True)
        if PressSpace2_2.status == STARTED:  # only update if drawing
            PressSpace2_2.setText(space, log=False)
        
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
        for thisComponent in Conway2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Conway2"-------
    for thisComponent in Conway2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if continueStudy==False:
        quit()
    trials.addData('response_2.started', response_2.tStartRefresh)
    trials.addData('response_2.stopped', response_2.tStopRefresh)
    trials.addData('PressSpace2_2.started', PressSpace2_2.tStartRefresh)
    trials.addData('PressSpace2_2.stopped', PressSpace2_2.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "Conway2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    pressSpace.keys = []
    pressSpace.rt = []
    _pressSpace_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [PressSpace_2, pressSpace]
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
        
        # *PressSpace_2* updates
        if PressSpace_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_2.frameNStart = frameN  # exact frame index
            PressSpace_2.tStart = t  # local t and not account for scr refresh
            PressSpace_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_2, 'tStartRefresh')  # time at next scr refresh
            PressSpace_2.setAutoDraw(True)
        
        # *pressSpace* updates
        waitOnFlip = False
        if pressSpace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Picture"-------
    continueRoutine = True
    # update component parameters for each repeat
    pressSpace_2.keys = []
    pressSpace_2.rt = []
    _pressSpace_2_allKeys = []
    #image = image_shown
    # keep track of which components have finished
    PictureComponents = [picture, PressSpace_3, pressSpace_2]
    for thisComponent in PictureComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PictureClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Picture"-------
    while continueRoutine:
        # get current time
        t = PictureClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PictureClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *picture* updates
        if picture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture.frameNStart = frameN  # exact frame index
            picture.tStart = t  # local t and not account for scr refresh
            picture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture, 'tStartRefresh')  # time at next scr refresh
            picture.setAutoDraw(True)
        if picture.status == STARTED:  # only update if drawing
            picture.setPos([image_x, image_y], log=False)
            picture.setSize(image_size, log=False)
            picture.setImage(image_shown, log=False)
        
        # *PressSpace_3* updates
        if PressSpace_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            PressSpace_3.frameNStart = frameN  # exact frame index
            PressSpace_3.tStart = t  # local t and not account for scr refresh
            PressSpace_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressSpace_3, 'tStartRefresh')  # time at next scr refresh
            PressSpace_3.setAutoDraw(True)
        
        # *pressSpace_2* updates
        waitOnFlip = False
        if pressSpace_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_2.frameNStart = frameN  # exact frame index
            pressSpace_2.tStart = t  # local t and not account for scr refresh
            pressSpace_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_2, 'tStartRefresh')  # time at next scr refresh
            pressSpace_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pressSpace_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pressSpace_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pressSpace_2.status == STARTED and not waitOnFlip:
            theseKeys = pressSpace_2.getKeys(keyList=['space'], waitRelease=False)
            _pressSpace_2_allKeys.extend(theseKeys)
            if len(_pressSpace_2_allKeys):
                pressSpace_2.keys = _pressSpace_2_allKeys[-1].name  # just the last key pressed
                pressSpace_2.rt = _pressSpace_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PictureComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Picture"-------
    for thisComponent in PictureComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('picture.started', picture.tStartRefresh)
    trials.addData('picture.stopped', picture.tStopRefresh)
    trials.addData('PressSpace_3.started', PressSpace_3.tStartRefresh)
    trials.addData('PressSpace_3.stopped', PressSpace_3.tStopRefresh)
    # check responses
    if pressSpace_2.keys in ['', [], None]:  # No response was made
        pressSpace_2.keys = None
    trials.addData('pressSpace_2.keys',pressSpace_2.keys)
    if pressSpace_2.keys != None:  # we had a response
        trials.addData('pressSpace_2.rt', pressSpace_2.rt)
    trials.addData('pressSpace_2.started', pressSpace_2.tStartRefresh)
    trials.addData('pressSpace_2.stopped', pressSpace_2.tStopRefresh)
    # the Routine "Picture" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "OpenQ_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    question = ''
    textbox_2.reset()
    # keep track of which components have finished
    OpenQ_2Components = [OpenQuestion_2, textbox_2, button_2, text_2]
    for thisComponent in OpenQ_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    OpenQ_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "OpenQ_2"-------
    while continueRoutine:
        # get current time
        t = OpenQ_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=OpenQ_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *OpenQuestion_2* updates
        if OpenQuestion_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            OpenQuestion_2.frameNStart = frameN  # exact frame index
            OpenQuestion_2.tStart = t  # local t and not account for scr refresh
            OpenQuestion_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OpenQuestion_2, 'tStartRefresh')  # time at next scr refresh
            OpenQuestion_2.setAutoDraw(True)
        if OpenQuestion_2.status == STARTED:  # only update if drawing
            OpenQuestion_2.setText(question, log=False)
        if qtext==1:
            question = 'What are your impressions of this person? Where is she at? Please describe her thoughts, her feelings, and what might be going on in this situation.'
        elif qtext==2:
            question = 'What are your impressions of this person? Where is he at? Please describe his thoughts, his feelings, and what might be going on in this situation.'
        
        
        # *textbox_2* updates
        if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_2.frameNStart = frameN  # exact frame index
            textbox_2.tStart = t  # local t and not account for scr refresh
            textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
            textbox_2.setAutoDraw(True)
        
        # *button_2* updates
        if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
            button_2.setAutoDraw(True)
        if button_2.status == STARTED:
            # check whether button_2 has been pressed
            if button_2.isClicked:
                if not button_2.wasClicked:
                    button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                    button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
                else:
                    button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
                if not button_2.wasClicked:
                    continueRoutine = False  # end routine when button_2 is clicked
                    None
                button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
            else:
                button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OpenQ_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "OpenQ_2"-------
    for thisComponent in OpenQ_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('OpenQuestion_2.started', OpenQuestion_2.tStartRefresh)
    trials.addData('OpenQuestion_2.stopped', OpenQuestion_2.tStopRefresh)
    trials.addData('textbox_2.text',textbox_2.text)
    trials.addData('textbox_2.started', textbox_2.tStartRefresh)
    trials.addData('textbox_2.stopped', textbox_2.tStopRefresh)
    trials.addData('button_2.started', button_2.tStartRefresh)
    trials.addData('button_2.stopped', button_2.tStopRefresh)
    trials.addData('button_2.numClicks', button_2.numClicks)
    if button_2.numClicks:
       trials.addData('button_2.timesOn', button_2.timesOn)
       trials.addData('button_2.timesOff', button_2.timesOff)
    else:
       trials.addData('button_2.timesOn', "")
       trials.addData('button_2.timesOff', "")
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "OpenQ_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Questionnaire1"-------
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
    spaceText= 'Press the spacebar for the last set of ratings.'
    question = ''
    feel = ''
    # keep track of which components have finished
    Questionnaire1Components = [Question_2, feelQ, Angry, slider, Bored, slider_2, Sad, slider_h, Embarrassed, slider_3, Disgusted, slider_4, Shy, slider_5, pressSpace_3, key_p, message]
    for thisComponent in Questionnaire1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Questionnaire1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Questionnaire1"-------
    while continueRoutine:
        # get current time
        t = Questionnaire1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Questionnaire1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_2* updates
        if Question_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_2.frameNStart = frameN  # exact frame index
            Question_2.tStart = t  # local t and not account for scr refresh
            Question_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_2, 'tStartRefresh')  # time at next scr refresh
            Question_2.setAutoDraw(True)
        if Question_2.status == STARTED:  # only update if drawing
            Question_2.setText(question, log=False)
        
        # *feelQ* updates
        if feelQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ.frameNStart = frameN  # exact frame index
            feelQ.tStart = t  # local t and not account for scr refresh
            feelQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ, 'tStartRefresh')  # time at next scr refresh
            feelQ.setAutoDraw(True)
        if feelQ.status == STARTED:  # only update if drawing
            feelQ.setText(feel, log=False)
        
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
            question = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'She feels...'
        
        elif qtext==2:
            question = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'He feels...'
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Questionnaire1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Questionnaire1"-------
    for thisComponent in Questionnaire1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_2.started', Question_2.tStartRefresh)
    trials.addData('Question_2.stopped', Question_2.tStopRefresh)
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
    # the Routine "Questionnaire1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q1_2"-------
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
    spaceText= 'Press the spacebar to continue.'
    question = ''
    feel = ''
    # keep track of which components have finished
    Q1_2Components = [feelQ_2, Uninterested_1, slider_39, Unhappy, slider_21, Anxious_3, slider_22, Tired_3, slider_26, Ashamed_3, slider_23, Fearful_3, slider_24, Guilty_3, slider_25, pressSpace_7, key_p_5, message_6]
    for thisComponent in Q1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q1_2"-------
    while continueRoutine:
        # get current time
        t = Q1_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q1_2Clock)
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
        if feelQ_2.status == STARTED:  # only update if drawing
            feelQ_2.setText(feel, log=False)
        
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
        if qtext==1:
            question = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'She feels...'
        
        elif qtext==2:
            question = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'He feels...'
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q1_2"-------
    for thisComponent in Q1_2Components:
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
    # the Routine "Q1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q2"-------
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
    spaceText= 'Press the spacebar for the last set of ratings.'
    question = ''
    feel = ''
    # keep track of which components have finished
    Q2Components = [Question_7, feelQ_3, Guilty_5, slider_27, Fearful_4, slider_28, Ashamed_5, slider_32, Tired_6, slider_29, Anxious_4, slider_30, Unhappy_4, slider_31, pressSpace_8, key_p_6, message_7]
    for thisComponent in Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q2"-------
    while continueRoutine:
        # get current time
        t = Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_7* updates
        if Question_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Question_7.frameNStart = frameN  # exact frame index
            Question_7.tStart = t  # local t and not account for scr refresh
            Question_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_7, 'tStartRefresh')  # time at next scr refresh
            Question_7.setAutoDraw(True)
        if Question_7.status == STARTED:  # only update if drawing
            Question_7.setText(question, log=False)
        
        # *feelQ_3* updates
        if feelQ_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feelQ_3.frameNStart = frameN  # exact frame index
            feelQ_3.tStart = t  # local t and not account for scr refresh
            feelQ_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feelQ_3, 'tStartRefresh')  # time at next scr refresh
            feelQ_3.setAutoDraw(True)
        if feelQ_3.status == STARTED:  # only update if drawing
            feelQ_3.setText(feel, log=False)
        
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
            question = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'She feels...'
        
        elif qtext==2:
            question = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'He feels...'
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q2"-------
    for thisComponent in Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_7.started', Question_7.tStartRefresh)
    trials.addData('Question_7.stopped', Question_7.tStopRefresh)
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
    # the Routine "Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q2_3"-------
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
    spaceText= 'Press the spacebar to continue.'
    question = ''
    feel = ''
    # keep track of which components have finished
    Q2_3Components = [feelQ_5, Shy_5, slider_46, Disgusted_5, slider_40, Embarrassed_6, slider_41, Sad_6, slider_42, Bored_6, slider_43, Angry_6, slider_44, Uninterested_6, slider_45, pressSpace_10, key_p_8, message_9]
    for thisComponent in Q2_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q2_3"-------
    while continueRoutine:
        # get current time
        t = Q2_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q2_3Clock)
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
        if feelQ_5.status == STARTED:  # only update if drawing
            feelQ_5.setText(feel, log=False)
        
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
        if qtext==1:
            question = 'How much do you think she is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'She feels...'
        
        elif qtext==2:
            question = 'How much do you think he is feeling each of the following? Please select the number on each scale that best represents your opinion. If you are not sure, please guess.'
            feel = 'He feels...'
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q2_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q2_3"-------
    for thisComponent in Q2_3Components:
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
    # the Routine "Q2_3" was not non-slip safe, so reset the non-slip timer
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
