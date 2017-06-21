init python: 
    m = MusicRoom(fadeout = 0.7) 

    #m.add("music/mainmenu_amb.wav",always_unlocked=True)
    m.add("music/terrain.mp3", always_unlocked=True)
    m.add("music/gallery.mp3", always_unlocked=True)
    m.add("music/game.mp3", always_unlocked=True)  
    m.add("music/good_ending.mp3", always_unlocked=True) 
    m.add("music/bad_ending.mp3", always_unlocked=True) 
## "music/m1.mp3" - расположение самой песни 
### always_unlocked - при значении true, будет всегда открыта, даже если не проигрывалась непосредственно в игре. 
screen music_rm:   
    tag menu   
    add "images/bg/bg_white.png"  

    #textbutton "Yourenigma - My Little Nocturne" action m.Play("music/mainmenu_amb.wav") xalign 0.5 yalign 0.1 xminimum 570
    textbutton "Terrain" action m.Play("music/terrain.mp3") xalign 0.5 yalign 0.15 xminimum 570
    textbutton "Gallery music" action m.Play("music/gallery.mp3") xalign 0.5 yalign 0.2 xminimum 570
    textbutton "Game ambient" action m.Play("music/game.mp3") xalign 0.5 yalign 0.25 xminimum 570
    textbutton "Good ending " action m.Play("music/good_ending.mp3") xalign 0.5 yalign 0.3 xminimum 570
    textbutton "Bad ending" action m.Play("music/bad_ending.mp3") xalign 0.5 yalign 0.35 xminimum 570
    
# "Yourenigma - My Little Nocturne" - название, выводимое на кнопке. 
# action m.Play("music/m1.mp3") - по нажатии проигрывать m1.mp3. 
# xalign 0.5 yalign 0.2 - расположение по координатам X, Y. 
# xminimum 570 - установление минимальной ширины кнопки - 570 пикселей. 
#Добавим кнопки управления 
    textbutton "->" action m.Next() xalign 0.83 yalign 0.95 xmaximum 300   
#....По нажатию будет проигрываться предыдущая песня из списка. 

    textbutton "<-" action m.Previous() xalign 0.75 yalign 0.95 xmaximum 300 
#....По нажатию будет проигрываться следующая песня из списка. 

    textbutton "Стоп" action Stop("music") xalign 0.8 yalign 0.95   
#....Останавливает проигрывающую песню. 

    label _("Громкость") xalign 0.965 yalign 0.9  
#Создаём надпись "Громкость" 
    bar value Preference("music volume") xalign 0.99 yalign 0.95 xmaximum 180 
#Добавляем ползунок регулировки громкости музыки. 

    textbutton "Назад" action ShowMenu("gallery") xalign 0.5 yalign 0.95   

    #on "replace" action m.Play("music/m1.mp3") 
#Проигрывать песню m1.mp3, при входе в музыкальную комнату. 
    #on "replaced" action Play("music", "music/main_menu.mp3")   
#Проигрывание музыки после выхода из комнаты. Можно указать музыку главного меню. 