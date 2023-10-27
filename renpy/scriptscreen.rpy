screen test:
    text "[love]" align (0.5, 0.5)
    bar value love range 50:        
        xmaximum 800
        ymaximum 50
        align (0.5, 0.5)
#텍스트 추가
screen test1:
    frame: #없으면 프레임없이 나옴
        text "test1 스크린입니다."
        
        textbutton _("close"):
            action Hide("test1")
        align (0.5, 0.7)
screen test2:
    frame: #없으면 프레임없이 나옴
        text "test2 스크린입니다."
        
        textbutton _("close"):
            action Hide("test2")
        
        align (0.5, 0.7)
screen test3: 
    frame: #없으면 프레임없이 나옴
        text "test3 스크린입니다."
        align (0.5, 0.7)
        
#이미지 추가
screen test4:
    add "btn_hint_idel.png" align (0.5, 0.5) 

screen testi:
    modal True #자기만 누를수있게 
    frame:

        xpadding 40
        ypadding 40

        textbutton _("Renpy"):
            action Show("test1")
            alternate Show("test2")
            hovered Show("test3")
            unhovered Hide("test3")
        align (0.5, 0.5)

screen tes:
    imagebutton:
        idle "img1.png"
        hover "img2.png"
        action Show("tes1")
        alternate Show("tes2")
        hovered Show("tes3")
        unhovered Hide("tes3")
screen tes1:
    frame:
        vbox:
            text "왼쪽 클릭입니다."
            textbutton _("close"):
                action Hide("tes1")
        align (0.5, 0.7)
screen tes2:
    frame:
        vbox:
            text "오른쪽 클릭입니다."
            textbutton _("close"):
                action Hide("tes2")
        align (0.5, 0.7)
screen tes3:
    frame:
        vbox:
            text "hoverd 입니다."

        align (0.5, 0.7)
screen te:
    vbox:
        text "1 2 3"
        text "4 5 6"
        text "7 8 9"
        text "10 11 12"
        align (0.5, 0.5)
        spacing 300
screen t:
    grid 2 3: #2개 3줄
        text "1"
        text "2"

        text "3"
        text "4"

        text "5"
        text "6"
#이름 입력받기
screen intest:
    frame:
        has vbox
        text "이름을 입력하세요"
        input default "메모린"
        align (0.5, 0.5)
#사칙연산테스트
screen t1:
    $ n = 5
    $ m = 9
    vbox:
        textbutton _("더하기"):
            action Return(n+m)
        textbutton _("빼기"):
            action Return(n-m)
        textbutton _("곱하기"):
            action Return(n*m)
        textbutton _("나누기"):
            action Return(n/m)
        align (0.5, 0.5)
        spacing 30

screen t2:
    mousearea:
        area(104, 343, 275, 387)
        hovered Show("t3")
        unhovered Hide("t3")
screen t3:
    frame:
        text "마우스를 올렸을떄"
        align (0.5, 0.5)

define arr = [1,2,3,4,5,6,7,8,9,10]
screen t4:
    side "c b r":
        area (589, 126, 421, 799)
        viewport id "testvp":
            mousewheel True
            draggable True
            #add "img2.png"
            vbox:
                for i in range(30):
                    text str(i)
                spacing 30
        bar value XScrollValue("testvp")    
        vbar value YScrollValue("testvp")
screen t5:
    frame:
        text "이 창은 3초 후에 사라집니다."
        align (0.5, 0.5)
    timer 3.0 action Hide("t5",transition = dissolve)
screen tooltip_test:
    default a = Tooltip("버튼이 선택되지 않았습니다.")

    frame:
        xfill True
        has vbox
        textbutton "하나. ":
            action Return(1)
            hovered a.Action("는 세상에서 가장 외로운 수.")
        textbutton "둘. ":
            action Return(1)
            hovered a.Action("이 무슨 일에도 필요하지.")
        textbutton "셋. ":
            action Return(1)
            hovered a.Action("은 너무 많아.")
        text a.value
#이미지 핫스팟(show)
screen imgmap:
    imagemap:
        ground "img1.png"
        hover "img2.png"

        hotspot (367, 706, 81, 102) action Show("te1")
        hotspot (337, 108, 195, 176) action Show("te2")
        hotspot (290, 382, 255, 261) action Show("te3")

screen te1:
    frame:
        vbox:
            text "빨간색 영역입니다."
            textbutton _("close"):
                action Hide("te1")
            align (0.5, 0.5)
screen te2:
    frame:
        vbox:
            text "파란색 영역입니다."
            textbutton _("close"):
                action Hide("te2")
            align (0.5, 0.5)
screen te3:
    frame:
        vbox:
            text "초록색 영역입니다."
            textbutton _("close"):
                action Hide("te3")
            align (0.5, 0.5)

screen big_hello_world:
    text "Hello, World" size 40
    text "HI,World" style "big_red"
    text "abcdefgdsanldnjakds" style "label_text" align (0.5, 0.5) size 100 color "#fff"
# 텍스트 옵션 init 설정
screen alternative:
    textbutton "Decorated" action StylePreference("text", "decorated")
    textbutton "Large" action StylePreference("text", "large") align (0.5, 0.5)
screen hello_world():
    tag example
    zorder 1
    modal False
    text "Hello, World."

transform hello_t:
    align (0.7, 0.5) alpha 0.0
    linear 0.5 alpha 1.0

screen hello_title():
    text "Hello." at hello_t
    text "Hello.":
        at transform:
            align (0.2, 0.5) alpha 0.0
            linear 0.5 alpha 1.0

screen dismiss_test():

    dismiss action Return()

    frame:
        modal True

        align (.5, .3)
        padding (20, 20)

        has vbox

        text "This is a very important message.":
            xalign 0.5
            text_align 0.5

        # Dismiss can be confusing on its own, so we'll add a button as well.
        textbutton "Dismiss":
            xalign 0.5
            action Hide("dismiss_test")

screen ask_are_you_sure:
    fixed:
        text "Are you sure?" xalign 0.5 yalign 0.3
        textbutton "Yes" xalign 0.33 yalign 0.5 action Return(True)
        textbutton "No" xalign 0.66 yalign 0.5 action Return(False)

screen test_frame():
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5

        vbox:
            text "Display"
            null height 10
            textbutton "Fullscreen" action Preference("display", "fullscreen")
            textbutton "Window" action Preference("display", "window")

screen input_screen():
    window:
        has vbox

        text "Enter your name."
        input default "Joseph P. Blow, ESQ." exclude "_!"

screen keymap_screen():
    key "game_menu" action ShowMenu('save')
    key "p" action ShowMenu('preferences')
    key ["s", "w"] action Screenshot()

screen button_overlay():
    mousearea:
        area (0, 0, 1.0, 100)
        hovered Show("buttons", transition=dissolve)
        unhovered Hide("buttons", transition=dissolve)
# 버튼~~ 안보였다 보이게!
screen buttons():
    hbox:
        textbutton "Save" action ShowMenu("save")
        textbutton "Prefs" action ShowMenu("preferences")
        textbutton "Skip" action Skip()
        textbutton "Auto" action Preference("auto-forward", "toggle")


default difficulty = "Easy"

screen select_difficulty():

    # This frame can be a very complex layout, if required.
    frame:
        align (.5, .3)
        padding (20, 20)

        has vbox

        # This is the button that is clicked to enable the dropdown,
        textbutton "Difficulty: [difficulty]":

            # This action captures the focus rectangle, and in doing so,
            # displays the dropdown.
            action CaptureFocus("diff_drop")

        textbutton "Done":
            action Return()

    # All sorts of other screen elements could be here, but the nearrect needs
    # be at the top level, and the last thing show, apart from its child.

    # Only if the focus has been captured, display the dropdown.
    # You could also use showif instead of basic if
    if GetFocusRect("diff_drop"):

        # If the player clicks outside the frame, dismiss the dropdown.
        # The ClearFocus action dismisses this dropdown.
        dismiss action ClearFocus("diff_drop")

        # This positions the displayable near (usually under) the button above.
        nearrect:
            focus "diff_drop"

            # Finally, this frame contains the choices in the dropdown, with
            # each using ClearFocus to dismiss the dropdown.
            frame:
                modal True

                has vbox

                textbutton "Easy" action [ SetVariable("difficulty", "Easy"), ClearFocus("diff_drop") ]
                textbutton "Medium" action [ SetVariable("difficulty", "Medium"), ClearFocus("diff_drop") ]
                textbutton "Hard" action [ SetVariable("difficulty", "Hard"), ClearFocus("diff_drop") ]
                textbutton "Nightmare" action [ SetVariable("difficulty", "Nightmare"), ClearFocus("diff_drop") ]


screen text_box():
    vbox:
        text "The title."
        null height 20
        text "This body text."

screen side_test():
    side "c tl br":
        text "Center"
        text "Top-Left"
        text "Bottom-Right"

screen timer_test():
    vbox:
        textbutton "Yes." action Call("yes")
        textbutton "No." action Jump("no")

    timer 3.0 action Jump("too_slow")

screen volume_controls():
    frame:
        has hbox

        vbar value Preference("sound volume")
        vbar value Preference("music volume")
        vbar value Preference("voice volume")
screen viewport_example():
    side "c b r":
        area (100, 100, 600, 400)

        viewport id "vp":
            draggable True

            add "img1.png"

        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")
# 버튼 테스트!!
screen vpgrid_test():

    vpgrid:

        cols 2
        spacing 5
        draggable True
        mousewheel True

        scrollbars "vertical"

        # Since we have scrollbars, this positions the side, rather than
        # the vpgrid.
        xalign 0.5

        for i in range(1, 101):

            textbutton "Button [i]":
                xysize (200, 50)
                action Return(i)

# 일정 추가~~~
screen scheduler():
    default club = None
    vbox:
        text "What would you like to do?"
        textbutton "Art Club" action SetScreenVariable("club", "art")
        textbutton "Writing Club" action SetScreenVariable("club", "writing")

        if club:
            textbutton "Select" action Return(club)
            


screen five_buttons():
    vbox:
        for i, numeral in enumerate(numerals):
            textbutton numeral action Return(i + 1)

screen skipping_indicator():
    if config.skipping:
        text "Skipping."
    else:
        text "Not Skipping."

screen preferences():
    frame:
        has hbox 

        text "Display"
        textbutton "Fullscreen" action Preference("display", "fullscreen")
        textbutton "Window" action Preference("display", "window")

    on "show" action Show("navigation")
    on "hide" action Hide("navigation")

screen file_slot(slot):
    button:
        action FileAction(slot)

        has hbox

        add FileScreenshot(slot)
        vbox:
            text FileTime(slot, empty="Empty Slot.")
            text FileSaveName(slot)

# 저장바꾸기
# screen save():
#     grid 2 5:
#         for i in range(1, 11):
#             use file_slot(i)

transform t1():
    xpos 150
    linear 1.0 xpos 0

screen common():
    text "Test" at t1

screen s1():
    tag s
    use common id "common"
    text "s1" ypos 100

screen s2():
    tag s
    use common id "common1"
    text "s2" xpos 100 ypos 100
# 사진 드래그
screen movable_frame(pos):
    drag:
        pos pos

        frame:
            background Frame("img1.png", 10, 10)
            top_padding 20

            transclude

screen test:
    use movable_frame((0, 0)):
        text "You can drag me."

    use movable_frame((0, 100)):
        vbox:
            text "You can drag me too."
            textbutton "Got it!" action Return(True)
# 파이썬 점프 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
screen python_screen:
    python:
        test_number = 5
        test_name = "Test %d" % test_number

    text test_name size 100
    $ test_label = 4
    $ test_label1 = "test_%d" % test_label

    textbutton "Run Test" action Jump(test_label1)
## 카운트다운~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
transform cd_transform:
    # This is run before appear, show, or hide.
    xalign 0.5 yalign 0.5 alpha 0.0

    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

screen countdown():
    default n = 3

    vbox:
        textbutton "3" action SetScreenVariable("n", 3)
        textbutton "2" action SetScreenVariable("n", 2)
        textbutton "1" action SetScreenVariable("n", 1)
        textbutton "0" action SetScreenVariable("n", 0)

    showif n == 3:
        text "Three" size 100 at cd_transform
    elif n == 2:
        text "Two" size 100 at cd_transform
    elif n == 1:
        text "One" size 100 at cd_transform
    else:
        text "Liftoff!" size 100 at cd_transform

## 버튼 점프 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
screen btn:
    frame:
        textbutton _("점프!"):
            #action Show("teee",transition=dissolve)
            action [Hide("btn",transition = dissolve), Jump("yes")]
        align (0.5, 0.5)
screen teee:
    frame:
        vbox:
            text "sadamsdmasdklasdkad"
            textbutton "닫기" action Hide("teee")
            spacing 20
        align (0.5, 0.7)

screen btn1:
    frame:
        vbox:
            for i in a:
                text "[i]" # str(i)
            spacing 10
        align (.1, .5)
    frame:
        vbox:
            textbutton "리스트에 추가":
                action AddToSet(a,"1")
            textbutton "리스트에서 제거":
                action RemoveFromSet(a,"1")
        align (0.5, 0.5)

screen btn2:
    default c = "렌파이"

    frame:
        vbox:
            text "[b]"
            text "[c]"
        align (0.1, 0.5)
    frame:
        vbox:
            textbutton "c를 123으로 변경":
                action SetScreenVariable('c',123) # defualt 스크린벨류!!!!!!!!!!!!!!!!!!!!!!!1
            textbutton "b를 미모린으로 변경":
                action SetVariable("b","미모린") # 원소 문자열로 줘야함
            
        align (0.5, 0.5)
#메뉴 불러올때는 Show 가 아닌 ShowMenu
screen omake:
    tag menu

    textbutton "후일담":
        action Start("afterstory")

# 파이썬식으로 코드짜기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111
screen btn3:
    frame:
        vbox:
            for idx in info.data:
                textbutton (idx.name):
                    action Show("char_info",who=idx)
            spacing 20    
screen char_info(who):
    add 'white'
    add who.img pos(96,88)
    frame:
        vbox:
            text who.name
            text who.atk
            text who.exp

            spacing 20
        pos (968,142)


label start:
    scene bg river
    show screen btn3
    "...."
    "....."
    "1111"
    "2222"
    "#333"
    "4444"
    "5555"
    # call screen t1
    # "[_return]"


    # call screen input("입력하세요")
    # # show screen test
    # e "새로운 렌파이 게임을 만들었군요."
    # e "이름을 지어주세요."
    # call screen intest
    # $ e_name = _return
    # e "제 이름은 [e_name]이군요!"

    # $ love = 20
    # "호감도가 20 상승합니다."
    #$ renpy.movie_cutscene("/video/v1.mpg")
    return  
label yes:
    "yessssssssssssssssssss"
    return
label no:
    "noooooooooooooooo"
    return
label too_slow:
    "tooooooooooo slowwwwwwwwwwwwwww"
    return
label test_4:
    "테스트4입니다."
label afterstory:
    "....."
    return