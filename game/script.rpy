
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
    $ persistent.sk2 = "yes"
    $ persistent.sk3 = "yes"
    scene room with dissolve
    $ persistent.sk6 = "yes"
    #play sound ""
    ivan "Первое сентября, время 7:30 утра. Я проснулся от того, что прозвонил будильник. Встал, умылся – сделал обычные утренние дела, собрался и вышел на улицу. Сегодня начинается первый учебный день в колледже в который я поступил. Поскольку это первый день, то опаздывать нельзя."
    $ persistent.sk1 = "yes"
    scene bus with pushleft
    $ persistent.sk4 = "yes"
    ivan "Я дошел до остановки, дождался маршрутки, к счастью она была пустой. Сев в неё направился на место назначения, хорошо, что ехать не далеко. Маршрутка остановилась практически у дверей колледжа, около которого уже собралась толпа студентов-первокурсников."
    scene college with dissolve
    ivan "Подходя к дверям, я услышал, как меня кто-то окрикнул сзади, обернувшись я увидел догоняющую меня девушку – это была Анна. Анна - моя подруга еще со школы, она была единственной девушкой, которая со мной общалась."
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
    anna "Ха...это похоже на совпадение, но я тоже на программиста поступила. Знаешь, я так рада, если честно. Прямо как в школе."
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
    anna "Да так, побывала за городом, в аквапарк съездила и вообще весело провела время. А ты небось дома сидел? "
    hide anna
    show ivan at Position(xalign = 0.7)
    ivan "Прости, но мне виднее, чем заниматься."
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Что же ты вредный то такой…"
    hide anna
    show ivan at Position(xalign = 0.7)
    ivan "Какой есть, ты же меня знаешь."
    python:
    #   renpy.show("ivan",at_position=("xalign = 0.7")) 
    #   renpy.show("Какой есть, ты же меня знаешь.")
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
        jump navigate2
      "Смолоть какую-нибудь чушь":
        $ test3 = +3
        jump navigate2
    return

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
    return

label navigate2: 
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
    return
    
label oneroot: #рут не попав в столовую==закончен
    $ persistent.sk8 = "yes"
    $ persistent.sk9 = "yes" 
    scene stol with dissolve
    "Прорыв в столовую не удался и вместо обеда, нам пришлось вернуться обратно в аудиторию, так как времени сходить в магазин уже не было, и мы остались голодными."
    scene 302 with dissolve
    "Вместо обеда мы с Димой разговаривали  о разных вещах."
    "Прозвенел звонок и было такое чувство что кого-то не хватает..."
    "И тут, уже спустя 10 минут после звонка, заходят староста с заместителем." 
    show alice at Position(xalign = 0.2)
    show maria at Position(xalign = 0.5)
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич."
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
    return

label secondroot: #рут_в магазине
    scene 3_floor with dissolve
    #show ivan at Position(xalign = 0.2)
    scene stol with dissolve
    show ivan at Position(xalign = 0.3)
    ivan "Что-то в столовой слишком много народу, может до магазина дойдем?"
    hide ivan
    show dmitriy at Position(xalign = 0.9)
    dmitriy "Я тоже так думаю, пока мы протиснемся в такой толпе к еде, уже перерыв кончится, так что пойдем."
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
    "Дойдя до магазина, мы решили заточить пару булок с кофе. Купив все необходимое, мы уселись на скамейку рядом с кофейным автоматом."
    "И тут мы увидели знакомые лица, которые видимо так и не смогли попасть в столовую – это были Алиса и Мария."
    "Они в спешке прошли мимо нас за покупками, потому, что время обеда поджимало, но через несколько минут они вернулись к нам."
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
        "Выйдя из магазина мы решили пойти по медленнее, хотя опоздать на пару в первый день было слишком, но мы решили пообщаться подольше по пути в колледж."
        jump after_market
    return

label after_market: #после магазина продолжение рута 2
    scene magaz with dissolve 
    show ivan at Position(xalign = 0.2)
    ivan "Чем ты обычно увлекаешься Маша?"
    hide ivan
    show maria at Position(xalign = 0.8)
    maria "Да ничем особенным, люблю читать книжки из жанра фэнтези и фантастики, слушать музыку и помогать людям, если это конечно можно считать за занятие."
    hide maria
    show dmitriy at Position(xalign = 0.7)
    dmitriy "А ты Алиса чем занимаешься? Ну кроме, того что всем грубо отвечать."
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
    ivan "Я особо ничем, обычный парень, который живет обычной скучной жизнью. Ну, а по сути просиживать свою жизнь за компом в играх и посиделках в интернете, ну и музыку слушать."
    hide ivan
    show dmitriy at Position(xalign = 0.2)
    dmitriy "Ну...я музыкой увлекаюсь – немного играю на гитаре, а еще подрабатываю кое-где."
    hide dmitriy
    show ivan at Position(xalign = 0.7)
    ivan "А про подработку ты мне и не говорил."
    hide ivan
    show dmitriy at Position(xalign = 0.2)
    dmitriy "А ты и не спрашивал."
    hide dmitriy
    show ivan at Position(xalign = 0.8)
    ivan "Как будто девчонки спрашивали, ты сам сказал. Решил выпендриться?" 
    "Девушки хихикнули."
    show dmitriy at Position(xalign = 0.2)
    dmitriy "Ну я… Это… В общем забудь, нужно быстрее идти обратно, а то итак уже опаздываем."
    scene dressroom with dissolve
    scene 302 with dissolve
    "Зайдя в кабинет, на нас с ходу накинулись с замечаниями, но ими дело не обошлось и нам пришлось писать объяснительную, затем, когда мы рассаживались по местам я заметил на себе неодобрительный взгляд Анны."
    "Видимо она злилась на меня из-за того, что я опоздал. Просто она слишком строгая и правильная. Затем пара пошла своим чередом."
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич."
    show andrey at Position(xalign = 0.5)
    andrey "Меня зовут Андрей Анатольевич и ближашие 4 года я буду преподовать у вас информатику и ещё несколько предметов позже. Давайте проведём перекличку."
    "Преподаватель открыл журнал и начал проводить перекличку, попутно стараясь запомнить кто есть на паре, и судя по его взгляду, когда он озвучивал нашу опоздавшую кампанию мы были в его маленьком черном списке. Когда перекличка закончилась, он продолжил занятие."
    hide andrey
    scene 3_floor with pushleft
    "После окончания пары всех первокурсников собрали в актовом зале, так как там намечался какой-то концерт или мероприятие в честь поступления. Все желающие могли принять в нем участие или просто посмотреть. Перед началом концерта мы все собрались на перемене и пока народ медленно заходил в зал, мы решили подождать пока толкучка пройдет."
    show ivan at Position(xalign = 0.5)
    ivan "Что-то мне особо идти туда не хочется, слишком шумно и слишком много народу, не люблю я этого."
    hide ivan 
    show dmitriy at Position(xalign = 0.3)
    dmitriy "Да ладно тебе, только первый день, а ты уже хочешь слинять по раньше, пошли посидим, посмотреть, не думаю, что там будет прямо так уж скучно."
    hide dmitriy
    show anna at Position(xalign = 0.6)
    anna "Тем более после концерта, мы могли бы пойти домой вместе."
    hide anna
    jump concert
    return

label end: #общая концовка
    scene 302 with dissolve
    "Началась пара информатики, и преподавал её солидный мужчина, звали его Андрей Анатольевич. На этой паре все расселись примерно так же, как и на предыдущей."
    show andrey at Position(xalign = 0.5)
    andrey "Меня зовут Андрей Анатольевич и ближашие 4 года я буду преподовать у вас информатику и ещё несколько предметов позже. Давайте проведём перекличку."
    "Преподаватель открыл журнал и начал проводить перекличку, попутно стараясь запомнить кто есть на паре, и судя по его взгляду, когда он озвучивал нашу опоздавшую кампанию мы были в его маленьком черном списке. Когда перекличка закончилась, он продолжил занятие."
    hide andrey
    scene 3_floor with pushleft
    "После окончания пары всех первокурсников собрали в актовом зале, так как там намечался какой-то концерт или мероприятие в честь поступления. Все желающие могли принять в нем участие или просто посмотреть. Перед началом концерта мы все собрались на перемене и пока народ медленно заходил в зал, мы решили подождать пока толкучка пройдет."
    show ivan at Position(xalign = 0.5)
    ivan "Что-то мне особо идти туда не хочется, слишком шумно и слишком много народу, не люблю я этого."
    hide ivan 
    show dmitriy at Position(xalign = 0.3)
    dmitriy "Да ладно тебе, только первый день, а ты уже хочешь слинять по раньше, пошли посидим, посмотреть, не думаю, что там будет прямо так уж скучно."
    hide dmitriy
    show anna at Position(xalign = 0.6)
    anna "Тем более после концерта, мы могли бы пойти домой вместе."
    hide anna
    show dmitriy at Position(xalign = 0.4)
    dmitriy "Ну, так что? Остаешься?"
    menu:
      "Остаться на концерт":
        jump concert
      "Уйти с концерта":
        jump concert2

    return

label concert: # концерт и 1 концовка (хорошая)
    show ivan at Position(xalign = 0.5)
    ivan "Ладно, уговорили, пойдем."
    hide ivan
    scene hall with pushleft 
    "Мы пришли в актовый зал, заняли места. Начался концерт, по началу он шел скучно, но в целом я не пожалел, что пришел на него. Было много смешных моментов. Кто-то пел, кто-то показывал сценки, а кто-то просто устраивал какой-то непонятный цирк. "
    scene dressroom2 with dissolve
    "Когда все закончилось мы пошли в холл, обсуждая по пути то, что творилось в актовом зале. Одевшись мы собрались у дверей."
    show dmitriy at Position(xalign = 0.3)
    dmitriy "Ну, я думаю неплохо для первого дня я считаю, было вполне себе хорошо, кроме момента, когда мы опоздали на пару…"
    hide dmitriy
    show ivan at Position(xalign = 0.6)
    ivan "Да ладно тебе, нормально все было и в тот момент."
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Сейчас бы в первый день на первую пару преподавателя опаздывать… Смертный приговор себе подписываете…"
    hide anna
    scene college with pushleft
    "Девушки дружно хихикнули. Мы постояли так еще немного, а потом попрощавшись, разошлись в разные стороны по домам. Я пошел вместе с Аней, потому что нам было с ней по пути, так как мы жили с ней практически рядом. Маше и Алисе было не по пути, и поэтому каждый пошел своей дорогой, одному Диме нужно было на подработку."
    "Итак, мы с Аней двигались домой, говоря о том, что нам понравилось или не понравилось в колледже за сегодняшний день."
    show ivan at Position(xalign = 0.6)
    ivan "Ну и как тебе сегодня было тут?"
    hide ivan
    show anna at Position(xalign = 0.3)
    anna "Неплохо, не считая того, что я не смогла поесть из-за того, что столовая была забита…"
    hide anna
    show ivan at Position(xalign = 0.6)
    ivan "Нужно было идти с нами и таких бы проблем не было."
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Пойти с вами и отхватить люлей от преподавателя? Нет спасибо уж."
    hide anna
    show ivan at Position(xalign = 0.6)
    ivan "Ой да ладно тебе, с кем не бывает…"
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Со мной."
    hide anna
    show ivan at Position(xalign = 0.5)
    ivan "Как скажешь, зануда… Как тебе преподаватели?"
    hide ivan
    show anna at Position(xalign = 0.2)
    anna "Мне понравились, вроде как добрые и понимающие, а тебе как?"
    hide anna
    show ivan at Position(xalign = 0.6)
    ivan "Ну мне тоже так показалось, правда похоже я уже одной ногой в маленьком черном списке опоздунов."
    hide ivan
    show anna at Position(xalign = 0.3)
    anna "Не думаю, что это что-то страшное, тем более это только первый день из нескольких лет, так что все еще впереди, и я не про углубление в черный список. В следующий раз просто рассчитывайте время."
    hide anna
    show ivan at Position(xalign = 0.6)
    ivan "Окей, босс."
    "За разговором время пролетело незаметно и вот мы уже оказались около ее дома. Попрощавшись с Аней, я направился к себе домой. Так и закончился мой первый день. Один день из жизни студента."
    jump credits 

label concert2: # концерт и 2 концовка (плохая)
    show ivan at Position(xalign = 0.5)
    ivan "Нет, не сегодня, не хочу. Не для меня это."
    hide ivan
    show dmitriy at Position(xalign = 0.3)
    dmitriy "Ну как хочешь, дело твое."
    hide dmitriy
    show anna at Position(xalign = 0.2)
    anna "А ведь мы могли бы пойти домой вместе, ну да ладно, ты всегда таким был. Не любил ничего такого."
    hide anna
    show ivan at Position(xalign = 0.5)
    ivan "Аня, может пойдешь со мной? Ну этот концерт, еще не один раз такой будет."
    hide ivan
    show anna at Position(xalign - 0.2)
    anna "Мне не очень хочется уходить в первый же день, а потом получать выговор, так что я пасс."
    hide anna
    show ivan at Position(xalign = 0.6)
    ivan "Ладно, хорошо, тогда до завтра."
    "Мы все попрощались. Я конечно понимал, что не хорошо так поступать, да и перед друзьями было немного стыдно, но я действительно не любил всех этих шумных собраний. Я вышел в холл, оделся и по быстрее направился домой."
    "Придя домой я подумал о том, что все-таки нужно было остаться, но было уже поздно думать о таком. Я мысленно пролистал в голове то, что произошло за сегодня и сел за компьютер. Так закончился мой первый день. Один день из жизни студента."
    jump credits


return

init:
    transform txt_up:
      yalign 1.5
      linear 15.0 yalign-1.5  
label credits:
    scene black with dissolve
    show text "Идея - Regis (Сергей Заварницын) и Hollow48 (Николай Денисюк) {p} Код - Regis {p} Арты - Owl {p} Программная среда разработки - RenPy {p} За тестирование спасибо: Almeanay, Belka, Franku, Owl {p} Всем спасибо! {p} Все персонажи являются вымышленными и любое совпадение с реально живущим или когда-либо жившими являются оошибочными. {p} The end {p}" at txt_up
    pause 15
    return