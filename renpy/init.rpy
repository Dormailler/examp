init:
    define year = 2023
    define month = 1
    define day = 1

    define level = 1
    define title = "무능력자"
    
    define phy = 10
    define itl = 10

    define height = 150
    define weight = 50
    define age = 15
    define money = 10000
    define stress = 0

    define phy_temp = 0
    define itl_temp = 0
    define money_temp = 0
    define stress_temp = 0

    

    define standard = {
        "name" : "표준식단",
        "change" : 1
    }
    define many = {
        "name" : "든든하게",
        "change" : 2
    }
    define diet = {
        "name" : "다이어트",
        "change" : -1
    }
    

    define rest = {
        "name" : "휴식",
        "phy" : 0,
        "itl" : 0,
        "money": 0,
        "stress" : -8,
        "background" :"room.jpg",
        "character":"jipsa.png",
        "label" : "rest_label"
    }
    define alba = {
        "name" : "알바",
        "phy" : 2,
        "itl" : 0,
        "money": 300,
        "stress" : 10,
        "background" :"mart.jpg",
        "character":"sajang.png",
        "label" : "alba_label"
    }
    define edu = {
        "name" : "교육",
        "phy" : 0,
        "itl" : 2,
        "money": -400,
        "stress" : 15,
        "background" :"edu.jpg",
        "character":"teacher.png",
        "label" : "edu_label"
    }
    define meal = standard
    $ first = second = third = rest
    $ event_list = []
    image misaka_teen = "images/misaka_teen.png"
    image misaka_young = "images/misaka_young.png"
    
    define m = Character("차운재" , color = "#ffe330")

    define dialogue = ""
    define dialogue_list = ["안녕","오늘은 뭐 할까?","꺼져","부끄러워..."] 
    