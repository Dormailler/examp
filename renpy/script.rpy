init:
    define a = "Renpy"
    define b = 999
    define c = [1,3,5,7,9]
    define love = 10

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


label start:
    call screen input("입력하세요")
    # show screen test
    "새로운 렌파이 게임을 만들었군요."
    
    show screen t
    "...."
    # $ love = 20
    # "호감도가 20 상승합니다."
    #$ renpy.movie_cutscene("/video/v1.mpg")
    "...."
    hide screen t
    "...."
    "아아앙아"
    return 
    