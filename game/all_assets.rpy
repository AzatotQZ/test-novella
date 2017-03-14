#init -2 :
    #$ qm_togle = False
init:
    # Описание персонажей
    define maria = Character("Мария", color="#FFFFE0", who_font = "fonts/georgia.ttf") 
    define alice = Character("Алиса", color="#FF4500")
    define anna = Character("Анна", color="#4169E1")
    define ivan = Character("Иван", color="#8B0000")
    define dmitriy = Character("Дмитрий", color="#E6E6FA")
    define alex = Character("Александра Ивановна", color="#F70D1A")
    define andrey = Character("Андрей Анатольевич", color="#A9A9A9")
    # Описание sideimage - для аватаров рядом с текстом
    #image side maria norm = "images/side_image/head_t.png"
    # Описание фонов
    image college = "images/bg/bg_college.png"
    image room = "images/bg/bg_room.png"
    image bus = "images/bg/bg_bus.png"
    image black = "images/bg/bg_black.png"
    image hall = "images/bg/bg_act_zal.png"
    image cabinet_108 = "images/bg/bg_cab_108.png"
    image 302 = "images/bg/bg_302.png"
    image dressroom = "images/bg/bg_dressroom.png"
    image stairs = "images/bg/bg_stairs.png"
    image 3_floor = "images/bg/bg_3_floor.png"
    image magaz = "images/bg/bg_magaz.png"
    image stol = "images/bg/bg_stol.png"
    # Описание спрайтов персонажей
    image ivan = "images/sprites/ivan.png"
    image anna = "images/sprites/anna.png"
    image alice = "images/sprites/alice.png"
    image maria = "images/sprites/maria.png"
    image alex = "images/sprites/alex.png"
    image andrey = "images/sprites/andrey.png"
    image logo_std = "images/logo/rh_logo.png" #заставка