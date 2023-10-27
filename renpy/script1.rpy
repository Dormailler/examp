init:
    image eileen happy = "images/char/ara.png" #ara
    image eileen = "images/char/siu.png" #siu

    image bg river = "images/bg/river.jpg"
    image bg room = "images/bg/room.jpg"

    define 아라 = Character("아라" , color = "#ff3352")
    define 시우 = Character("시우" , color = "#33d4ff")
    define pov = Character("[povname]")
    define p = Character("Player", image="img1.png")
    image side player happy = "images/char/ara.png"
    image side player concerned = "images/char/siu.png"
    $mars_flag = False
    $on_mars = False

screen exam:
    vbox:
        text "[mars_flag]"
        text "[on_mars]"
        align (0.5, 0.5)
    vbox:
        textbutton "A":
            action [ SensitiveIf(SetVariable("mars_flag", True)), SetVariable("on_mars", True) ]
        textbutton "B":
            action [ SensitiveIf(SetVariable("mars_flag", True)), SetVariable("on_mars", True) ]
# 툴팁
screen tooltip_example:
    vbox:
        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]"
#팝업툴팁
screen tooltip_example2:
    frame:

        padding (20, 20)
        align (.5, .3)

        has vbox

        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

    # This has to be the last thing shown in the screen.

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip
#툴팁테스트
screen tooltip_test:

    default tt = Tooltip("No button selected.")

    frame:
        xfill True

        has vbox

        textbutton "One.":
            action Return(1)
            hovered tt.Action("The loneliest number.")

        textbutton "Two.":
            action Return(2)
            hovered tt.Action("Is what it takes.")

        textbutton "Three.":
            action Return(3)
            hovered tt.Action("A crowd.")

        text tt.value


#notify 왼쪽위알림
#skip_indicator 스킵중화면
#main-menu 메인메뉴
#navigation esc메뉴
#preferences 기본설정 특수화면이름
#confirm(메시지,예행동,아니오행동)
#매개변수 없어도 () 쓰는게 빠름
#shift d 개발자옵션
#shift i 스크린검사
screen test():
    textbutton "Mouse Test" action NullAction() mouse "spin"
screen a:
    $ who = "Jane"
    $ t = "Hello, [who]!"
    text 'Then I told her, [t!i]' #텍스트에 대체가 포함된경우 !i써야함?
screen name: #이름짓기 정규식보자 기타-텍스트입력
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"

    #pov "My name is [povname]!"

        align (0.5, 0.5)
init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True
screen snap(): #위치변경?

    drag:
        as carmen
        draggable True
        xpos 100 ypos 100
        frame:
            style "empty"
            background "img1.png"
            xysize (100, 100)

            vbox:
                textbutton "London" action Function(carmen.snap, 450, 140, 1.0)
                textbutton "Paris" action Function(carmen.snap, 500, 280, 1.0)


# label splashscreen: #게임시작전 쓸만한듯?  
#     scene black
#     with Pause(1)

#     play sound "audio/bgm1.mp3"

#     show river with dissolve
#     show text "American Bishoujo Presents..." with dissolve
#     with Pause(2)

#     scene river with dissolve
#     with Pause(1)
#     stop sound
#     #$ renpy.movie_cutscene('movie.ogv')
#     return
init python:
    def parse_random(lexer):
        subblock_lexer = lexer.subblock_lexer()
        choices = []

        while subblock_lexer.advance():
            with subblock_lexer.catch_error():
                statement = subblock_lexer.renpy_statement()
                choices.append(statement)

        return choices


    def next_random(choices):
        return renpy.random.choice(choices)


    def lint_random(parsed_object):
        for i in parsed_object:
            renpy.check_text_tags(i.what)


    renpy.register_statement(
        name="random",
        block=True,
        parse=parse_random,
        next=next_random,
        lint=lint_random,
    )
#sprite개웃김
label start:
    
    random:
        "Hello."
        "Welcome."
        "Can I help you?"
    "..."
    "..."
    "..."
    return
label introduction: #랜덤선택
    python:
        greetings = ['Hello.', 'Welcome.', 'Can I help you?']
        greeting = renpy.random.choice(greetings)

    "[greeting]"