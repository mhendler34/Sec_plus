#!/usr/bin/python3

from class_security import Security
from class_topics import Topics
import secplusdict

while True:
    topics = Topics()
    topics.main_menu()
    response = input('> ')
    if response == '1':
        #  topics.mod1_menu()  Create this
        #  response = input('> ')
        mod1 = Security()
        mod1.flash_cards(secplusdict.sbj_mod1td, secplusdict.dict_mod1td)
    elif response == '2':
        mod2 = Security()
        mod2.flash_cards(secplusdict.sbj_mod2td, secplusdict.dict_mod2td)
    elif response == '3':
        mod3 = Security()
        mod3.flash_cards(secplusdict.sbj_mod3td, secplusdict.dict_mod3td)
    elif response == '4':
        mod4 = Security()
        mod4.flash_cards(secplusdict.sbj_core, secplusdict.dict_core)
    elif response == '5':
        mod5 = Security()
        mod5.flash_cards(secplusdict.sbj_mod5td, secplusdict.dict_mod5td)
    elif response == '6':
        mod6 = Security()
        mod6.flash_cards(secplusdict.sbj_mod6td, secplusdict.dict_mod6td)
    elif response == '7':
        mod7 = Security()
        mod7.flash_cards(secplusdict.sbj_mod7td, secplusdict.dict_mod7td)
    elif response == '8':
        mod8 = Security()
        mod8.flash_cards(secplusdict.sbj_mod8td, secplusdict.dict_mod8td)
    elif response == '9':
        mod9 = Security()
        mod9.flash_cards(secplusdict.sbj_mod9td, secplusdict.dict_mod9td)
    elif response == '10':
        mod10 = Security()
        mod10.flash_cards(secplusdict.sbj_mod10td, secplusdict.dict_mod10td)
    elif response == '11':
        mod11 = Security()
        mod11.flash_cards(secplusdict.sbj_mod11td, secplusdict.dict_mod11td)
    elif response == '12':
        mod12 = Security()
        mod12.flash_cards(secplusdict.sbj_mod12td, secplusdict.dict_mod12td)
    elif response == '13':
        mod13 = Security()
        mod13.flash_cards(secplusdict.sbj_mod13td, secplusdict.dict_mod13td)
    elif response == '14':
        mod14 = Security()
        mod14.flash_cards(secplusdict.sbj_mod14td, secplusdict.dict_mod14td)
    elif response == '15':
        mod15 = Security()
        mod15.flash_cards(secplusdict.sbj_mod15td, secplusdict.dict_mod15td)
    else:
        print("Do It Again Tomorrow!!")
        break
