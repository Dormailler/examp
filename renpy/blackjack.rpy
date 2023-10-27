init python:
    # game end money change
    def cards_pay(winner, loser, bet):
        winner.cash -= bet
        loser.cash += bet
    character_dialogue = {
        "character1": "Hello, I am Character 1.",
        "character2": "Nice to meet you! I am Character 2.",
    }

    

    class blackjack_class:
        def __init__(self, player, enemy):
            self.player = player
            self.enemy = enemy
            self.player.escape = (self.player.cash/2)
            self.enemy.escape = (self.enemy.cash/2)
            self.turn = 0
            self.revealed = False

            self.first_deal_count = 1

            self.bet = 1
        def set_bet(self, amount):
            self.bet += amount
            if self.bet < 1:
                self.bet = 1
            self.cash_check()
        def cash_check(self):
            if self.player.cash < self.bet:
                self.bet = self.player.cash
            if self.enemy.cash < self.bet:
                self.bet = self.enemy.cash
        def pay(self, winner, amount):
            if winner == "player":
                self.player.cash += amount
                self.enemy.cash -= amount
                self.enemy.escape -= amount
            else:
                self.enemy.cash += amount
                self.player.cash -= amount
                self.player.escape -= amount
        def first_deal(self):
            if len(self.player.hand) < 2 or len(self.enemy.hand) < 2:
                if (self.first_deal_count % 2) and len(self.player.hand) < 2:
                    renpy.play("audio/card.mp3")
                    self.player.hand.append(self.player.deck.pop())
                elif len(self.enemy.hand) < 2:
                    renpy.play("audio/card.mp3")
                    self.enemy.hand.append(self.player.deck.pop())
                self.first_deal_count += 1
            else:
                self.turn = 2
        def draw(self, index = False):
            renpy.play("audio/card.mp3")
            if index:
                self.enemy.hand.append(self.player.deck.pop())
            else:
                self.player.hand.append(self.player.deck.pop())

        def set_turn(self, turn):
            self.turn = turn
            if turn == 0:
                self.revealed = False
                self.cash_check()
            elif turn == 3:
                self.revealed = True
            elif turn == 4:
                self.revealed = True
        def next(self):
            self.player.hand = []
            self.enemy.hand = []
            self.set_turn(0)
        def escape_check(self):
            chance = renpy.random.randint(1, 100)
            if chance < 20:
                return "enemy ran"


screen test3:
    frame:
        vbox:
            text "Blackjack is a game where the total number of cards is close to 21.\n Both J/Q/K are calculated as the number 10, and A is calculated as 1 or 11 depending on the situation."
        align (0.5, 0.5)
style mystyle:
    
    hover_background "#00a"
    #outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    # xpos 50 ypos pos 텍스트 위치 변경 
    # yanchor 50 xanchor anchor 텍스트 위치 변경 
    # align
    # xmaximum ymaximum maximum
    # maximum (100, 200)
    # xsize 50 ysize 50 xysize 버튼크기
   
    xsize 30 ysize 60
    align (0.5, 0.5)
    background None
    # xfill yfill area

    # ------------------------------
    # text style
    # bold True 
    # color '#ff0' font "" size "int" italic justify "boolean" 
    # kerning 사이공백? line_spacing 아래공백 line_leading 위공백
    # outlines [(absolute(1), "#f00", absolute(0), absolute(0))] 윤곽선 outline_scaling
    # underline 밑줄 
    # hyperlink_functions - (함수, 함수, 함수) 스타일,클릭함수,포커스함수
    # ------------------------------
    
    # window style
    # background 배경
    # padding ()  modal 이것만클릭
    # margin()
    # ------------------------------

    # button style
    # activate_sound 포커스 사운드
    # focus_mask Ture 웬만하면?

    # -------------------------------

    # box style
    # spacing 간격
    # box_reverse 반전




screen blackjack_screen(g):
    if win_count == 3 or remain ==0:
        timer 0.1 action Return('blackjackend')
    modal True
    # default coin = "cards/coins.png"

    style_prefix "card_games"

    # hbox: # Enemy's cash
    #     align 0.0,0.0 offset 15,15
    #     add coin
    #     text "{}".format(g.enemy.cash) size 35 color "#ff6"
    # hbox: # Player's cash
    #     align 1.0,1.0 offset -15,-15
    #     text "{}".format(g.player.cash) size 35 color "#ff6"
    #     add coin

    # fixed: # Deck
    #     align(1.0,0.5) xoffset -16
    #     fit_first True
    #     at card_game_ani
    #     add "cards/back.png" at zoom(.4)
    
        # align 0.0,1.0 padding 0,0
        # fixed:
        #     fit_first True
        #     add "cards/run.png"
        #     text _("End") align .2,.8
        # action Return("player ran")
        # if g.player.escape < 1:

    frame:
        xpadding 10
        ypadding 10

        button:
            style "mystyle"
            #add "black" xsize 100 ysize 100 xpos -50 ypos -20
            text "?" align (0.5, 0.5) color "#ff6" size 40  # bold True 
            action Show("test3")
            hovered Show("test3")
            unhovered Hide("test3")
            
        align (0.86, 0.05)
    

############# 
    hbox: # Player cards
        align .6,0.3
        at zoom(.4)
        for i in g.player.hand:
            button:
                background None
                add i.img xsize 320 ysize 480
                at card_game_ani
    hbox: # Enemy cards
        align .6,0.0
        at zoom(.4)
        for i in g.enemy.hand:
            button:
                background None
                if g.revealed:
                    add i.img xsize 320 ysize 480
                else:
                    add "cards/back.png" xsize 320 ysize 480
                at card_game_ani
############# Total sum
    if len(g.player.hand):
        fixed:
            align .8,.07 fit_first True
            add "cards/points.png"

            if g.revealed: # Enemies hand
                text str(g.enemy.sum()):
                    size 50 align .5,.5 yoffset -130
                    if g.enemy.sum() > 21:
                        color "#f00"
                    elif g.enemy.sum() == 21:
                        color "#0f0"
                    else:
                        color "#fff"
            else:
                text "??" size 50 align .5,.5  yoffset -130
            text str(g.player.sum()): #player score
                size 50 align .5,.5  yoffset 130
                if g.player.sum()> 21:
                    color "#f00"
                elif g.player.sum() == 21:
                    color "#0f0"
                else:
                    color "#fff"

    # Betting
    if g.turn == 0:
        if len(g.player.deck) < 16: # low cards re shuffle
            timer .01 action Function(g.player.build)
        if g.enemy.escape < 1:
            timer .2 action Function(g.escape_check)


        button:
            align .83,.15 yoffset 0
            xysize 308,150 background "cards/btn.png" hover_background "cards/btn1.png"
            text "START" align .5,.2
            action Function(g.set_turn, 1)
        button:
            align .83,.15 yoffset 120
            xysize 308,108 background "cards/btn.png" hover_background "cards/btn1.png"
            text "END" align .5,.5
            action None
        fixed:
            text "WIN:[win_count]\nREMAIN:[remain]" align (0.81, 0.05)
    # Dealing
    elif g.turn == 1:
        timer .6 repeat True action Function(g.first_deal)
    elif g.turn == 2: # Main game
        hbox:
            align 1.0,.1 xoffset -12 spacing 30
            button:
                align .5,.5
                xysize 308,108 background "cards/btn.png" hover_background "cards/btn1.png"
                text "I'm good." align .5,.5 
                action Function(g.set_turn, 4)
                
            button:
                background None
                fixed:
                    fit_first True
                    add "cards/back.png" at zoom(.4) xsize 560 ysize 800    
                    text "Draw one." size 40 align .5,.5 color "#ff613a" 
                action Function(g.draw)
    elif  g.turn == 3:
        pass
############# Auto wins
    if g.player.sum() == 21 or g.enemy.sum() > 21:
        timer 0.2 action Function(g.set_turn, 3)
        timer 1.5 action Return("player_win")
        # button:
        #     action NullAction()
        #     background "#4f44"
        # frame:
        #     align .5,.5 background "#000a" padding 20,20
        #     hbox:
        #         spacing 20
        #         text "You've gained {} soul points.".format(g.bet) align .5,.5
        #         button:
        #             background "#000a" padding 20,20
        #             text "Next"
        #             action Return("player_win")
                    # action Function(g.next)
    if g.enemy.sum() == 21 or g.player.sum() > 21:
        timer 0.2 action Function(g.set_turn, 3)
        timer 1.5 action Return("enemy_win")
        # button:
        #     action NullAction()
        #     background "#f444"
        # frame:
        #     align .5,.5 background "#000a" padding 20,20
        #     hbox:
        #         spacing 20
        #         text "You've lost {} soul points.".format(g.bet) align .5,.5
        #         button:
        #             background "#000a" padding 20,20
        #             text "Next"
        #             action Function(g.next)
############# AI's turn
    if g.turn == 4 and g.player.sum() < 21 and g.enemy.sum() < 21:
        if g.player.sum() > g.enemy.sum():
            timer .5 repeat True action Function(g.draw, True)
        elif g.player.sum() == g.enemy.sum():
            timer 1 action Return("draw")
            # button:
            #     action NullAction()
            #     background "#fff4"
            # frame:
            #     align .5,.5 background "#000a" padding 20,20
            #     hbox:
            #         spacing 20
            #         text "Its a draw." align .5,.5
            #         button:
            #             background "#000a" padding 20,20
            #             text "Next"
            #             action Function(g.next)
        elif g.player.sum() < g.enemy.sum():
            # timer .1 action Show("blackjack_pay_time", winner = "enemy", amount = g.bet, game = g)
            timer 1 action Return("enemy_win")
            # button:
            #     action NullAction()
            #     background "#f444"
            # frame:
            #     align .5,.5 background "#000a" padding 20,20
            #     hbox:
            #         spacing 20
            #         text "You've lost {} soul points.".format(g.bet) align .5,.5
            #         button:
            #             background "#000a" padding 20,20
            #             text "Next"
            #             action Function(g.next)
############# complete lose
    if g.player.cash < 1:
        timer .1 action Return("player lost")
    elif g.enemy.cash < 1:
        timer .1 action Return("enemy lost")

# screen blackjack_pay_time(winner, amount, game):
#     timer .6 action Hide("blackjack_pay_time"), Function(game.pay, winner, amount)
#     if winner == "enemy":
#         hbox:
#             align 0.0,0.0
#             at blackjack_pay_animation(960, 540)
#             add "cards/coins.png"
#             text str(amount)
#     elif winner == "player":
#         hbox:
#             align 1.0,1.0
#             at blackjack_pay_animation(-960, -540)
#             add "cards/coins.png"
#             text str(amount)

transform blackjack_pay_animation(x, y):
    offset (x,y) zoom 2 alpha 0
    ease .6 offset (0,0) zoom 1 alpha 1


