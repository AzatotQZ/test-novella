init python:
   g = Gallery()
   g.transition = dissolve

screen gallery: 
    python:
        g.button("sk1") 
        if persistent.sk1=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk1.png") 
            
        g.button("sk2") 
        if persistent.sk2=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk2.png") 

        g.button("sk3") 
        if persistent.sk3=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk3.png") 
        g.button("sk4") 
        if persistent.sk4=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk4.png") 

        g.button("sk5") 
        if persistent.sk5=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk5.png") 

        g.button("sk6") 
        if persistent.sk6=="yes": 
        
            g.image("images/gallery/fong.png", "images/gallery/sk6.png") 

    tag menu 
    add "images/gallery/fong.png"
    grid 3 2:
        xfill True
        yfill True
        add g.make_button("sk1", "images/gallery/sk1_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3)
        add g.make_button("sk2", "images/gallery/sk2_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3) 
        add g.make_button("sk3", "images/gallery/sk3_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3) 
        add g.make_button("sk4", "images/gallery/sk4_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45) 
        add g.make_button("sk5", "images/gallery/sk5_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45) 
        add g.make_button("sk6", "images/gallery/sk6_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45)

    #textbutton "Музыкальная комната" action ShowMenu("music_mr") xalign 0.5 yalign 0.75
    textbutton "Следующая страница" action ShowMenu("gallery2") xalign 0.85 yalign 0.99
    #textbutton "Фоны" action ShowMenu("gallery3") xalign 0.5 yalign 0.9
    textbutton "Назад в меню" action ShowMenu("main_menu") xalign 0.5 yalign 0.99


screen gallery2:
    python:
        g.button("sk7") 
        if persistent.sk1=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk1.png") 
            
        g.button("sk8") 
        if persistent.sk2=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk2.png") 

        g.button("sk9") 
        if persistent.sk3=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk3.png")

        g.button("sk10") 
        if persistent.sk4=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk4.png") 

        g.button("sk11") 
        if persistent.sp5=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk5.png") 

        g.button("sk12") 
        if persistent.sp6=="yes": 
            g.image("images/gallery/fong.png", "images/gallery/sk6.png")

    tag menu 
    add "images/gallery/fong.png"
    grid 3 2:
        xfill True
        yfill True
        add g.make_button("sk7", "images/gallery/sk7_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3)
        add g.make_button("sk8", "images/gallery/sk8_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3) 
        add g.make_button("sk9", "images/gallery/sk9_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.3) 
        add g.make_button("sk10", "images/gallery/sk10_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45) 
        add g.make_button("sk11", "images/gallery/sk11_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45) 
        add g.make_button("sk12", "images/gallery/sk12_min.png", locked="images/gallery/fon_lock.png", xalign=0.5, yalign=0.45)
    
    textbutton "Предыдущая страница" action ShowMenu("gallery") xalign 0.1 yalign 0.99
    textbutton "Назад в меню" action ShowMenu("main_menu") xalign 0.5 yalign 0.99

#label gallery3:

