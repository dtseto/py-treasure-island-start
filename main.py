print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print('''
      ,,, /\_/\ ,,,
       \\=('o')=//
///////////////////////////////////////////////////
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        // (( \\
       "'   )) "'
           ((
            `       Information Highway Victim
///////////////////////////////////////////////////
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
''')
print('You are at a crossroad go Left or Right?')
firststep = input()
if firststep == 'Left':
  print('''
  *******************************************************************************
                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-
*******************************************************************************                                      
''')

  print('Keep walking till reach a stream Swim or Wait?')
  secondstep = input()
  if secondstep == 'Wait':
    print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |     
           |__________|
    
    ''')
    print('A path appears with doors at the end')
    print('Go to Red, Blue or Yellow Doors?')
    thirdstep = input()
    if thirdstep == 'Red':
      print('''
                     (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''')
      print('Burned by Fire GAME OVER')
    elif thirdstep == 'Blue':
      print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
      ''')
      print('Eaten by Beasts GAME OVER')
    elif thirdstep == 'Yellow':
      print('YOU WIN!')
      print(r'''
                                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
      ''')
    else:
      print('YOU LOSE')
  else:
    print('Eaten by a trout')
    print('''
              __ 
             /  ;  
         _.--"""-..   _.
        /F         `-'  [
       ]  ,    ,    ,    ;
        '--L__J_.-"" ',_;
            '-._J
                   fsc
    
    ''')

else:
  print('Fall into a hole GAME OVER')  

