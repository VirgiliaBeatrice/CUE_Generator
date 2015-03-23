# -*- coding: utf-8-*-
'''
Created on 2015��3��23��

@author: virbea
'''
import os
import codecs

class CueFile():
    """
    """
    def __init__(self, wavfilePath):
        self.default_InfoStr = {"tml_Genre" : [u"REM GENRE ", u"placeholder"],
                                "tml_Date"  : [u"REM DATE ", u"placeholder"],
                                "tml_AlbumPerformer" : [u"PERFORMER \"", u"placeholder", u"\""],
                                "tml_AlbumTitle" : [u"TITLE \"", u"placeholder", u"\""],
                                "tml_AlbumPath" : [u"FILE \"", u"placeholder", u"\" WAVE"],
                                "tml_TrackNum" : [u"  TRACK ", u"placeholder", u" AUDIO"],
                                "tml_TrackTitle": [u"    TITLE \"", u"placeholder", u"\""],
                                "tml_TrackPerformer" : [u"    PERFORMER \"", u"placeholder", u"\""],
                                "tml_TrackIndex00" : [u"    INDEX 00 ", u"HH", u":", u"MM", u":", u"SS"],
                                "tml_TrackIndex01" : [u"    INDEX 01 ", u"HH", u":", u"MM", u":", u"SS"]
                                }
        self.default_InfoStr["tml_AlbumPath"][1] = unicode(wavfilePath)

        self.cuefile_TrackVolume = 0
        self.cuefile_Cache = []
       
        
    def input_genre(self, genre=u"Null"):
        self.default_InfoStr["tml_Genre"][1] = genre
        self.cuefile_Cache.append(self.default_InfoStr["tml_Genre"][:])
        print "Genre: " + self.default_InfoStr["tml_Genre"][1] + "\r\n"


    def input_date(self, date=u"1900"):
        self.default_InfoStr["tml_Date"][1] = date
        self.cuefile_Cache.append(self.default_InfoStr["tml_Date"][:])
        print "Date: " + self.default_InfoStr["tml_Date"][1] + "\r\n"
        
        
    def input_album_performer(self, performer=u"Null"):
        self.default_InfoStr["tml_AlbumPerformer"][1] = performer
        self.cuefile_Cache.append(self.default_InfoStr["tml_AlbumPerformer"][:])
        print "Album Performer: " + self.default_InfoStr["tml_AlbumPerformer"][1] + "\r\n"
        
        
    def input_album_title(self, title=u"Null"):
        self.default_InfoStr["tml_AlbumTitle"][1] = title
        self.cuefile_Cache.append(self.default_InfoStr["tml_AlbumTitle"][:])
        print "Album Title: " + self.default_InfoStr["tml_AlbumTitle"][1] + "\r\n"
        
        
    def input_album_path(self):
        self.cuefile_Cache.append(self.default_InfoStr["tml_AlbumPath"][:])
        print "Album Path: " + self.default_InfoStr["tml_AlbumPath"][1] + "\r\n"
        
    
    def input_track_title(self, title=u"Null"):
        self.default_InfoStr["tml_TrackTitle"][1] = title
        self.cuefile_Cache.append(self.default_InfoStr["tml_TrackTitle"][:])
        print "Track Title: " + self.default_InfoStr["tml_TrackTitle"][1] + "\r\n"
        
        
    def input_track_performer(self, performer=u"Null"):
        if performer != u"Null":
            self.default_InfoStr["tml_TrackPerformer"][1] = performer
            self.cuefile_Cache.append(self.default_InfoStr["tml_TrackPerformer"][:])
            print "Track Title: " + self.default_InfoStr["tml_TrackPerformer"][1] + "\r\n"
        else:
            print "Track Title: " + self.default_InfoStr["tml_AlbumPerformer"][1] + "\r\n"
            
            
    def input_track_index00(self, time=u"000000"):
        self.default_InfoStr["tml_TrackIndex00"][1] = time[:2]
        self.default_InfoStr["tml_TrackIndex00"][3] = time[2:4]
        self.default_InfoStr["tml_TrackIndex00"][5] = time[4:6]
        self.cuefile_Cache.append(self.default_InfoStr["tml_TrackIndex00"][:])
        print ("Track Index00: " + self.default_InfoStr["tml_TrackIndex00"][1] + ":"
                                 + self.default_InfoStr["tml_TrackIndex00"][3] + ":"
                                 + self.default_InfoStr["tml_TrackIndex00"][5] + "\r\n")
    
    
    def input_track_index01(self, time=u"000000"):
        self.default_InfoStr["tml_TrackIndex01"][1] = time[:2]
        self.default_InfoStr["tml_TrackIndex01"][3] = time[2:4]
        self.default_InfoStr["tml_TrackIndex01"][5] = time[4:6]
        self.cuefile_Cache.append(self.default_InfoStr["tml_TrackIndex01"][:])
        print ("Track Index01: " + self.default_InfoStr["tml_TrackIndex01"][1] + ":"
                                 + self.default_InfoStr["tml_TrackIndex01"][3] + ":"
                                 + self.default_InfoStr["tml_TrackIndex01"][5] + "\r\n")


    def input_track_info(self, title=u"Null", performer=u"Null", time00=u"Null", time01=u"000000"):
        self.input_track_title(title)
        self.input_track_performer(performer)
        if time00 != u"Null":
            self.input_track_index00(time00)
        self.input_track_index01(time01)        
          
          
    def makeFile(self):
        self.cuefile = codecs.open((self.default_InfoStr["tml_AlbumPath"][1] + u".cue"), "w+", "utf-8")
        for item in self.cuefile_Cache:
            self.cuefile.write(("".join(item)) + u"\r\n")
        self.cuefile.close()
        


def generate_cuefile():
    input_str = raw_input("Do u want to make a cue file? Y/N\r\n")
    if input_str.upper() == "Y":
        input_str = raw_input("Pls input WAV file path.\r\n")
        cuefile = CueFile(input_str.decode("utf-8"))
        input_str = raw_input("Pls input Genre.\r\n")
        cuefile.input_genre(input_str.decode("utf-8"))
        input_str = raw_input("Pls input Date.\r\n")
        cuefile.input_date(input_str.decode("utf-8"))
        input_str = raw_input("Pls input Album Title.\r\n")
        cuefile.input_album_title(input_str.decode("utf-8"))
        input_str = raw_input("Pls input Album Performance.\r\n")
        cuefile.input_album_performer(input_str.decode("utf-8"))
        cuefile.input_album_path()
        input_str = raw_input("Pls input Track Volume.\r\n")
        cuefile.cuefile_TrackVolume = int(input_str.decode("utf-8"))
        
        for dummy_idx in range(cuefile.cuefile_TrackVolume):
            input_str_list = []
            if dummy_idx < 9:
                cuefile.default_InfoStr["tml_TrackNum"][1] = unicode("0" + str(dummy_idx + 1))
            else:
                cuefile.default_InfoStr["tml_TrackNum"][1] = unicode(str(dummy_idx + 1))
            input_str_list.append(cuefile.cuefile_Cache.append(cuefile.default_InfoStr["tml_TrackNum"][:]))
            input_str_list.append(raw_input("Pls input Track Title.\r\n").decode("utf-8"))
            input_str_list.append(raw_input("Pls input Track Performer.\r\n").decode("utf-8"))
            input_str_list.append(raw_input("Pls input Track Index00.\r\n").decode("utf-8"))
            input_str_list.append(raw_input("Pls input Track Index01.\r\n").decode("utf-8"))
            cuefile.input_track_info(input_str_list[1], input_str_list[2], input_str_list[3], input_str_list[4])
        
        cuefile.makeFile()
        print "CUE file have been successfully made."


if __name__ == '__main__':
    generate_cuefile()
    pass