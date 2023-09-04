## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story!

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ JJ_name = "JJ"
    $ c_name = "Cashier"
    $ ms_name = "M. Starke"
    $ q_name = "???"
    $ h_name = "Harumi"
    $ d_name = "Daisuke"
    $ mom_name = "Mom"
    $ k_name = "Kara"
    $ JJpark_name = "JJ"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)
    if persistent.playthrough == 0:

        # This variable sets the chapter number to X depending on the chapter
        # your player is experiencing ATM.
        $ chapter = 0

        call Test from _call_Test
        call demo_end from _call_demo_end
        

        # This call statement ends the game but doesn't play the credits.
        call endgame from _call_endgame
        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main from _call_ch10_main
        
        # This jump statement jumps over to Act 2 from Act 1.
        jump playthrough2


    elif persistent.playthrough == 2:
        ## Day 1 - Act 2
        $ chapter = 0
        call ch20_main from _call_ch20_main
        label playthrough2:
            call poem from _call_poem

            python:
                if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
                    try: file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                elif renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                else:
                    try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                    except IOError: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            ## Day 2 - Act 2
            $ chapter = 1
            call ch21_main from _call_ch21_main
            call poemresponse_start from _call_poemresponse_start
            call ch21_end from _call_ch21_end

            # This call statement calls the poem mini-game with no transition.
            call poem(False) from _call_poem_1

            python:
                if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
                    try: file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                elif renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                else:
                    try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except IOError: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            ## Day 3 - Act 2
            $ chapter = 2
            call ch22_main from _call_ch22_main
            call poemresponse_start from _call_poemresponse_start_1
            call ch22_end from _call_ch22_end

            call poem(False) from _call_poem_2

            ## Day 4 - Act 2
            $ chapter = 3
            call ch23_main from _call_ch23_main

            # This if statement calls either a special poem response game or play
            # as normal.
            if y_appeal >= 3:
                call poemresponse_start2 from _call_poemresponse_start2
            else:
                call poemresponse_start from _call_poemresponse_start_2

            # This if statement is leftover code from DDLC where if your game is
            # a demo that it ends the game fully.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end from _call_ch23_end
            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:
        ## Day 1 - Act 4
        $ chapter = 0
        call ch40_main from _call_ch40_main
        jump credits

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
