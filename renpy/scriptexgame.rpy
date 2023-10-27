init:
    define j = Character("집사",color="#000000")
    define s = Character("사장님",color="#ff0000")
    define t = Character("선생님",color="#00ff00")
    define a = Character("엑셀",color="#ffffff")
    define k = Character("토우마",color="#0000ff")
    define date_who = ""
    image bg room = "room.jpg"
    image touma = "teacher.png"
    image accel = "jipsa.png"
screen speech:
    $ dialogue = renpy.random.choice(dialogue_list)

    frame:
        text "[dialogue]"
        align (0.9, 0.9)
    
    timer 3.0 action Hide("speech")
screen manager:
    add 'room.jpg': 
        at transform:
            alpha 0
            ease 0.5 alpha 1.0

    imagebutton:
        if 15 >= age:
            idle "misaka_young.png"
            hover "misaka_young.png"
        elif age > 17:
            idle "misaka_teen.png"
            hover "misaka_teen.png"

        action [Hide("speech"), Show("speech",transition=dissolve)]

        align (1.0, 1.0)
        at transform:
            alpha 0
            ease 0.5 alpha 1.0

    frame:
        vbox:
            text "이름 : 차운재"
            text "나이 : [age]"
            text "키 : [height]cm 체중 : [weight]kg"
            text "현재 식단 : " + meal['name']
            spacing 10
        align (0.95,.1)

    frame:
        vbox:
            text "레벨 : [level]"
            text "칭호 : [title]"
            text "힘 : [phy]"
            text "지능 : [itl]"
            text "소지금 : [money]"
            text "스트레스 : [stress]"
            spacing 10
        align .1,.5

    frame:
        textbutton "데이트":
            action Show("date_menu")

        align .1,.8

    frame:
        grid 3 2:
            text "첫 번째 일정"
            text "두 번째 일정"
            text "세 번째 일정"

            textbutton first['name']:
                action Show("plan",to_do = "first")
            textbutton second['name']:
                action Show("plan",to_do = "second")
            textbutton third['name']:
                action Show("plan",to_do = "third")
            spacing 15
        align .5,.1

    frame:
        textbutton "일정 돌리기":
            action Return()
        align .5,.9
screen plan(to_do):
    frame:
        hbox:
            textbutton "휴식":
                action [SetVariable(to_do,rest), Hide("plan")]
            textbutton "알바":
                action [SetVariable(to_do,alba), Hide("plan")]
            textbutton "교육":
                action [SetVariable(to_do,edu), Hide("plan")]
        align (0.5, 0.5)
screen date_menu:
    modal True # 다른스크린버튼 안눌리게
    frame:
        vbox:
            textbutton "토우마를 부른다.":
                action [SetVariable("date_who","touma"),Hide("date_menu"),Return()]
            textbutton "엑셀을 부른다.":
                action [SetVariable("date_who","accel"),Hide("date_menu"),Return()]
            spacing 40
        align (0.5, 0.5)
screen today_background: 
    zorder -1
    add event_list[0]['background']:
        at transform:
            on show:
                alpha 0
                ease 0.5 alpha 1.0
            on hide:
                alpha 0.0
                ease 0.5 alpha 0.0
    add event_list[0]['character']:
        align .5,1.0
        at transform:
            on show:
                alpha 0
                ease 0.5 alpha 1.0
            on hide:
                alpha 0.0
                ease 0.5 alpha 0.0
screen calendar:
    frame:
        text "[year]년 [month]월 [day]일"
        align .1,.1
screen today:
    frame:
        text "오늘의 일정은" + event_list[0]['name'] + "입니다."
        align .5,.1
screen report:
    frame:
        vbox:
            text "힘 : [phy_temp] -> [phy]     "   +  str(phy-phy_temp)
            text "지능 : [itl_temp] -> [itl]     "  +   str(itl-itl_temp)
            text "소지금 : [money_temp] -> [money]      "   +  str(money-money_temp)
            text "스트레스 : [stress_temp] -> [stress]     " +    str(stress-stress_temp)
        align (0.5, 0.5)

label start:

    show misaka_young with dissolve

    m "안녕! 닌 차운재!"
    m "학원도시에서 최고의 초능력자가 되는게 꿈이야!"
    m "그러니까 앞으로 당신이 나를 도와서 내 꿈을 이룰 수 있도록 해줘!"
    m "라고 차운재는 애교를 부려본다!"


label schedule:
    show misaka_young with dissolve
    m "이번 달 식단은 어떻게 할까?"
    menu:
        "표준 식단으로 하자.":
            $ meal = standard
        "자라나는 아이는 많이 먹어야지!":
            $ meal = many
        "살좀 빼자...ㅠㅠ":
            $ meal = diet
    call screen manager
    if date_who == "":
        pass
    elif date_who == "touma":
        jump touma_label
    elif date_who == "accel":
        jump accel_label
    $ event_list = [first,second,third]
label touma_label:
    scene bg room
    show misaka_young at left with dissolve
    show touma at right with dissolve
    
    k "운지중..., 초등학생?"
    m "운지~~"
    hide misaka_young
    hide touma
    with dissolve
    jump schedule
    $ date_who = ""
label accel_label:
    scene bg room
    show misaka_young at left with dissolve
    show accel at right with dissolve
    
    a "너는..??"
    m "운지~~"
    hide misaka_young
    hide accel
    with dissolve
    jump schedule
    $ date_who = ""
label one:

    show screen calendar

    show misaka_young with dissolve
    m "첫 번째 일정을 진행할게!"
    hide misaka_young with dissolve
    call event_run
label two:
    show misaka_young with dissolve
    m "두 번째 일정을 진행할게!"
    hide misaka_young with dissolve
    call event_run
label three:
    show misaka_young with dissolve
    m "세 번째 일정을 진행할게!"
    hide misaka_young with dissolve
    call event_run
    jump final_day  

label event_run:
    show screen today_background
    
    $ count = 10
    while count > 0:
        show screen today
        $ renpy.call(event_list[0]['label'])
        $ phy_temp = phy
        $ itl_temp = itl
        $ money_temp = money
        $ stress_temp = stress

        
        if event_list[0] != edu:
            
            $ phy += event_list[0]['phy']
            $ itl += event_list[0]['itl']
            $ money = max(money + event_list[0]['money'],0)
            $ stress = max(stress + event_list[0]['stress'],0)
            show screen report
            m "오늘의 성과야!"
            hide screen report
        else:
            
            if money + event_list[0]['money'] < 0:
                show misaka_young with dissolve
                m "돈이 부족해서 교육을 받을 수 없어.ㅠㅠ"
                hide misaka_young with dissolve
            else:
                show screen report
                $ phy += event_list[0]['phy']
                $ itl += event_list[0]['itl']
                $ money = max(money + event_list[0]['money'],0)
                $ stress = max(stress + event_list[0]['stress'],0)
                show screen report
                m "오늘의 성과야!"
                hide screen report
        $ count -= 1
        $ day += 1  
        hide screen today
    hide screen today_background
    $ del event_list[0]
    
    return
label final_day:
    if day == 31:
        $ day = 30
    m "한 달 일정이 끝났어!"
    m "이번 달 성과야!"
    hide screen calendar
    $ weight += meal['change']
    $ day = 1
    $ month += 1
    if month == 13:
        $ month = 1
        $ year += 1
        $ age += 1
        $ height += 3
    jump schedule
    return

label rest_label:
    j "오늘은 휴식입니다."
    j "운재군, 편히 쉬세요~"
    return
label alba_label:
    s "자, 오늘도 열심히 일하자고."
    s "농땡이 피우면 죽는다."
    return
label edu_label:
    t "오늘 수업도 힘내서 해요,"
    t "못 따라오면 콜럼버스이 달걀이에요."
    return