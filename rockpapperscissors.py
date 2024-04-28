k=input('do you want play rock papper scissors?(yes/no)')
while k=='yes':
    print('lets play a game with computer')
    playername=input("enter the player:")
    name=playername
    print('='*100)
    print('hello player {} lets see your luck 😉'.format(name))
    print('select',0,'for rock')
    print('selecet',1,'for papper')
    print('select',2,'for scissors')
    player_input=int(input('the player {} selected:'.format(name)))
    list=['rock','papper','scissors']
    print('player selcted as:',list[player_input])
    import random
    computer_input=random.randrange(0,2)
    print('computer selectd as:',list[computer_input])
    if player_input>2:
        print('invalid option,please select valid option')
        player_input=int(input('the player selected:'))
    elif  player_input==0 and computer_input==0:
       print('its tie')   
    elif  player_input==1 and computer_input==1:
       print('its tie')
    elif  player_input==2 and computer_input==2:
      print('its tie')
    elif  player_input==1 and computer_input==0:
       print('player {} win the match 😊'.format(name))
    elif  player_input==2 and computer_input==1:
       print('player {} win the match 😊'.format(name))
    elif  player_input==0 and computer_input==2:
       print('player {} win the match 😊'.format(name))
    elif  player_input==0 and computer_input==1:
       print('computer win the match and player {} lost 😞'.format(name))
    elif  player_input==1 and computer_input==2:
       print('computer win the match and player {} lost 😞'.format(name))
    elif  player_input==2 and computer_input==0:
       print('computer win the match and player {} lost 😞'.format(name))
    k=input('do you want play rock papper scissors?(yes/no)')                     
