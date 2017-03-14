
label splashscreen:
    scene black with dissolve
    pause 1
    show logo_std with dissolve
    pause 6 
    return

label start:
    #stop music fadeout 1
    #$ renpy.pause(2.0, hard = True)
    #play music "music/" fadeout 1 loop
    scene room with dissolve
    $ persistent.sk6 = "yes"
    #play sound ""
    ivan "Первое сентября, время 7:30 утра. Я проснулся от того, что прозвонил будильник. Встал, умылся – сделал обычные утренние дела, собрался и вышел на улицу. Сегодня начинается первый учебный день в колледже в который я поступил. Поскольку это первый день, то опаздывать нельзя."
    $ persistent.sk1 = "yes"
    scene bus with dissolve
    $ persistent.sk4 = "yes"
    #jump credits
    ivan "Я дошел до остановки, дождался маршрутки, к счастью она была пустой. Сев в неё направился на место назначения, хорошо, что ехать не далеко. Маршрутка остановилась практически у дверей колледжа, около которого уже собралась толпа студентов-первокурсников."
    scene college with dissolve
    ivan "Подходя к дверям, я услышал, как меня кто-то окрикнул сзади, обернувшись я увидел догоняющую меня девушку – это была Анна. Анна - моя подруга еще со школы, она была единственной девушкой, которая со мной общалась."
    #Первый диалог
    #$ qm_togle = True
    show anna at Position(xalign = 0.1)
    anna "Привет Ваня! Давно не виделись, как ты? Вижу ты тоже сюда поступил."
    hide anna
    #show ivan at Position(xalign = 0.8) with move
    show ivan at Position(xalign = 0.8)
    ivan "Привет, не так уж давно. Как видишь, нормально все со мной. С тобой тоже смотрю все в полном порядке."
    hide ivan
    show anna at Position(xalign = 0.1)
    anna "Какой-то ты хмурый и мрачный, обычно ты не такой. Что-то случилось?"
    hide anna
    show ivan at Position(xalign = 0.8)
    ivan "Кха..Конечно случилось – вставать рано утром и тащиться куда-то после трехмесячного отдыха, что может быть хуже."
    hide ivan
    show anna at Position(xalign = 0.1)
    anna "Кстати, а на кого ты учиться то поступил?"
    hide anna
    show ivan at Position(xalign = 0.8)
    ivan "На программиста. Выбор был не особо богатый. Либо на программиста, либо на фотографа."
    ivan "Уж компьютер я знаю получше фотоаппарата."
    hide ivan
    show anna at Position(xalign = 0.1)
    anna "Ха.. это похоже на совпадение, но я тоже на программиста поступила. Знаешь, я так рада, если честно. Прямо как в школе."
    hide anna
    show ivan at Position(xalign = 0.8)
    ivan "Я тоже этому рад."
    hide ivan
    "Как оказалось, она поступила в этот же колледж и оказалась со мной в одной группе. Не разлей вода, как и в школьные годы. Честно я не ожидал что встречу её здесь."
    scene hall with dissolve
    "После разговора нас всех дружно собрали в актовом зале, где рассказывали о том, как нам всем будет здесь хорошо учиться и что эти 4 курса пройдут замечательно и все в этом духе."
    scene college with dissolve 
    $ persistent.sk7 = "yes"
    "Затем началась линейка, ради которой нас вывели на улицу, впрочем, погода стояла хорошая. Анна нашла меня и встала рядом со мной. Некоторые из нас начали знакомиться  друг с другом, спрашивать кто как провел лето, пока шло это скучное и унылое действо, называемое «линейкой»."
    show anna at Position(xalign = 0.2)
    anna "Кстати, как прошло твоё лето, чем был занят?"
    hide anna
    show ivan at Position(xalign = 0.7)
    ivan "Ты сама прекрасно знаешь ответ на этот вопрос – просидел практически все эти три месяца дома."
    ivan "А ты как провела лето?"
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Да так, побывалаза горомом, в аквапарк съездила и вообще весело провела время. А ты небось дома сидел? "
    hide anna
    show ivan at Position(xalign = 0.7)
    ivan "Прости, но мне виднее, чем заниматься."
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Что же ты вредный то такой…"
    hide anna
    show ivan at Position(xalign = 0.7)
    ivan "Какой есть, ты же меня знаешь."
    #hide ivan 
    python:
    #    renpy.show("ivan",at_position=("xalign = 0.7")) 
    #    renpy.show("Какой есть, ты же меня знаешь.")
        renpy.hide("ivan")
        #renpy.show("cabinet_108")

    scene cabinet_108 with dissolve
    $ persistent.sk5 = "yes"
    "Когда все кончилось нашу группу, как и все остальные повели знакомить с кураторами."
    "Нас отвели в большую и просторную аудиторию, где начался час куратора, на котором нам рассказывали о том, что будет ждать нас на ближайший учебный год."
    "Но осматревшись на соседей по парте, я понял что особо сильно никто не слушает."
    "Когда все кончилось нашу группу, как и все остальные повели знакомить с кураторами."
    "В конце сего мероприятия куратор предложил нам выбрать старосту."
    "Выбор пал на с виду миловидную миниатюрную девушку, которая сама вызвалась стать старостой и внешний вид которой соответствовал этой ответственной должности."
    show alice at Position(xalign  = 0.4)
    alice "Извините, раз никто не хочет, то давайте я стану старостой. У меня в школе не было пробем с помощью учителю, так, что и с этим я справлюсь без проблем. А всем, кто меня ещё не знает, меня зовут Алиса. Приятно познакомиться."
    hide alice
    "Так же старосте нужен был заместитель. Была так же выбрана девушка – практически полная противоположность Алисы: высокая, стройная и красивая, которая представилась как Мария."
    show maria at Position(xalign = 0.5)
    maria "Меня зовут Маша. Простите, но может я бы смогла помочь Алисе, если конечно никто не будет против."
    hide maria
    "Куратор утвердил кандидатуры и сказал всем собираться и идти на первую пару"
    #"Она сразу всем понравилась, но не только из-за внешнего вида, всем своим видом она выражала доброту, и оказалась милой и заботливой девушкой, готовой протянуть руку помощи любому."
    "Прозвенел звонок, и вся группа направилась на первую пару в другую аудиторию, которая находилась на втором этаже, надо сказать в коридорах было огромное столпотворение людей, из за большого количества  поступивших."
    "Войдя в аудиторию, каждый начал садиться кто куда, я же занял место на последней парте среднего ряда. Анна села на соседний ряд напротив меня, рядом с какой-то девушкой."
    "Рядом со мной сел тихо сел парень: у него были длинный волосы, собранные в хвост, из отличительных черт на нём была футболка группы которая нравилась и мне тоже."
    show dmitriy at Position(xalign = 0.1)
    dmitriy "Давай знакомиться, меня зовут Дима, а тебя как?"
    python:
        renpy.hide("dmitriy")
    show ivan at Position(xalign = 0.7)
    ivan "Я Ваня, тоже рад знакомству. Судя по футболке у тебя хороший музыкальный вкус."
    hide ivan
    show dmitriy at Position(xalign = 0.1)
    dmitriy "А то, очень крутые ребята и хорошо играют. Я, кстати, сам немного музыкант, играю на гитаре."
    hide dmitriy
    show ivan at Position(xalign = 0.7)
    ivan "Я тоже раньше, чем-то подобным занимался, по крайней мере пытался научиться петь, но потом от чего-то забил на это."
    hide ivan
    "Преподаватель опаздывал и пока все дружно его ждали, у меня с этим парнем завязался разговор, из которого оказалось что его зовут Дмитрий Сычёв."
    "Мы разговаривали до тех пор, пока не пришел преподаватель, который преподавал нам математику, с которой я не в ладах еще со школы. Им оказалась миловидная с виду девушка лет 30."
    show alex at Position(xalign = 0.5)
    alex "Здравствуйте студенты, меня зовут Александра Ивановна и с сегодняшнего дня я буду преподавать у вас математику, для начала давайте проведем перекличку."
    "Алексагдра Ивановна открыла журнал и начала проводить перекличку, попутно стараясь запомнить кто есть, кто. Когда перекличка закончилась, она продолжила занятие."
    show alex at Position(xalign = 0.5)
    alex "Для того, чтобы начать работать серьезно, нужно будет вспомнить некоторые аспекты предмета из вашего школьного курса, ну или если кто-то из вас вообще ничего не знает, то узнать. Итак, начнем…"
    hide alex
    "Первая пара шла полным ходом, преподаватель объяснял нам, что-то со школьного курса, но мимо моих ушей это пролетало, так как я общался с моим соседом по парте."
    "Мы так разговорились с Димой и видимо из-за шума с нашей стороны, либо просто так, Александра Ивановна решила задать мне вопрос."    
    show alex at Position(xalign = 0.5)
    alex "Ерохин, я вижу ты все знаешь, поэтому реши-ка мне задачу которая написана на доске."
    menu:
      "Попытаться ответить":
        $ test = +1
        jump navigate
      "Промолчать или сказать не знаю":   
        $ test2 = +2
        jump zhopa
      "Смолоть какую-нибудь чушь":
        $ test3 = +3
        jump zhopa

label navigate: #метка для навигации
    hide alex 
    "Я попытался ответить, но попытка была тщетна, так как с математикой, как я ранее уже заметил – я был не в ладах, но за попытку я получил плюсик и замечание о разговоре не паре."
    "Наконец пара закончилась и по времени наступил обеденный перерыв."
    menu:
      "Попытаться пробиться в столовую":
        $ test2 = +2
        jump oneroot
      "Пойти в магазин":
        $ test3 = +3
        jump secondroot

label zhopa: 
    hide alex 
    "Я попытался ответить, но попытка была тщетна, так как с математикой, как я ранее уже заметил – я был не в ладах. Я получил строгое замечание"
    "Наконец пара закончилась и по времени наступил обеденный перерыв."
    menu:
      "Попытаться пробиться в столовую":
        $ test2 = +2
        jump oneroot
      "Пойти в магазин":
        $ test3 = +3
        jump secondroot
    
label oneroot: #рут не попав в столовую 
    #scene 302 with dissolve
    $ persistent.sk8 = "yes"
    $ persistent.sk9 = "yes" 
    scene stol with dissolve
    "Прорыв в столовую не удался и вместо обеда, нам пришлось вернуться обратно в аудиторию, так как времени сходить в магазин уже не было, и мы остались голодными."
    scene 302 with dissolve
    "Вместо обеда мы с Димой разговаривали  о разных вещах."
    "Прозвенел звонок и было такое чувство что кого-то не хватает... И тут, уже спустя 10 минут после звонка, заходят староста с заместителем." 
    show alice at Position(xalign = 0.2)
    show maria at Position(xalign = 0.5)
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич. На этой паре все расселись примерно так же, как и на предыдущей."
    show andrey at Position(xalign = 0.8)
    andrey "Ну что девушки вы до Теплотеха кушать бегали, сейчас то ещё хорошо, а зимой что делать будете?"
    "Алиса вроде и открыла рот чтобы ответить, но Маша остановила её и они тихо прошли на свои места."
    hide alice
    hide maria
    andrey "Итак о чём это я... Меня зовут Андрей Анатольевич и ближашие 4 года я буду преподовать у вас информатику и ещё несколько предметов позже. Давайте проведём перекличку."
    "Преподаватель открыл журнал и начал проводить перекличку, попутно стараясь запомнить кто есть на паре, и судя по его взгляду, когда он озвучивал нашу опоздавшую кампанию мы были в его маленьком черном списке. Когда перекличка закончилась, он продолжил занятие."
    hide andrey
    $ persistent.sk3 = "yes"
    $ persistent.sk10 = "yes"
    jump credits

label secondroot: #рут_перед столовой  
    scene 3_floor with dissolve
    #show ivan at Position(xalign = 0.2)
    scene stol with dissolve
    show ivan at Position(xalign = 0.3)
    ivan "Что-то в столовой слишком много народу, может до магазина дойдем?"
    hide ivan
    show dmitriy at Position(xalign = 0.9)
    dmitriy "Я тоже так думаю, пока мы протиснемся в такой толпе к еде, уже перерыв кончится звонок, так что пойдем."
    hide ivan
    show ivan at Position(xalign = 0.2)
    ivan "Аня пойдёшь с нами до магазина?"
    hide ivan
    hide dmitriy
    show anna at Position(xalign = 0.5)
    anna "Извини, но я пойду со своей подругой по парте, надеюсь ты не обидишься."
    hide anna
    show ivan at Position(xalign = 0.2)
    ivan "Нет проблем."
    hide ivan
    scene magaz with dissolve
    "Мы с Димой направились в ближайший магазин, а Алиса с Марией решили направиться в забитую столовую, у входа в которую видимо начал проявляться истинный характер Алисы."
    "Дойдя до магазина, мы решили заточить пару булок с кофейком. Купив все необходимое, мы уселись на скамейку рядом с кофейным автоматом."
    "И тут мы увидели знакомые лица, которые видимо так и не смогли попасть в столовую – это были Алиса и Мария."
    " Они в спешке прошли мимо нас за покупками, потому, что время обеда поджимало, но через несколько минут они вернулись к нам."
    show maria at Position(xalign = 0.7)
    maria "Привет, можно нам тут присесть?"
    hide maria
    show ivan at Position(xalign = 0.2)
    ivan "Да, конечно."
    hide ivan
    show maria at Position(xalign = 0.7)
    maria "Спасибо."
    hide maria
    "Нам пришлось подвинуться, чтобы девочки сели рядом с нами."
    show maria at Position(xalign = 0.2)
    maria "Меня Маша зовут, а это Алиса."
    hide maria
    show ivan at Position(xalign = 0.7)
    ivan "Да мы уже знаем, вы же представлялись, зато вот мы нет. Меня зовут Ваня."
    hide ivan
    show dmitriy at Position(xalign = 0.1)
    dmitriy "А меня Дима, приятно познакомиться. Алиса, а почему ты молчишь? Стесняешься, что лм?"
    show alice at Position(xalign = 0.8)
    alice "Ничего я не стесняюсь! Может просто не хочу разговаривать… Из-за этой столовой мы потратили кучу времени в пустую… И да, рада знакомству."
    hide alice
    show maria at Position(xalign = 0.4)
    maria "Я не думаю, что в этом есть, что-то страшное, просто надо по-быстрому закончить с перекусом и тогда мы успеем, и все будет хорошо, так что не надо так волноваться Алиса."
    hide maria
    show ivan at Position(xalign = 0.7)
    ivan "Думаю, что время уже поджимает и пора выдвигаться обратно."
    hide ivan
    show dmitriy at Position(xalign = 0.1)
    dmitriy "Я тоже так думаю, не хочется как-то в первый день получать нагоняй от преподавателя."
    hide dmitriy
    $ persistent.sk11 = "yes"
    "Перекинувшись парой фраз, мы в спешке собрались обратно в колледж на следующую пару."
    menu:
      "Идти быстро":
        scene 302 with dissolve
        "Мы решили не испытывать судьбу и поспешили на пару. Зайдя в кабинет, мы расселись по местам, и я случайно встретился с Анной глазами."
        jump end
      "Идти медленноее":
        "Выйдя из магазина мы решили пойти по медленнее, хотя опоздать на пару в первый день было слишком, но мы решили пообщаться по дольше по пути в колледж."
        jump thirdroot

label thirdroot: #окончание рута
    scene magaz with dissolve 
    show ivan at Position(xalign = 0.2)
    ivan "Слушайте, а может пойдем по медленнее? Чего спешить, может лучше по дольше поболтаем? Чем ты увлекаешься или обычно занимаешься Маша?"
    hide ivan
    show maria at Position(xalign = 0.8)
    maria "Да ничем особенным, люблю читать книжки из жанра фэнтези и фантастики, слушать музыку и помогать людям, если это конечно можно считать за занятие."
    hide maria
    show dmitriy at Position(xalign = 0.7)
    dmitriy "А ты Алиса чем занимаешься? Ну кроме, того чтобы всем грубо отвечать."
    hide dmitriy
    $ persistent.sk12 = "yes"
    show alice at Position(xalign = 0.1)
    alice "Да чего ты ко мне привязался то?! Учиться я люблю и ничего больше, а делаю это для того, чтобы не быть такой глупой как ты, дурак!"
    hide alice
    show dmitriy at Position(xalign = 0.7)
    dmitriy "Эй, ну чего ты на меня так нападаешь, я же просто пошутил, но прости, если я обидел тебя."
    hide dmitriy
    show alice at Position(xalign = 0.2)
    alice "Ладно забудь, ты тоже меня извини, вспылила. В общем я тоже люблю читать книжки, только те что связаны с учебой, слушать музыку и иногда гулять, только вот из-за учебы не всегда получается."
    alice "А вы чем занимаетесь?"
    hide alice
    show ivan at Position(xalign = 0.7)
    ivan "Я особо ничем, просто обычный парень, который живет обычной скучной жизнью. Ну, а по сути просиживать свою жизнь за компом в играх и посиделках в интернете, ну и музыку слушать."
    hide ivan
    show dmitriy at Position(xalign = 0.2)
    dmitriy "Я практически также, только еще увлекаюсь музыкой – немного играю на гитаре, а еще подрабатываю кое-где."
    hide dmitriy
    show ivan at Position(xalign = 0.7)
    ivan "Об этом ты мне не говорил."
    hide ivan
    show dmitriy at Position(xalign = 0.2)
    dmitriy "А ты и не спрашивал."
    hide dmitriy
    show ivan at Position(xalign = 0.8)
    ivan "Как будто девчонки спрашивали, ты сам сказал. Решил выпендриться?" 
    "Девушки хихикнули"
    show dmitriy at Position(xalign = 0.2)
    dmitriy "Ну я… Это… В общем забудь, нужно быстрее идти обратно, а то итак уже опаздываем."
    scene dressroom with dissolve
    scene 302 with dissolve
    "Зайдя в кабинет, на нас с ходу накинулись с замечаниями, но ими дело не обошлось и нам пришлось писать объяснительную, затем, когда мы рассаживались по местам я заметил на себе неодобрительный взгляд Анны."
    "Видимо она злилась на меня из-за того, что я опоздал. Просто она слишком строгая и правильная. Затем пара пошла своим чередом."
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич. На этой паре все расселись примерно так же, как и на предыдущей."
    show andrey at Position(xalign = 0.5)
    andrey "Меня зовут Андрей Анатольевич и ближашие 4 года я буду преподовать у вас информатику и ещё несколько предметов позже. Давайте проведём перекличку."
    "Преподаватель открыл журнал и начал проводить перекличку, попутно стараясь запомнить кто есть на паре, и судя по его взгляду, когда он озвучивал нашу опоздавшую кампанию мы были в его маленьком черном списке. Когда перекличка закончилась, он продолжил занятие."
    hide andrey
    $ persistent.sk2 = "yes"
    $ persistent.sk3 = "yes"
    jump credits

label end: #общая концовка
    scene 302 with dissolve
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич. На этой паре все расселись примерно так же, как и на предыдущей."
    show andrey at Position(xalign = 0.5)
    andrey "Меня зовут Андрей Анатольевич и ближашие 4 года я буду преподовать у вас информатику и ещё несколько предметов позже. Давайте проведём перекличку."
    "Преподаватель открыл журнал и начал проводить перекличку, попутно стараясь запомнить кто есть на паре, и судя по его взгляду, когда он озвучивал нашу опоздавшую кампанию мы были в его маленьком черном списке. Когда перекличка закончилась, он продолжил занятие."
    $ persistent.sk2 = "yes"
    $ persistent.sk3 = "yes"
    jump credits

return

init:
    transform txt_up:
      yalign 1.5
      linear 15.0 yalign-1.5  
label credits:
    scene black with dissolve
    show text "Идея - Regis(Сергей Заварницын) и Hollow48(Николай Денисюк) {p} Код - Regis {p} Арты - Owl {p} Программная среда(ака движок - RenPy) {p} За тестирование спасибо: Almeanay, Belka, Frank {p} Всем спасибо! {p} Все персонажи являются вымышленными и любое совпадение с реально живущим или когда-либо жившими являются оошибочными. {p} The end {p}" at txt_up
    pause 15
    return