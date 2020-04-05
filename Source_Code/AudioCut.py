from pydub import AudioSegment

def cutaudio(inputfile, label, maxtime, start_point):
    t1 = start_point
    # cut the sample by 5 second if you want another second change the plus var
    t2 = t1+5
    max_time = t1 + maxtime

    while t1<max_time:
        #in pydub use ms second so multiple 1000
        #start
        st1 = t1*1000
        #end 
        et2 = t2*1000
        newAudio = AudioSegment.from_wav(inputfile)
        newAudio = newAudio[st1:et2]
        #make naming numbering
        number = t1/5
        name = str(number)+label
        newAudio.export('audio8/'+name+'.wav', format="wav")
        t1 = t1+5
        t2 = t1+5

cutaudio("SeaSound (1).wav","1sea-1",250, 0) # 50

cutaudio("SeaSound (2).wav","2sea-1",160, 0) # 64
cutaudio("SeaSound (2).wav","2-1sea-1",160, 300) 

cutaudio("SeaSound (3).wav","3sea-1",95, 0)
cutaudio("SeaSound (3).wav","3-1sea-1",95, 180)
cutaudio("SeaSound (3).wav","3-2sea-1",100, 360)

cutaudio("SeaSound (4).wav","4sea-1",95, 0)
cutaudio("SeaSound (4).wav","4-1sea-1",95, 180)
cutaudio("SeaSound (4).wav","4-2sea-1",95, 360)

cutaudio("SeaSound (5).wav","5sea-1",95, 0)
cutaudio("SeaSound (5).wav","5-1sea-1",95, 140)
cutaudio("SeaSound (5).wav","5-2sea-1",95, 280)

cutaudio("SeaSound (6).wav","6sea-1",95, 0)
cutaudio("SeaSound (6).wav","6-1sea-1",95, 180)
cutaudio("SeaSound (6).wav","6-2sea-1",95, 360)

cutaudio("SeaSound (7).wav","7sea-1",95, 0)
cutaudio("SeaSound (7).wav","7-1sea-1",95, 120)
cutaudio("SeaSound (7).wav","7-2sea-1",95, 240)



"""

cutaudio("FactorySound (1).wav","1factory-3",200)
cutaudio("FactorySound (2).wav","2factory-3",200)
cutaudio("FactorySound (3).wav","3factory-3",200)
cutaudio("FactorySound (4).wav","4factory-3",200)
cutaudio("FactorySound (5).wav","5factory-3",200)

cutaudio("ClubSound (1).wav","1club-8",400) # 45
cutaudio("ClubSound (2).wav","2club-8",25) # 5
cutaudio("ClubSound (3).wav","3club-8",200) # 40
cutaudio("ClubSound (4).wav","4club-8",160) # 40
cutaudio("ClubSound (5).wav","1club-8",25) # 5
cutaudio("ClubSound (6).wav","5club-8",80) # 16
cutaudio("ClubSound (7).wav","1club-8",120) # 44

cutaudio("HarborSound (1).wav","1harbor-5",300)
cutaudio("HarborSound (3).wav","2harbor-5",270)
cutaudio("HarborSound (4).wav","3harbor-5",200)
cutaudio("HarborSound (5).wav","4harbor-5",50)
cutaudio("HarborSound (6).wav","harbor-5",400)

cutaudio("MountainSound (1).wav","1mountain-0",200)
cutaudio("MountainSound (2).wav","2mountain-0",200)
cutaudio("MountainSound (3).wav","3mountain-0",200)
cutaudio("MountainSound (4).wav","4mountain-0",200)
cutaudio("MountainSound (5).wav","5mountain-0",200)

cutaudio("MusicConcertSound (1).wav","1musicconcert-6",200)
cutaudio("MusicConcertSound (2).wav","2musicconcert-6",200)
cutaudio("MusicConcertSound (3).wav","3musicconcert-6",200)
cutaudio("MusicConcertSound (4).wav","4musicconcert-6",200)
cutaudio("MusicConcertSound (5).wav","5musicconcert-6",200)

cutaudio("SeaSound (1).wav","1sea-1",200)
cutaudio("SeaSound (2).wav","2sea-1",200)
cutaudio("SeaSound (3).wav","3sea-1",200)
cutaudio("SeaSound (4).wav","4sea-1",200)
cutaudio("SeaSound (5).wav","5sea-1",200)



cutaudio("도서관.wav","1library-11", 110, 0)
cutaudio("도서관.wav","1-1library-11", 110, 360)
cutaudio("도서관.wav","1-2library-11", 110, 720)
cutaudio("도서관2.wav","2library-11", 330, 0)
cutaudio("도서관3.wav","3library-11", 340, 0)

cutaudio("사무실1.wav","1office-11", 300, 0)
cutaudio("사무실2.wav","2office-11", 120, 0)
cutaudio("사무실2.wav","2-1office-11", 110, 600)
cutaudio("사무실2.wav","2-2office-11", 120, 1200)
cutaudio("사무실3.wav","3office-11", 110, 0)
cutaudio("사무실3.wav","3-1office-11", 120, 600)
cutaudio("사무실3.wav","3-2office-11", 120, 1200)

cutaudio("집1.wav","1home-9", 250, 0)
cutaudio("집1.wav","1-1home-9", 250, 300)
cutaudio("집2.wav","2home-9", 250, 0)
cutaudio("집2.wav","2-1home-9", 250, 450)

cutaudio("카페.wav","cafe-14", 55, 0)
cutaudio("카페.wav","1-1cafe-14", 55, 1200)
cutaudio("카페.wav","1-2cafe-14", 55, 2400)
cutaudio("카페.wav","1-3cafe-14", 55, 3600)
cutaudio("카페.wav","1-4cafe-14", 55, 4800)
cutaudio("카페.wav","1-5cafe-14", 55, 6000)
cutaudio("카페2.wav","2cafe-14", 55, 0)
cutaudio("카페2.wav","2-1cafe-14", 55, 600)
cutaudio("카페2.wav","2-2cafe-14", 55, 1200)
cutaudio("카페2.wav","2-3cafe-14", 55, 1800)
cutaudio("카페2.wav","2-4cafe-14", 55, 2400)
cutaudio("카페2.wav","2-5cafe-14", 55, 3000)
cutaudio("카페4.wav","4cafe-14", 110, 0)
cutaudio("카페4.wav","4cafe-14", 110, 600)
cutaudio("카페4.wav","4cafe-14", 120, 1200)



#66개 2 67개 4개
cutaudio("library1.wav","1library-11", 110, 0)
cutaudio("library1.wav","1-1library-11", 110, 600)
cutaudio("library1.wav","1-2library-11", 110, 1200)

cutaudio("library2.wav","2library-11", 110, 0)
cutaudio("library2.wav","2-1library-11", 110, 420)
cutaudio("library2.wav","2-2library-11", 110, 840)

cutaudio("library3.wav","3library-11", 110, 0)
cutaudio("library3.wav","3-1library-11", 110, 120)
cutaudio("library3.wav","3-2library-11", 115, 240)

cutaudio("library4.wav","4library-11", 110, 0)
cutaudio("library4.wav","4-1library-11", 110, 180)
cutaudio("library4.wav","4-2library-11", 115, 360)

cutaudio("library5.wav","5library-11", 110, 0)
cutaudio("library5.wav","5-1library-11", 110, 300)
cutaudio("library5.wav","5-2library-11", 115, 600)

cutaudio("library6.wav","6library-11", 110, 0)
cutaudio("library6.wav","6-1library-11", 110, 300)
cutaudio("library6.wav","6-2library-11", 115, 600)

cutaudio("class1.wav","1lectureroom-13",55, 0)
cutaudio("class1.wav","1-1lectureroom-13",55, 720)
cutaudio("class1.wav","1-2lectureroom-13",55, 1440)
cutaudio("class1.wav","1-3lectureroom-13",55, 2160)
cutaudio("class1.wav","1-4lectureroom-13",65, 2880)

cutaudio("class2.wav","2lectureroom-13",55, 0)
cutaudio("class2.wav","2-1lectureroom-13",55, 600)
cutaudio("class2.wav","2-2lectureroom-13",55, 1200)
cutaudio("class2.wav","2-3lectureroom-13",55, 1800)
cutaudio("class2.wav","2-4lectureroom-13",65, 2400)

cutaudio("class3.wav","3lectureroom-13",95,0)
cutaudio("class3.wav","3-1lectureroom-13",95,240)
cutaudio("class3.wav","3-2lectureroom-13",95,480)

cutaudio("class4.wav","4lectureroom-13",95,0)
cutaudio("class4.wav","4-1lectureroom-13",95,420)
cutaudio("class4.wav","4-2lectureroom-13",95,840)

cutaudio("class5.wav","5lectureroom-13",95,0)
cutaudio("class5.wav","5-1lectureroom-13",95,240)
cutaudio("class5.wav","5-2lectureroom-13",95,480)

cutaudio("class6.wav","6lectureroom-13",95,0)
cutaudio("class6.wav","6-1lectureroom-13",95,300)
cutaudio("class6.wav","6-2lectureroom-13",95,600)

cutaudio("class7.wav","7lectureroom-13",95,0)
cutaudio("class7.wav","7-1lectureroom-13",95,300)
cutaudio("class7.wav","7-2lectureroom-13",100,600)

#7개 파일로부터 400개 57, 58
cutaudio("home1.wav","1home-9", 95, 0)
cutaudio("home1.wav","1-1home-9", 95, 180)
cutaudio("home1.wav","1-1home-9", 95, 360)

cutaudio("home2.wav","2home-9", 95, 0)
cutaudio("home2.wav","2-1home-9", 95, 300)
cutaudio("home2.wav","2-2home-9", 95, 600)

cutaudio("home3.wav","3home-9", 95, 0)
cutaudio("home3.wav","3-1home-9", 95, 120)
cutaudio("home3.wav","3-2home-9", 95, 230)

cutaudio("home4.wav","4home-9", 95, 0)
cutaudio("home4.wav","4-1home-9", 95, 480)
cutaudio("home4.wav","4-2home-9", 95, 960)

cutaudio("home5.wav","5home-9", 95, 0)
cutaudio("home5.wav","5-1home-9", 95, 180)
cutaudio("home5.wav","5-2home-9", 95, 360)

cutaudio("home6.wav","6home-9", 95, 0)
cutaudio("home6.wav","6-1home-9", 95, 240)
cutaudio("home6.wav","6-2home-9", 95, 480)

cutaudio("home7.wav","7home-9", 95, 0)
cutaudio("home7.wav","7-1home-9", 95, 180)
cutaudio("home7.wav","7-2home-9", 100, 360)

#각 샘플당 57개 , 용량이 큰 샘플인 경우에는 58개
cutaudio("cafe1.wav","1cafe-14", 95, 0)
cutaudio("cafe1.wav","1-1cafe-14", 95, 480)
cutaudio("cafe1.wav","1-2cafe-14", 95, 960)

cutaudio("cafe2.wav","2cafe-14", 55, 0)
cutaudio("cafe2.wav","2-1cafe-14", 55, 1080)
cutaudio("cafe2.wav","2-2cafe-14", 55, 2160)
cutaudio("cafe2.wav","2-3cafe-14", 55, 3240)
cutaudio("cafe2.wav","2-4cafe-14", 55, 4320)
cutaudio("cafe2.wav","2-5cafe-14", 65, 5400)

cutaudio("cafe3.wav","3cafe-14", 55, 0)
cutaudio("cafe3.wav","3-1cafe-14", 55, 600)
cutaudio("cafe3.wav","3-2cafe-14", 55, 1200)
cutaudio("cafe3.wav","3-3cafe-14", 55, 1800)
cutaudio("cafe3.wav","3-4cafe-14", 55, 2400)
cutaudio("cafe3.wav","3-5cafe-14", 65, 3000)

cutaudio("cafe4.wav","4cafe-14", 55, 0)
cutaudio("cafe4.wav","4-1cafe-14", 55, 300)
cutaudio("cafe4.wav","4-2cafe-14", 55, 600)
cutaudio("cafe4.wav","4-3cafe-14", 55, 900)
cutaudio("cafe4.wav","4-4cafe-14", 55, 1200)
cutaudio("cafe4.wav","4-5cafe-14", 55, 1500)

cutaudio("cafe5.wav","5cafe-14", 55, 0)
cutaudio("cafe5.wav","5-1cafe-14", 55, 180)
cutaudio("cafe5.wav","5-2cafe-14", 55, 360)
cutaudio("cafe5.wav","5-3cafe-14", 55, 540)
cutaudio("cafe5.wav","5-4cafe-14", 55, 720)
cutaudio("cafe5.wav","5-5cafe-14", 55, 900)

cutaudio("cafe6.wav","6cafe-14", 55, 0)
cutaudio("cafe6.wav","6-1cafe-14", 55, 120)
cutaudio("cafe6.wav","6-2cafe-14", 55, 240)
cutaudio("cafe6.wav","6-3cafe-14", 55, 360)
cutaudio("cafe6.wav","6-4cafe-14", 55, 480)
cutaudio("cafe6.wav","6-5cafe-14", 55, 600)

cutaudio("cafe7.wav","7cafe-14", 55, 0)
cutaudio("cafe7.wav","7-1cafe-14", 55, 120)
cutaudio("cafe7.wav","7-2cafe-14", 55, 240)
cutaudio("cafe7.wav","7-3cafe-14", 55, 360)
cutaudio("cafe7.wav","7-4cafe-14", 55, 480)
cutaudio("cafe7.wav","7-5cafe-14", 55, 600)

#한개 60 나머지 78개
cutaudio("office1.wav","1office-11", 300, 0)

cutaudio("office2.wav","2office-11", 130, 0)
cutaudio("office2.wav","2-1office-11", 130, 600)
cutaudio("office2.wav","2-2office-11", 130, 1200)

cutaudio("office3.wav","3office-11", 130, 0)
cutaudio("office3.wav","3-1office-11", 130, 720)
cutaudio("office3.wav","3-2office-11", 130, 1440)

cutaudio("office4.wav","4office-11", 130, 0)
cutaudio("office4.wav","4-1office-11", 130, 300)
cutaudio("office4.wav","4-2office-11", 130, 600)

cutaudio("office5.wav","5office-11", 130, 0)
cutaudio("office5.wav","5-1office-11", 130, 180)
cutaudio("office5.wav","5-2office-11", 130, 360)

cutaudio("office6.wav","6office-11", 130, 0)
cutaudio("office6.wav","6-1office-11", 130, 240)
cutaudio("office6.wav","6-2office-11", 130, 480)

#66 개 4 68 2개 
cutaudio("traffic1.wav","1road-12", 330, 0)

cutaudio("traffic2.wav","2road-12", 165, 0)
cutaudio("traffic2.wav","2-1road-12", 165, 300)

cutaudio("traffic3.wav","3road-12", 110, 0)
cutaudio("traffic3.wav","3-1road-12", 110, 420)
cutaudio("traffic3.wav","3-2road-12", 110, 840)

cutaudio("traffic4.wav","4road-12", 110, 0)
cutaudio("traffic4.wav","4-1road-12", 110, 300)
cutaudio("traffic4.wav","4-2road-12", 110, 600)

cutaudio("traffic5.wav","5road-12", 110, 0)
cutaudio("traffic5.wav","5-1road-12", 110, 180)
cutaudio("traffic5.wav","5-2road-12", 120, 360)

cutaudio("traffic6.wav","6road-12", 110, 0)
cutaudio("traffic6.wav","6-1road-12", 110, 180)
cutaudio("traffic6.wav","6-2road-12", 120, 360)

#40개씩 
cutaudio("AirportSound (1).wav","1airport-4",100, 0)
cutaudio("AirportSound (1).wav","1-1airport-4",100, 240)

cutaudio("AirportSound (2).wav","2airport-4",100, 0)
cutaudio("AirportSound (2).wav","2-2airport-4",100, 300)

cutaudio("AirportSound (3).wav","3airport-4",150, 0)

cutaudio("AirportSound (4).wav","4airport-4",125, 0)
cutaudio("AirportSound (4).wav","4-1airport-4",125, 240)

cutaudio("AirportSound (5).wav","5airport-4",100, 0)
cutaudio("AirportSound (5).wav","5-1airport-4",100, 240)

cutaudio("AirportSound (6).wav","6airport-4",100, 0)
cutaudio("AirportSound (6).wav","6-1airport-4",100, 180)

cutaudio("AirportSound (7).wav","7airport-4",30, 0)

cutaudio("AirportSound (8).wav","8airport-4",150, 0)
cutaudio("AirportSound (8).wav","8-1airport-4",150, 300)

cutaudio("AirportSound (9).wav","9airport-4",70, 0)

cutaudio("AirportSound (10).wav","10airport-4",100, 0)
cutaudio("AirportSound (10).wav","10-1airport-4",100, 300)

cutaudio("AirportSound (11).wav","11airport-4",100, 0)
cutaudio("AirportSound (11).wav","11-1airport-4",100, 180)

# 66 4개 68 2개
cutaudio("CaveSound (1).wav","1cave-2",165,0)
cutaudio("CaveSound (1).wav","1-1cave-2",165,300)

cutaudio("CaveSound (2).wav","2cave-2",165,0)
cutaudio("CaveSound (2).wav","2-1cave-2",165,300)

cutaudio("CaveSound (3).wav","3cave-2",185,0)
cutaudio("CaveSound (3).wav","3-1cave-2",185,300)

cutaudio("CaveSound (4).wav","4cave-2",120,0)

cutaudio("CaveSound (5).wav","5cave-2",210,0)
cutaudio("CaveSound (5).wav","5-1cave-2",215,300)

cutaudio("CaveSound (6).wav","6cave-2",210,0)
cutaudio("CaveSound (6).wav","6-1cave-2",215,300)

#57 6개 58 1개

cutaudio("Classic (1).wav","1classic-7",285, 0)

cutaudio("Classic (2).wav","2classic-7",285, 0)

cutaudio("Classic (3).wav","3classic-7",145, 0)
cutaudio("Classic (3).wav","3-1classic-7",145, 360)

cutaudio("Classic (4).wav","4classic-7",140, 0)
cutaudio("Classic (4).wav","4-1classic-7",140, 210)

cutaudio("Classic (5).wav","5classic-7",145, 0)
cutaudio("Classic (5).wav","5-1classic-7",145, 300)

cutaudio("Classic (6).wav","6classic-7",145, 0)
cutaudio("Classic (6).wav","6-1classic-7",145, 360)

cutaudio("Classic (7).wav","7classic-7",280, 0)

# 40개 -> 10개

cutaudio("Club (1).wav","1club-8",200, 0) # 40

cutaudio("Club (2).wav","2club-8",170, 0) # 34

cutaudio("Club (3).wav","3club-8",25, 0) # 5

cutaudio("Club (4).wav","4club-8",80,0) # 16

cutaudio("Club (5).wav","5club-8",125, 0) # 25

cutaudio("Club (6).wav","6club-8",210, 0) # 42

cutaudio("Club (7).wav","7club-8",130, 0) # 26
cutaudio("Club (7).wav","7-1club-8",130, 240) # 26
cutaudio("Club (7).wav","7-2club-8",130, 480) # 26

cutaudio("Club (8).wav","8club-8",130, 0) # 26
cutaudio("Club (8).wav","8-1club-8",130, 240) # 26
cutaudio("Club (8).wav","8-2club-8",130, 480) # 26

cutaudio("Club (9).wav","9club-8",385, 0) # 77

cutaudio("Club (10).wav","10club-8",25, 0) # 5

cutaudio("FactorySound (1).wav","1factory-3",110, 0)
cutaudio("FactorySound (1).wav","1-1factory-3",110, 180)
cutaudio("FactorySound (1).wav","1-2factory-3",110, 360)

cutaudio("FactorySound (2).wav","2factory-3",165, 0)
cutaudio("FactorySound (2).wav","2factory-3",165, 210)

cutaudio("FactorySound (3).wav","3factory-3",110, 0)
cutaudio("FactorySound (3).wav","3-1factory-3",110, 180)
cutaudio("FactorySound (3).wav","3-2factory-3",110, 360)

cutaudio("FactorySound (4).wav","4factory-3",110, 0)
cutaudio("FactorySound (4).wav","4-1factory-3",110, 180)
cutaudio("FactorySound (4).wav","4-2factory-3",110, 360)

cutaudio("FactorySound (5).wav","5factory-3",110, 0)
cutaudio("FactorySound (5).wav","5-1factory-3",110, 180)
cutaudio("FactorySound (5).wav","5-2factory-3",120, 360)

cutaudio("FactorySound (6).wav","6factory-3",110, 0)
cutaudio("FactorySound (6).wav","6-1factory-3",110, 180)
cutaudio("FactorySound (6).wav","6-2factory-3",120, 360)

cutaudio("Harbor Sound (1).wav","1harbor-5",55, 0) # 11

cutaudio("Harbor Sound (2).wav","2harbor-5",200, 0)
cutaudio("Harbor Sound (2).wav","2-1harbor-5",265, 360)

cutaudio("Harbor Sound (3).wav","3harbor-5",175, 0)
cutaudio("Harbor Sound (3).wav","3-1harbor-5",240, 300)

cutaudio("Harbor Sound (4).wav","4harbor-5",200, 0)
cutaudio("Harbor Sound (4).wav","4-1harbor-5",265, 360)

cutaudio("Harbor Sound (5).wav","5harbor-5",150, 0) # 60
cutaudio("Harbor Sound (5).wav","5-1harbor-5",150, 180)

cutaudio("Harbor Sound (6).wav","6harbor-5",300, 0) # 60

cutaudio("Harbor Sound (7).wav","6harbor-5",195, 0) # 39 

cutaudio("MountainSound (1).wav","1mountain-0",110, 0)
cutaudio("MountainSound (1).wav","1-1mountain-0",110, 240)
cutaudio("MountainSound (1).wav","1-2mountain-0",110, 480)

cutaudio("MountainSound (2).wav","2mountain-0",110, 0)
cutaudio("MountainSound (2).wav","2-1mountain-0",110, 180)
cutaudio("MountainSound (2).wav","2-2mountain-0",110, 360)

cutaudio("MountainSound (3).wav","3mountain-0",210, 0) # 42

cutaudio("MountainSound (4).wav","4mountain-0",390, 0) # 78

cutaudio("MountainSound (5).wav","5mountain-0",185, 0)
cutaudio("MountainSound (5).wav","5-1mountain-0",185, 360)

cutaudio("MountainSound (6).wav","6mountain-0",185, 0)
cutaudio("MountainSound (6).wav","6-1mountain-0",185, 360)

cutaudio("MusicConcert (1).wav","1musicconcert-6",100, 0)
cutaudio("MusicConcert (1).wav","1-1musicconcert-6",100, 300)

cutaudio("MusicConcert (2).wav","2musicconcert-6",100, 0)
cutaudio("MusicConcert (2).wav","2-1musicconcert-6",100, 240)

cutaudio("MusicConcert (3).wav","3musicconcert-6",100, 0)
cutaudio("MusicConcert (3).wav","3-1musicconcert-6",100, 210)

cutaudio("MusicConcert (4).wav","4musicconcert-6",100, 0)
cutaudio("MusicConcert (4).wav","4-1musicconcert-6",100, 180)

cutaudio("MusicConcert (5).wav","5musicconcert-6",100, 0)
cutaudio("MusicConcert (5).wav","5-1musicconcert-6",100, 240)

cutaudio("MusicConcert (6).wav","6musicconcert-6",100, 0)
cutaudio("MusicConcert (6).wav","6-1musicconcert-6",100, 150)

cutaudio("MusicConcert (7).wav","7musicconcert-6",100, 0)
cutaudio("MusicConcert (7).wav","7-1musicconcert-6",100, 420)

cutaudio("MusicConcert (8).wav","8musicconcert-6",200, 0)

cutaudio("MusicConcert (9).wav","9musicconcert-6",200, 0)

cutaudio("MusicConcert (10).wav","10musicconcert-6",200, 0)
"""

