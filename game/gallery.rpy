init python:
    g = Gallery()
    g.transitions = dissolve

#menu gallery
screen gallery:
    tag menu
    add "images/bg/bg_black.png"
    frame:
        style_group "mm"
        xalign .50
        yalign .50

        has vbox
        textbutton _("Персонажи") action ShowMenu("character")
        textbutton _("Иллюстрации") action ShowMenu("illustration")
        textbutton _("Музыка") action ShowMenu("music_rm")
        textbutton _("Главное меню") action ShowMenu("main_menu")

# menu character 
screen character: 
    python:
        g.button("sk1")
        if persistent.sk1=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk1.png") 
            
        g.button("sk2") 
        if persistent.sk2=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk2.png") 

        g.button("sk3") 
        if persistent.sk3=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk3.png") 
        g.button("sk4") 
        if persistent.sk4=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk4.png") 

        g.button("sk5") 
        if persistent.sk5=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk5.png") 

        g.button("sk6") 
        if persistent.sk6=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk6.png")

        g.button("sk7") 
        if persistent.sk6=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk7.png")

        g.button("sk8") 
        if persistent.sk6=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk8.png")

        g.button("sk9") 
        if persistent.sk6=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Character/sk9.png")

 # create bttons for picture
             
    tag menu 
    add "images/gallery/fong.png"
    grid 3 3:
        xfill True
        yfill True
        add g.make_button("sk1", "images/gallery/Character/sk1_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk2", "images/gallery/Character/sk2_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk3", "images/gallery/Character/sk3_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk4", "images/gallery/Character/sk4_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk5", "images/gallery/Character/sk5_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk6", "images/gallery/Character/sk6_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk7", "images/gallery/Character/sk7_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk8", "images/gallery/Character/sk8_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk9", "images/gallery/Character/sk9_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)

   # textbutton "Следующая страница" action ShowMenu("character2") xalign 0.85 yalign 0.99
    textbutton "Назад" action ShowMenu("gallery") xalign 0.5 yalign 0.99

# menu illustartion

screen illustration:
    python:
        g.button("sk10") 
        if persistent.sk7=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk10.png") 
            
        g.button("sk11") 
        if persistent.sk8=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk11.png") 

        g.button("sk12") 
        if persistent.sk9=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk12.png")

        g.button("sk13") 
        if persistent.sk10=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk13.png") 

        g.button("sk14") 
        if persistent.sp11=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk14.png") 

        g.button("sk15") 
        if persistent.sp12=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk15.png")

        g.button("sk16") 
        if persistent.sk10=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk16.png") 

        g.button("sk17") 
        if persistent.sp11=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk17.png") 

        g.button("sk18") 
        if persistent.sp12=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk18.png")

    tag menu 
    #add "images/gallery/fong.png"
    add "black"
    grid 3 3:
        xfill True
        yfill True
        add g.make_button("sk10", "images/gallery/Illustration/sk10_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk11", "images/gallery/Illustration/sk11_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk12", "images/gallery/Illustration/sk12_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk13", "images/gallery/Illustration/sk13_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk14", "images/gallery/Illustration/sk14_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk15", "images/gallery/Illustration/sk15_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk16", "images/gallery/Illustration/sk16_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk17", "images/gallery/Illustration/sk17_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk18", "images/gallery/Illustration/sk18_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
    
    textbutton "Следующая страница" action ShowMenu("illustration2") xalign 0.9 yalign 0.99
    textbutton "Назад" action ShowMenu("gallery") xalign 0.5 yalign 0.99

screen illustration2:
    python:
        g.button("sk19") 
        if persistent.sk7=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk19.png") 
            
        g.button("sk20") 
        if persistent.sk8=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk20.png") 

        g.button("sk21") 
        if persistent.sk9=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk21.png")

        g.button("sk22") 
        if persistent.sk10=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk22.png") 

        g.button("sk23") 
        if persistent.sp11=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/Illustration/sk23.png")

        g.button("sk24") 
        if persistent.sp11=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/fong.png")

    tag menu 
    #add "images/gallery/fong.png"
    add "black"
    grid 3 2:
        xfill True
        yfill True
        add g.make_button("sk19", "images/gallery/Illustration/sk19_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk20", "images/gallery/Illustration/sk20_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk21", "images/gallery/Illustration/sk21_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk22", "images/gallery/Illustration/sk22_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1) 
        add g.make_button("sk23", "images/gallery/Illustration/sk23_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)
        add g.make_button("sk23", "images/gallery/fong.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.1)

    textbutton "Предыдущая страница" action ShowMenu("illustration") xalign 0.1 yalign 0.99
    #textbutton "Назад" action ShowMenu("gallery") xalign 0.5 yalign 0.99
