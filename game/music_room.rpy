init python: 
    m = MusicRoom(fadeout = 1.0) 

    m.add("music/mainmenu_amb.wav",always_unlocked=True)   
## "music/m1.mp3" - расположение самой песни 
### always_unlocked - при значении true, будет всегда открыта, даже если не проигрывалась непосредственно в игре. 
screen music_rm:   
    tag menu   
    add "images/gallery/fong.png"   
# Добавляем фоновое изображение. 
# Сейчас создадим кнопки проигрывания, для каждой песни, свою. Я буду применять textbutton. 
    textbutton "Yourenigma - My Little Nocturne;" action m.Play("music/mainmenu_amb.wav") xalign 0.5 yalign 0.2 xminimum 570
    
# "Yourenigma - My Little Nocturne" - название, выводимое на кнопке. 
# action m.Play("music/m1.mp3") - по нажатии проигрывать m1.mp3. 
# xalign 0.5 yalign 0.2 - расположение по координатам X, Y. 
# xminimum 570 - установление минимальной ширины кнопки - 570 пикселей. 
#Добавим кнопки управления 
    #textbutton "Следующая ->" action m.Next() xalign 0.99 yalign 0.94 xmaximum 300   
#....По нажатию будет проигрываться предыдущая песня из списка. 

    #textbutton "<-Предыдущая" action m.Previous() xalign 0.99 yalign 0.99 xmaximum 300 
#....По нажатию будет проигрываться следующая песня из списка. 

    textbutton "Стоп" action Stop("music") xalign 0.7 yalign 0.99   
#....Останавливает проигрывающую песню. 

    label _("Громкость") xalign 0.4 yalign 0.95   
#Создаём надпись "Громкость" 
    bar value Preference("music volume") xalign 0.45 yalign 0.99 xmaximum 180 
#Добавляем ползунок регулировки громкости музыки. 

    textbutton "Главное меню" action ShowMenu("main_menu") xalign 0.01 yalign 0.99   

    #on "replace" action m.Play("music/m1.mp3") 
#Проигрывать песню m1.mp3, при входе в музыкальную комнату. 
    #on "replaced" action Play("music", "music/main_menu.mp3")   
#Проигрывание музыки после выхода из комнаты. Можно указать музыку главного меню. 