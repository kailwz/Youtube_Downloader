from tkinter import *
from pytubefix import YouTube, streams
from pytubefix.cli import on_progress
from PIL import Image, ImageTk
import os, os.path
import requests
import time

class window ():
    def __init__(self):
        self.root = Tk()

        ###Configurations of the window###
        self.windowConfigurations()

        ###Frames for separate the parts of the application###
        self.windowFrames()

        ###Idicate Labels###
        self.windowLabels()

        ###Buttons that gonna do some functions###
        self.windowButtons()

        ###Window entry for search the video###
        self.windowEntrys()

        ###Load the Window###
        self.root.mainloop()

    def windowConfigurations (self):
        
        ###Configurations of the window###
        self.root.config(bg = '#101010')
        img = PhotoImage(file = 'logo.png')
        self.root.iconphoto(True, img)
        self.root.title('GetItNow - Youtube Downloader')
        self.root.geometry('800x495+250+55')
        self.root.resizable(0, 0)

    def windowFrames (self):
        ###Main frame of the window###
        self.mainFrame = Frame(
            bg = '#151515',
            width = 790,
            height = 240,
            relief = FLAT
            )
        self.mainFrame.place(
            x = 5,
            y = 5
            )

        ###Second frame of the window###
        self.secondFrame = Frame(
            bg = '#151515',
            width = 390,
            height = 240,
            relief = FLAT
            )
        self.secondFrame.place(
            x = 5,
            y = 250
            )

        ###Third frame of the window###
        self.thirdFrame = Frame(
            bg = '#151515',
            width = 395,
            height = 240,
            relief = FLAT
            )
        self.thirdFrame.place(
            x = 400,
            y = 250
            )

    def windowLabels (self):
        #**********FIRST FRAME THINGS**********#
        ###Label with the main title###
        self.titleLabel = Label(
            self.mainFrame,
            text = 'Dowload Your Video!',
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 25 bold'
        )
        self.titleLabel.place(
            x = 230,
            y = 5
            )

        ###Label asking to choise the directory###
        self.selectLabel = Label(
            self.mainFrame,
            text = 'Select the directory:',
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 15'
        )
        self.selectLabel.place(
            x = 130,
            y = 100
            )

        ###Label indicating to put the URL (Link)###
        self.linkLabel = Label(
            self.mainFrame,
            text = 'Video Link:',
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 15'
        )
        self.linkLabel.place(
            x = 515,
            y = 100
        )

        #**********THIRD FRAME THINGS**********#
        ###High quality video label###
        self.highQualityLabel = Label(
            self.thirdFrame,
            text = "High Quality (720p)",
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 15'
        )
        self.highQualityLabel.place(
            x = 20,
            y = 20
        )

        ###lower quality video label###
        self.lowQualityLabel = Label(
            self.thirdFrame,
            text = "Low Quality (144p)",
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 15'
        )
        self.lowQualityLabel.place(
            x = 20,
            y = 70
        )

        ###mp3 download label###
        self.mpQualityLabel = Label(
            self.thirdFrame,
            text = "Music Format (mp3)",
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 15'
        )
        self.mpQualityLabel.place(
            x = 20,
            y = 120
        )

    def videoInfoLabels(self):

        directory = self.searchDirectoryEntry.get()
        url = self.searchVideoEntry.get()
        youtube = YouTube(url)

        video_title = youtube.title
        video_time = str(time.strftime('%H:%M:%S', time.gmtime(int(youtube.length))))

        """
            data = requests.get(youtube.thumbnail_url).content

            with open('file01.jpg','wb') as file:
                file.write(data)
        """

        photo = PhotoImage(file = 'logo.png')

        #**********SECOND FRAME THINGS**********#
        ###Show the thumbnail of the video label###
        self.showThumbnailLabel = Label(
            self.secondFrame,
            image = photo,
            width  = 300,
            height = 150
        )
        self.showThumbnailLabel.place(
            x = 42,
            y = 20
        )

        ###Video name label###
        self.videoNameLabel = Label(
            self.secondFrame,
            text = video_title,
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 10'
        )
        self.videoNameLabel.place(
            x = 10,
            y = 190
        )

        ###Video duration label###
        self.videoDurationLabel = Label(
            self.secondFrame,
            text = f'Time: {video_time}',
            bg = '#151515',
            fg = 'whitesmoke',
            font = 'helvetica 10'
        )
        self.videoDurationLabel.place(
            x = 10,
            y = 210
        )

    def windowEntrys (self):
        #**********FIRST FRAME THINGS**********#
        ###Search the video you want###
        self.searchVideoEntry = Entry(
            self.mainFrame,
            width = 25,
            font = 'helvetica 15'
        )
        self.searchVideoEntry.place(
            x = 430,
            y = 135
        )

        ###Entry showing the current directory###
        self.searchDirectoryEntry = Entry(
            self.mainFrame,
            width = 25,
            font = 'helvetica 15'
        )
        self.searchDirectoryEntry.insert(0, '/home/filipe/Downloads/')
        self.searchDirectoryEntry.place(
            x = 80,
            y = 135
        )
    
    def windowButtons (self):
        #**********THIRD FRAME THINGS**********#
        ###High quality video button###
        self.highQualityButton = Button(
            self.thirdFrame,
            text = 'Download',
            activebackground = '#2bad43',
            activeforeground = 'whitesmoke',
            highlightthickness = 0,
            fg = 'whitesmoke',
            bg = '#2fce4c',
            bd = 0,
            width = 18,
            height = 1,
            command = lambda: (self.downloadVideoHighQuality(), self.videoInfoLabels())
        )
        self.highQualityButton.place(
            x = 210,
            y = 17
        )

        ###lower quality video button###
        self.lowQualityButton = Button(
            self.thirdFrame,
            text = 'Download',
            activebackground = '#2bad43',
            activeforeground = 'whitesmoke',
            highlightthickness = 0,
            fg = 'whitesmoke',
            bg = '#2fce4c',
            bd = 0,
            width = 18,
            height = 1,
            command = lambda: (self.downloadVideoLowQuality(), self.videoInfoLabels())
        )
        self.lowQualityButton.place(
            x = 210,
            y = 67
        )

        ###mp3 download button###
        self.mpQualityButton = Button(
            self.thirdFrame,
            text = 'Download',
            activebackground = '#2bad43',
            activeforeground = 'whitesmoke',
            highlightthickness = 0,
            fg = 'whitesmoke',
            bg = '#2fce4c',
            bd = 0,
            width = 18,
            height = 1,
            command = lambda: (self.downloadAudio(), self.videoInfoLabels())
        )
        self.mpQualityButton.place(
            x = 210,
            y = 117
        )

    def downloadVideoHighQuality(self):
        url = self.searchVideoEntry.get()
        directory = self.searchDirectoryEntry.get()

        youtube = YouTube(url, on_progress_callback = on_progress)
        stream = youtube.streams.get_highest_resolution()
        stream.download(output_path=directory)

    def downloadVideoLowQuality(self):
        url = self.searchVideoEntry.get()
        directory = self.searchDirectoryEntry.get()

        youtube = YouTube(url, on_progress_callback = on_progress)
        stream = youtube.streams.get_lowest_resolution()
        stream.download(output_path=directory)

    def downloadAudio(self):
        url = self.searchVideoEntry.get()
        directory = self.searchDirectoryEntry.get()

        youtube = YouTube(url, on_progress_callback = on_progress)
        stream = youtube.streams.get_audio_only()
        stream = stream.download(output_path=directory)

loadWindow = window()
