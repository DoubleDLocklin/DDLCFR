label KaneMonger:
    'Oh shoot. KaneMonger himself is playing my DDLC mod yet again?'
    'It\'\s truly an honor considering I\'\ve loved your content for years!'
    'Thanks for playing the full release, and playing the demo beforehand.'
    'Anyway, enough talking. Enjoy DDLC Foreign Relations!'
call Chapter1 from _call_Chapter1

label Tbishy:
    'Oh shoot. Tbishy is playing my DDLC mod again?'
    'It\'\s truly an honor that you played my mod when it was in demo.'
    'I\'\m honored that you are playing the full release!'
    'Anyway, enough fanboying. Enjoy DDLC Foreign Relations!'
call Chapter1 from _call_Chapter1_1

label Softlock:
    'Error Code 1995, please consult David Locklin for assistance.'
    'Any attempt at playing will be ended until you can contact him for assistance.'
call Softlock from _call_Softlock

label Rps:
    menu:
        "Rock":
            $selection = "rock"
            $result = renpy.random.choice(['rock', 'paper', 'scissors'])
        "Paper":
            $selection = "paper"
            $result = renpy.random.choice(['rock', 'paper', 'scissors'])
        "Scissors":
            $selection = "scissors"
            $result = renpy.random.choice(['rock', 'paper', 'scissors'])
call Results from _call_Results

label Results:
    if result == "rock":
        if selection == "rock":
            jump tie
        elif selection == "paper":
            jump win
        elif selection == "scissors":
            jump lose

    elif result == "paper":
        if selection == "rock":
            jump lose
        elif selection == "paper":
            jump tie
        elif selection == "scissors":
            jump win

    elif result == "scissors":
        if selection == "rock":
            jump win
        elif selection == "paper":
            jump lose
        elif selection == "scissors":
            jump tie


label win:

$ persistent.rpswin = True

show text "{i}Achievement Get: Outplayed.{/i}" at topright
with dissolve
show natsuki 1a zorder 2 at t11

n'Oh, no fair!'

hide text
with dissolve

n'You sneak!'

n'Best of three?'

call Rps from _call_Rps

label lose:

show natsuki 1a zorder 2 at t11

n'Ha!'

n'Beaten. Fair and square.'

n'Best of three?'

call Rps from _call_Rps_1

label tie:

show natsuki 1a zorder 2 at t11

n'Tied game, [player!u]. Again!'

call Rps from _call_Rps_2

label rpsgame:
    stop music fadeout 2.0
    with dissolve_scene_full

show natsuki 1a zorder 2 at t11

n'[player!u], let\'\s play Rock, Paper Scissors!'
mc'Whatever you say, Natsuki, but I\'\m going to destroy you.'
n'We\'\ll see about that!'
call Rps from _call_Rps_3


label demo_end:

scene black

'Thanks for playing the 1.2 demo of DDLC Foreign Relations!'

'All of us in Team Relations are hard at work making this mod the best it can be!'

'If you would like to help us on our journey, offer feedback, or simply keep in touch with updates, you can join our official Discord server by clickling {a=https://discord.gg/Qu2MU56dwv}here.{/a}'

'If you want to get in touch with me, David Locklin, directly, you can DM me either on Reddit or Discord.'

'Discord: davidlocklin'

'Reddit: u/DoubleDLocklin'

'Anyway, I believe that\'\s it!'

'Again, thanks for playing, and until next time!'

hide window

return