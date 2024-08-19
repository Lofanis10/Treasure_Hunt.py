print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the treasure hunt. Your goal is to find the treasure. But be careful...")
left_or_right = input("You are on a cross road. Where do you want to go? Type l for left and r for right.")
if left_or_right == "l":  # Remember to add the footsteps here.
    bull = input("That looks promising. You see nothing yet, until you get to a farm.\n There is a bull behind you. Type r to try to outrun it, or h to try to hide until it leaves.")
    if bull == "r":
        print(r"""
        
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
        """)
        print("You got chased by the bull. It threw you on the fence. You died.")
    else:
        now_run = input("You hid on a tree. You saw that the bull left. You got away,\n but found a lake. Type s to swim it, or w to wait for a boat.")
        if now_run == "s":
            print("You decided to swim the lake. There were piranhas in it. They torn\n you.")
            print(r'''
     _.--""--._
    /  _    _  \.
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\.
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
             ''')
        else:
            boat = input("OK. A boat came, and the old man inside it asks you\n to pay him. You have no money. Lie that you will pay him (p),\n or give him your bracelet? (b)")
            if boat == "p":
                get_across = input("He took you across. Now he asks for money. Run for it(r), or try to kill him(k)?")
                if get_across == "r" or "k":
                    print(r'''
                      
 ||""""""""""""""""""""""""""""""""  \ \ \  \/~)
 ||                                  \  \ \  \/_
  |~~~~~~~~-________________-_________________\ ~--_
  !---------|_________       ------~~~~~(--   )--~~
                      \ /~~~~\~~\   )--- \_ /(
                       ||     |  | \   ()   \.
                       \____/_ / ()\        \.
                        `~~~~~~~~~-. \        \.
                                    \ \  <($)> \.
                                     \ \        \.
                                      \ \        \.
                                       \ \        \.
                                        \ \  ()    \|
                                        _\_\__====~~~

                    
                    ''')

                    print("That was unfortunate. He had a gun on him. He shot you.")
            else:
                boat_guy = input("He accepted your offer. He got you to the other side. Ask from someone to help you (a)\n or try for yourself? (y)")
                if boat_guy == "a":
                    man = input("A man told you to go to the tower. Type g to go, and n to go were you think.")
                    if man == "n":
                        print(r"""
                                                 
  d8"                                   88  
  88                                    88  
MM88MMM ,adPPYba,   ,adPPYba,   ,adPPYb,88  
  88   a8"     "8a a8"     "8a a8"    `Y88  
  88   8b       d8 8b       d8 8b       88  
  88   "8a,   ,a8" "8a,   ,a8" "8a,   ,d88  
  88    `"YbbdP"'   `"YbbdP"'   `"8bbdP"Y8  
                                            
                        """)
                        print("You did not her the man. You died from starvation, because it took \n you so long to find the treasure. What a dumb ending!")
                    else:
                        tower = input("You went to the tower. You saw a map at the entrance, showing a plan to get the treasure. \n Follow the plan (f), or get back to your sweet home? (h)")
                        if tower == "h":
                            print(r"""
$$$$$$$$$$$$$$$$Q$$$$$$
$$$$$$$$$$$$' $ `$$$$$$
$$$$$$$$$$$$  $  $$$$$$
$$$$$$  $$$$  $  $$"'$$
$$$$$$$  '$$  $  $' .$$
$$$$$$$$.  "  $ .! .$$$
$$$$$$$$$.    '    $$$$
$$^^$$$$$'        J$$$$
$$$   ~""   `.   .$$$$$
$$$$$e,      ;  .$$$$$$
$$$$$$$$$$$.'   $$$$$$$
$$$$$$$$$$$$.    $$$$$$
$$$$$$$$$$$$$     $$$$$    
                            """)
                            print("While on your way back, the same man put you on his boat, for your watch this time. But the boat sank. You, coward!")
                        else:
                            door = input("You entered, and you now see three doors. The plan says that you chose the first one. Type 1 for the first, \n 2 for the second and 3 for the third.")
                            if door == "1":
                                hacking = input("You entered the first room, and the door closed before you. A bomb will go off in one minute. You have four choices:\n 1. Try to get the lock open with a toothpick you had on you. \n 2. Try to stop the bomb from what you learned in the movies you saw.\n 3. Half a minute try for the door, the rest the bomb. \n 4. Pray.")
                                if hacking == "1":
                                    second_chance = input("You got the door open, and avoided your death for now. What door do you choose? The second one (2), or the third one (3)?")
                                    if second_chance == "2":
                                        third_chance = input ("The door is locked. You need a key. For now, you entered the third one. Where will you look for the key? Under the carpet (c), \n in the fridge (f), or in the toilet (t)?")
                                        if third_chance == "c":
                                            look = input ("It was not there. Only an old newspaper. You kept it for future use. Will you look into the fridge (f), \n or in the toilet? (t)")
                                            if look == "f":
                                                watermelon = input ("There is a watermelon inside. Cut it open (c), or run to the toilet for your life? (l)")
                                                if watermelon == "c":
                                                    print(r"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\.
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \.\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\.\ \     )
                        (/ / //  /|//||||\.\  \ \  \ _)
-------------------------------------------------------------------------------

                                                    """)
                                                    print("Well, there were explosives in it. Guess what!...")
                                                else:
                                                    hand = input("You headed straight to the toilet. You looked in it. There is a key. Try to get it \n with hand (h), or with toilet pumper? (p)")
                                                    if hand == "p":
                                                        print(r"""
                                                        
                     _______
              ,,--''         ''--,,
           ,-'                     '-,
          /                           \.
          |                           |
          |                           |
          | |\                     /| |
     |\   | | \                   / | |   /|
     | \  | |  '-,             ,-'  | |  / |
     |  '-| |     '-,       ,-'     | |-'  |
     |      |        \     /        |      |
     |      |    ,-;;/     \;;-,    |      |
     |  ,'   \__|;;;/ ,   , \;;;|__/   ',  |
      \/              |   |              \/
      /             ,-|   |-,             \.
      ;             \       /             ;
       \             '-, ,-'             /
        '-,,            '            ,,-'
            '-,    \.'-,           ,-'
               ',   \  ''--,,   ,'
                 \   ''--,, /  /
                 |\           /|
                 |(           )|
                 |'-,       ,-'|
                     ''-,-'' 

                                                        
                                                        
                                                        """)
                                                        man = input("Well, I should have mentioned earlier that there is no toilet pumper. You put your hand in. \n You got the key, and ran to the door. You opened it. There is a spooky man staring at you. \n he says he wants paper. Write here something paper you have on you. (Do not use capital letters.)")
                                                        if man != "newspaper":
                                                            print(r"""
                      .--. .-,       .-..-.__
                    .'(`.-` \_.-'-./`  |\_( "\__
                 __.>\ ';  _;---,._|   / __/`'--)
                /.--.  : |/' _.--.<|  /  | |
            _..-'    `\     /' /`  /_/ _/_/
             >_.-``-. `Y  /' _;---.`|/))))
            '` .-''. \|:  \.'   __, .-'"`
             .'--._ `-:  \/:  /'  '.\                _|_
                 /.'`\ :;   /'      `-              `-|-`
                -`    |     |                         |
                      :.; : |                     .-'~^~`-.
                      |:    |                   .' _     _ `.
                      |:.   |                   | |_) | |_) |
                      :. :  |                   | | \ | |   |
                    .jgs. : ;                   |           |
            -."-/\.\.\/:::.    `\."-._'."-"_\.\-|           |///."-
            " -."-.\.\."-."//.-".`-."_\.\-.".-\.\`=.........=`//-".

                                                            """)
                                                            print("He killed you. But he buried you afterwards! Such a nice guy!")
                                                        else:
                                                            start = input("Nice memory you have there! He let you go though the door. You are on a crossroad. You go left (l), or right? (r)")
                                                            if start == "r":
                                                                print("Seriously? Didn't you see that stone on the floor? You fell down, hit your head, and died. RIP.")
                                                            else:
                                                                bull_death = input("You are in a farm, and you see a bull. Hide (h) until it leaves, or try to outrun it? (r)")
                                                                if bull_death == "h":
                                                                    print(r'''
       ,/         \,
      ((__,-"""-,__))
       `--)~   ~(--`
      .-'(       )`-,
      `~~`d\   /b`~~`
          |     |
          (6___6)
           `---`
                                                                    ''')
                                                                    print("You tried to get on a tree, but the bull hit it, and you fell. Rest in Peace, olf friend.")
                                                                else:
                                                                    lake_swim = input("Such a brave action. You find a lake. Wait for a boat to come (w), or swim? (s)")
                                                                    if lake_swim == "w":
                                                                        print(r'''
                               __
                             .d$$b
                           .' TO$;\ 
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\ 
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\.
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\ 
                            ; 
                                                                    
                                                                        ''')
                                                                        print("You waited for so long, that night came, and a wolf attacked you. GG.")
                                                                    else:
                                                                        smart = input("You swam the lake, and got across. Good. Now, will you ask for help (h) or not (n)? Oh, Deja-vu...")
                                                                        if smart == "h":
                                                                            print(r"""
                    ___   ___
                  _/~~~\_/~~~\_
                 /~~~~~~~~~~~~~\_
                /~~~~~~~~~~~~~~~~\ 
               /~~~~~~~~~~~~~~~~~~\ 
              /~~~~~~~~~~~~~~~~~~~~\ 
             /~~~~~~~~~~~~~~~~~~~~~~\ 
            /~~~~~~~~~~~~~~~~~~~~~~~~\ 
           /~~~~.__~~~~~~~~~~~~~~~~~~~\ 
          |~~~~~|  \_~~~~~~~~~~~.~~~~~|
          /~~~~~|    \___~~~___/|~~~~~\ 
         /~~~~~~|        \_/    |~~~~~~\ 
        |~~~~~~~|              .|~~~~~~|
        |~~~~~~~|'===-    -===' |~~~~~~|
        /~~~~~~~| ___      ___  |~~~~~~\ 
       |~~~~~~~~|[_@_\    /_@_] |~~~~~~~\ 
       |~~~~~~~~|        .      |~~~~~~~~\ 
       |~~~~~~~~\        |      |~~~~~~~~~|
       /~~~~~~~~~|       \      |~~~~~~~~~~\ 
      |~~~~~~~~~~|     ___)     |~~~~~~~~~~~|
      |~~~~~~~~~~\     ^ ^      |~~~~~~~~~~~|
      |~~~~~~~~~~~|._        _. |~~~~~~~~~~~\ 
      |~~~~~~~~~~~|  \======/   A~~~~~~~~~~~~|
      |~~~~~~~~~~~\   |IIII|   /|~~~~~~~~~~~~|
      |~~~~~~~~~~~~|  |====|  /#|\~~~~~~~~~~~|
      |~~~~~~~~~____\ |    | |##|?\_~~~~~~~~~|
      |~~~~~~__/?:| #\______/#  |:??\__~~~~~~|
       \____/???. |::::|::::::::| .????\___~~|
    ___/???????: ?\:::|:::::::::|? :???????\_|__
  _/??????????. ???|::|::::::::/??? .???????????\_
 /???????????: ????|::A:::::::/????? :????????????
|???????????. ?????|_/H\::::_/??????? .???????????
|??????????: ????? /***\|::/????????? |???????????
|?????????. ????? (*****|_/?????????? |???????????
|????????| ??????? \***/ ???????????? |???????????
|????????| ???????? III ????????????? |???????????
|????????| ??????? /+ +\ ???????????? |???????????
|????????| ?????? ! + + ! ??????????? |???????????
|?????????\ ????? !+ + +! ?????????? /????????????
|??????????\ ???? ! + + ! ????????? /?????????????
|???????????| ??? !+ + +! ???????? |??????????????
|???????????| ??? ! + + ! ???????? |??????????????
|??????????/ ???? !+ + +! ????????? \?????????????
|?????????| ????? ! + + ! ?????????? |?????????? /
|?????????| ????? !+ + +! ?????????? |????????? |?
|?????????| ????? ! + + ! ?????????? |????????? |?
|?????????| ????? !MEPH.! ?????????? |???????? /??
  
                                                                        
                                                                        
                                                                            """)
                                                                            print("He turned out to be a vampire. Guess what...")
                                                                        else:
                                                                            tower_the_second = input("You are brave. I would say if you were. You found a tower. You entered, seeing three doors. Enter the first (1),\n the second (2), or the third (3)?")
                                                                            if tower_the_second == "1":
                                                                                print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-     '    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'


                                                                                """)
                                                                                open_or_not = input("You found a chest. Probably treasure chest. Open it (o), or not? (n)")
                                                                                if open_or_not == "n":
                                                                                    print("Seriously? You cam that far, bro! Well, I will delete you, then! Now!")
                                                                                else:
                                                                                    print("It is my honour to give you the treasure after all. It seems that the scientific program was successful.\n An AI with consciousness -You that is-, managed to get through the maze! You will now be \n used as a powerful tool for humanity.")
                                                                            elif tower_the_second == "2":
                                                                                print(r"""
                                                                                
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                                                """)
                                                                                print("You entered a room full of fire. You ran out of oxygen. Then your body was burnt. Have a good day!")
                                                                            else:
                                                                                fridge_trap = input("There is a fridge here. Open it (o), or not? (n)")
                                                                                if fridge_trap != "hajsnsjbjxjkdjksnskxj":
                                                                                    print(r"""
      /\ 
 __   \/   __
 \_\_\/\/_/_/
   _\_\/_/_
  __/_/\_\__
 /_/ /\/\ \_\ 
      /\ 
      \/
                                                                                    """)
                                                                                else:
                                                                                    print("How did you know? I do not play with cheaters! Leave, now!")
                                                    else:
                                                        yes_or_no = input("Are you sure? It looks dirty... (Type yes or no)")
                                                        if yes_or_no == "yes":
                                                            print("Ewww... There is no way. I will delete you. Now.")
                                                        else:
                                                            print("So you do not want to find the treasure, huh? Well I will delete you now, then!")
                                            else:
                                                are_we_ok = input("We would you want to do that? Anyway, you went to the toilet, opened it, found a key inside. You took it with your \n hand -that was gross-. Then you went to the second door, and opened it. A man is staring at you.\n He wants paper. Type here something you have on you, and is made out of paper (Do not use capital letters.):")
                                                if are_we_ok == "newspaper":
                                                    print(r"""
                      .--. .-,       .-..-.__
                    .'(`.-` \_.-'-./`  |\_( "\__
                 __.>\ ';  _;---,._|   / __/`'--)
                /.--.  : |/' _.--.<|  /  | |
            _..-'    `\     /' /`  /_/ _/_/
             >_.-``-. `Y  /' _;---.`|/))))
            '` .-''. \|:  \.'   __, .-'"`
             .'--._ `-:  \/:  /'  '.\                _|_
                 /.'`\ :;   /'      `-              `-|-`
                -`    |     |                         |
                      :.; : |                     .-'~^~`-.
                      |:    |                   .' _     _ `.
                      |:.   |                   | |_) | |_) |
                      :. :  |                   | | \ | |   |
                    .jgs. : ;                   |           |
            -."-/\.\.\/:::.    `\."-._'."-"_\.\-|           |///."-
            " -."-.\.\."-."//.-".`-."_\.\-.".-\.\`=.........=`//-".

                                                    """)
                                                    print("That is right. But you did not look into the fridge, You need something from there. So I told him to kill you, and bury you,\n because I am polite. You are welcome.")
                                                else:
                                                    print(r"""
                      .--. .-,       .-..-.__
                    .'(`.-` \_.-'-./`  |\_( "\__
                 __.>\ ';  _;---,._|   / __/`'--)
                /.--.  : |/' _.--.<|  /  | |
            _..-'    `\     /' /`  /_/ _/_/
             >_.-``-. `Y  /' _;---.`|/))))
            '` .-''. \|:  \.'   __, .-'"`
             .'--._ `-:  \/:  /'  '.\                _|_
                 /.'`\ :;   /'      `-              `-|-`
                -`    |     |                         |
                      :.; : |                     .-'~^~`-.
                      |:    |                   .' _     _ `.
                      |:.   |                   | |_) | |_) |
                      :. :  |                   | | \ | |   |
                    .jgs. : ;                   |           |
            -."-/\.\.\/:::.    `\."-._'."-"_\.\-|           |///."-
            " -."-.\.\."-."//.-".`-."_\.\-.".-\.\`=.........=`//-".
                                                    """)
                                                    print("He killed you, and buried you afterwards. Such a nice guy! Don't you think?")
                                        elif third_chance == "f":
                                            print(r"""
      ______________________________    . \  | / .
     /                            / \     \ \ / /
    |                            | ==========  - -
     \____________________________\_/     / / \ \ 
  ______________________________      \  | / | \ 
 /                            / \     \ \ / /.   .
|                            | ==========  - -
 \____________________________\_/     / / \ \    /
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |                            | ==========  -  - -
     \____________________________\_/     / / \ \ 
                                        .  / | \  .
                                            """)
                                            print("There were explosives in a watermelon. You were blown up. :( Try again.")
                                        else:
                                            print(r"""
       ---_ ......._-_--.
      (|\ /      / /| \  \ 
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\ 
       `/'\__/      \ _ _ \*\ 
      /^|            \ _ _ \*
     '  `             \ _ _ \      
                       \_
                                            """)
                                            print("There was a snake in the toilet. Its poison killed you in seconds. GG though.")
                                    else:
                                        print(r"""
                                                              
                            _-' "'-,     
                         _-' | d$$b |  
                      _-'    | $$$$ |    
                   _-'       | Y$$P |  
                _-'|         |      |
             _-'  _*         |      |
          _-' |_-"      __--''\    /
       _-'         __--'     __*--'
     -'       __-''    __--*__-"`
    |    _--''   __--*"__-'`  
    |_--"  .--=`"__-||"  
    |      |  |.\   ||
    | .dUU |  | .\ //
    | UUUU | _|___//
    | UUUU |  |   
    | UUUU |  |         
    | UUUU |  |
    | UUUU |  |
    | UUUU |  |
    | UUP' |  |
    |   ___^-"`
     ""'          
                                        """)
                                        print("A gun shot you somehow. I am surely not responsible for that...")
                                elif hacking == "2":
                                    print(r"""
                                  ..-^~~~^-..
                                .~           ~.
                               (;:           :;)
                                (:           :)
                                  ':._   _.:'
                                      | |
                                    (=====)
                                      | |
                                      | |
                                      | |
                                   ((/   \))

                                    """)
                                    print("I think you know what happened...")
                                elif hacking == "3":
                                    print(r"""
                                                                     ..-^~~~^-..
                                                                   .~           ~.
                                                                  (;:           :;)
                                                                   (:           :)
                                                                     ':._   _.:'
                                                                         | |
                                                                       (=====)
                                                                         | |
                                                                         | |
                                                                         | |
                                                                      ((/   \))

                                    """)
                                    print("You started with the bomb. Did not go as planned...")
                                else:
                                    print("I am your God. And I am not willing to help you. Restart!")
                            elif door == "2":
                                print("Every five minutes, the corridor to the rooms gets heated, and burns everything in it. You needed to enter \n a room to get away. But the second one was locked. You were burnt like a chicken in the oven. GG though.")
                            else:
                                hehe = input("You entered the third room. There is a gun in there. If you shoot the target, you will probably open the door in front of you.\n But I do not promise. Take the gun and shoot (g), or wait to be saved? (s)")
                                if hehe == "s":
                                    print("You waited for so much, that you starved to death.")
                                else:
                                    print(r"""
                                 __)),
                                //_ _)
                                ( "\ "
                                 \_-/
                             ,---/  '---.
                            /     - -    \ 
                           /  \_. _|__,/  \ 
                          /  )\        )\_ \ 
                         / _/  (   '  ) /  /
                        / |     (_____) | /
                       /,'      /     \/ /,
                     _/(_      (   ._, )-'
                    `--,/      |____|__|
                               |    )  |
                               |   /   |
                               |  / \  |
                              / `|  | _)
                              |  |  |  |
                              |  /  \  |
                              | |    \ |
                              | \    | \_
                             /__(    '-._`,   
                                    """)
                                    print("Has anyone ever told you that you are not the brightest of all? Like, seriously, you held the gun the other way around, and shot yourself. Game Over.")
                else:
                    print(r"""
                                                                     
                      d8"                                   88  
                      88                                    88  
                    MM88MMM ,adPPYba,   ,adPPYba,   ,adPPYb,88  
                      88   a8"     "8a a8"     "8a a8"    `Y88  
                      88   8b       d8 8b       d8 8b       88  
                      88   "8a,   ,a8" "8a,   ,a8" "8a,   ,d88  
                      88    `"YbbdP"'   `"YbbdP"'   `"8bbdP"Y8  

                    """)
                    print("You did not ask for help. You died from starvation, because it took \n you so long to find the treasure. What a dumb ending!")
else:
    print(r"""
                                              .---.
                                        _.--(\,/\,`\ 
                                      ,' . . .' . \/`-._
                                      : . . .' .  . |  _`--.
                                      :,----'--.  . ; (  \  `-.
                                    ,;:|,-----.`,   `  `\_)  . `-.
                                  ,;;;`;        /; ,         '   `.
                                ,';;,-'`.    ,-;;;;/-.         .  :
                              ,;;;,'     `-,;;;;;-'  `-      ; '
                             .;;,'       ,;;;;-'   :  .     -'
                            .;.'       ,';;;':     `  `
                            ;;'      .;;;-'  ;  ,             ,
            ____,-------.__ `'      .','    ;   `           , '
         ,-'     __,---.__ `-.      `'   ,-'  ,             '
      _,'___,-    `\_:_/'  - `:       ,-'     `  ,
    ,'  ((_); . .    :   . .  :    ,-'           `
  ,' :  '   :  . . _.;._  .  ,' ,-'
 ,'  `      `.  _,:,---.`-._,' ,              _,---------._
'      :     `.::||     ::||  '            ,-'         ___ `-.
  `    `-.     ::||     ::||`-.     __,---.,--_      ,'---`, `.
    ,    `     ::|| `-' ::||   `_,-' `\_:_/'   `--._ `-(_)-'  |
    `          ::||      :||   ; .  .   :    .  .   ;       `.|
               ::||`-'   :||  : .  .  __`.__  .  .  :          |
               `:||      :|;  `.  .  ; ____ :  .  . `,         |
                :;       `'     `.  /;'    `|---._   ;          |
                `               ; );::.,   , \:::||/'           `.
                               .' :::||` - '  :::||              :
                              ,'  :::||       :::||              :.
   (         `.   ,'         ,'   :::|| `--'  :::||  -'          ::
     -.       `---'       _,-'    `::|:       :::||              `|
      `-  (             ,'   ,     ::|| `   ' :::|| -'            |
    )    )  -.         ,'    `     ::||       `::||   --'         :
   ) -.      `     __,-'    ,       :||        ::||               :
      `   _____,--'         `        \;        `;/'            : .:
 __,-----'            ,        ` .                              `::
-'           ,         `      :   `  .         -                   :
     ,    , `,     ,         `.__    `     -      -      ;      '::
(  , '    '  `     `    ;    ,'  `---.__            ;    ',      :
 \ '  ,          ,     ,'               `-._         ;    ';    ::
  `-. '          `    :   ;                 `.        ,    ;,   ::
     )        ,       :   `;                  `.   ,' ` ,  ,'   ;
`.  )__    ,  `  ,    `.   `; __                :  ,    ` ,'   :
 )  )  `---`____ `      `   _'--`-.             ;___,----:    ,
__ \)))          `-----. _,-' --   `------.__,  ,'       |    ;
                     ,-' -__,_______           ;        :       ,'
                      `--'          `---------'          `-----'
    """)
    environment = input("So you went right... You looked around, and you saw many kinds of different and peculiar animals.\n Stop to look at them (l), or move on? (m)")
    if environment == "l":
        print("You sat there, watching them. Until you died from starvation. When we say 'Sit to watch', we do not mean forever.")
    else:
        cube = input("You went further into the forest you found, until you saw a big, white building-like cube. Enter from the front door (d), or get back to your sweet home? (h)")
        if cube == "h":
            print(r"""
                                    (__
                                   ,_) \_,-/
                                  /__      )__,
                                 )/  _\_    /
                                 /d   \ \   \__
                                /  _.'  /    ( '
                               (,-,) |  |_   |_,
                               ,-.___|_  /_,  /
                               ) .__        ) \ 
                                \ \ `-..-    \(`.
                                 \( \_\          `._
                                  \`-,'`.           `-.
                                   `'    `-.__         \ 
                                              `,'      |-,._)
                                              !       ,')   `-.
                                              (    ,-'  (   ,-.)
                                               \   \  \ _/   \_
                                                \_ |\_ \`-'._  )
                                                ( ,'( /      )/
                                            __,','__/(
                                           /__(^ 7..1"
            """)
            print("You got chased by a horse, which killed you. Bad luck... GG.")
        else:
            brave = input("Brave guy we have here! You entered the cube, and found a room, with three doors; one on each side. \n Type 1 to enter the first one, 2 to enter the second one, and 3 to enter the third one.")
            if brave == "1" or "2" or "3":
                maze = input("You entered the door, and saw another room, pretty much the same with the last one. Go into a random door (r), or get back from were you came? (c)")
                if maze == "c":
                    print("The room looked the exact same as before. You opened the door, that you were sure was the one you cam from. But you just found another room. \n You became crazy from what you just saw, and hit your head on the wall so hard, that you died. RIP.")
                else:
                    still_alive = input("You entered a random door, and found the same room. You did this over ten times, until you found a wall, writen with blood 'Help me'.\n Ask if there is anyone here (a), or stay silent, and continue checking rooms? (r)")
                    if still_alive == "a":
                        print(r"""
                        
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\ 
       ::::::;       ;          OOOOO\ 
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
                        """)
                        print("There was a man there. He looked terribly weak. He said 'I am sorry, but I am angry', \n and attacked you, until he ate you. Rest in Peace, old friend.")
                    else:
                        print("You remained silent, and continued doing the same think, until you eventually died from starvation. Better luck next time, traveller!")