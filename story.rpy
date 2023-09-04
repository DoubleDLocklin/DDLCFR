label Test:  
    stop music fadeout 2.0
    with dissolve_scene_full

show text "DISCLAIMER: WHEN DIALOGUE TEXT IS DISPLAYED LIKE THIS: \"{color=#9FA100}Hello world!{/color}\" It is meant to signify that the character's speaking in Japanese."
$ pause(4)
hide text with Dissolve(1.5, alpha=False)

with dissolve_scene_full

'A subdued, high-pitched whine gives way to a rumbling racket, reverberating in my chest, as the rest of my body is gently yanked forward in my seat.'

'...'

'I think we\'\re landing.'

'The onslaught of audible and physical cacophonies serves as a rude awakening, the tires making contact with the tarmac providing most of it.'

'Catching a few hours of sleep on the plane was much needed, but a steady fatigue still mulled over my brain. Nothing a lethal amount of caffeine can\'\t fix though.'

'My mind tries to process the next 24 hours, the wheres, the whats, the whens, the costs. All into a monotonous process that felt second nature to me.'

'Nothing could disrupt me on how I was going to settle down in this new world I\'\ve found myself in.'

'Save for a few ambiguities, though I can\'\t really expect much more of my home school\'\s competency in these things.'

'Christ, one time they mixed up their recycled and drinking water pipes and that\'\s just the tip of the iceberg.'

play music t2b
scene bg peakpx
with wipeleft_scene
show screen StatButtonUIScreen

'Walking down the jet bridge to arrivals I soon come to realise I\'\m no longer inside an air-conditioned heating flying tin can.'

'A chill soon finds itself and I zip up my hoodie in an attempt to retain much of my heat.'

'Looking out the windows shows a vast concrete plateau adorned with lights, as passenger jets taxi, take off, land, a frantic scurry that seems all too chaotic, all under a gentle scattered light through an overcast sky.'

'A mental reminder tells me to take out my phone and turn the airplane mode off and check for any notifications I might have missed out on during the flight.'

'Of course, switching over to the airport wifi as I don\'\t have a sim card here.'

'{i}JJ - 2 Notifications.{/i}'

'Oh, bother.'

label MC_JJ_Landing:          
    $ phone.discussion(mc_JJ)

    $ phone.date(2, 12, 2022, 10, 11)

    $ phone.message("mc", _("Chill dude I've only set foot in Japan for like an hour."))

    $ phone.message("mc", _("It's damn cold is what it is."))

    $ phone.message("mc", _("No snow though."))

    $ phone.message("JJ", _("You dont seem excited bruv."))

    $ phone.message("mc", _("I've been more or less sent on exile, I don't think I should be all that pumped."))

    $ phone.message("JJ", _("Yeah but you're in Japan!"))

    $ phone.message("JJ", _("Lots of cool stuff fr."))

    $ phone.message("JJ", _("You get to make new friends at school."))

    $ phone.message("JJ", _("Maybe cop a baddie."))

    $ phone.message("mc", _("Dude you realise this shit isn't like anime."))

    $ phone.message("mc", _("School is school, I'm sure boringness transcends languages and cultures."))

    $ phone.message("JJ", _("Aight pipe down."))

    $ phone.message("JJ", _("Just tryna be optimistic."))

    $ phone.message("mc", _("I'm just trying to be realistic."))

    $ phone.message("JJ", _("This is why you get no bitches."))

    $ phone.message("mc", _("Oh? Remind me who you went to formal with?"))

    $ phone.message("JJ", _("..."))

    $ phone.message("mc", _("Thought so."))

    $ phone.message("JJ", _("Aight come on man."))

    $ phone.message("mc", _("That aside you know I can't really make small talk with strangers, let alone ones with a language barrier between us."))

    $ phone.message("mc", _("Besides it's not like I'm gonna end up in some whimsical situations like in that one anime you recommended where it was just some guy surrounded by girls all the time."))

    $ phone.message("mc", _("You're not missing out on much I assure you."))

    $ phone.message("JJ", _("Aight fine."))

    $ phone.message("JJ", _("Just dont miss out on anything tho, I wanna know."))

    $ phone.message("JJ", _("I wouldn't waste this opportunity by being a loner n shit."))

    $ phone.message("JJ", _("Especially when you can cop a Japanese baddie."))

    $ phone.message("JJ", _("Leave your old self back at St. Hewlett's bruv."))

    $ phone.message("mc", _("Whatever."))

    $ phone.end_discussion()

'I put my phone back inside my coat pocket.'

'JJ and I must\'\ve been chatting for a while, I can now see the entrance to customs through to arrivals.'

'A small queue seems to have been built up from the other passengers from my flight, and I take this time to get ready.'

'I reposition my bag to pull out the folder with all my documentation - passports and the like - in anticipation for the screening at customs.'

'The queue gets smaller by the minute, and I soon remember I have to take my laptop out onto a separate tray to get scanned.'

'I take a stroll around the airport for a quick lunch having just retrieved my luggage from the carousel. I spot a chic-looking joint that sells pre-packaged meals in a neat little box.'

'Hm, when in Rome I guess.'

'I go in to choose whatever looks the most appetising, prices marked out on small yellow paper stickers on their covers.'

'I flip through my wallet to check out if I\'\ve exchanged enough yen for this.'

'...'

'Good to go.'

'I go over to the cashier and give them the exact amount of yen for it, as I really don\'\t want to embarrass myself by butchering this poor worker\'\s language and making an ass out of myself.'

'They take the bill and hand back a receipt having just been coughed out by a delicately yellowed small plastic printer.'

c'Have a good one.'

mc'Thanks, you too.'

'...'

'Wait.'

'The fuck?'

'{i}*VRR*{/i}'

'I don\'\t have a moment to go over what just happened back at the bento stall as I feel my phone vibrate in my pocket.'

'I look for a spot to sit down in and take in my surroundings. Given it\'\s closeness to where I just was, this has got to be some sort of food court.'

'Bare concrete pillars line the outside, a few metres away from the floor-to-ceiling windows.'

'The floor\'\s made out of some polished stone that has some obvious wear to it, as its shimmer is occasionally broken by streaks left over from rubberized castor wheels of foot traffic.'

'I sit down at a bench, first checking on the notification on my phone.'

'{i}St. Hewlett\'\s College / Kuribayashi High School Exchange Channel.{/i}'

label MC_MS_Landing:     
    $ phone.discussion(mc_ms)

    $ phone.date(2, 12, 2022, 10, 25)

    $ phone.message("mc", _("On it, making tracks."))

    $ phone.end_discussion()

'I stow my lunchbox back into my bag and haul ass to the meet point, given its distance.'

scene bg foodcourt
with wipeleft_scene

'I scan the area around me, it seems like another food court, though the decor and general air of it was leagues above the one I was just at.'

'The ceiling was a lot lower, though it lent itself being more extravagant, with ceiling lights hidden behind sconces to give off the look that the ceiling itself was glowing.' 

'The seating arrangements were vastly superior too, booths upholstered in tartan cushions align themselves in an orderly manner, giving some privacy between groups.'

'Far better than a hodgepodge of sheet aluminium tables and benches.'

'All the tables had groups of people on them save for the odd loner, and I was hard pressed to find the correct one.'

show sayori 1a zorder 2 at t32
show natsuki 1a zorder 2 at t31
show monika 1a zorder 2 at t33

stop music fadeout 2.0

'Just as I was doubting myself on finding them, I spotted a group of girls in uniform out in the distance by the windows.'

'The colors are on point with mine I packed for before the flight, a grey-ish blazer with blue skirts. That has to be Kuribayashi High.'

show sayori 2b zorder 2 at t32
show natsuki 1a zorder 2 at t31
show monika 1d zorder 2 at t33

'As I approach the group I spot one of them adorned with a red bow gently nudges the girl with the white bow next to her, soon pointing in my direction.'

'A thought crosses my mind whether hair accessories signify a pecking order, but I soon dismiss this notion.'

show sayori 2b zorder 2 at t32
show natsuki 1a zorder 2 at t31
show monika 3j zorder 2 at h33

m'Over here!'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'She outstretches an arm up in the air and flashes a wide grin, unaware of any attention she might bring to herself.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'I get closer only to realise the reality of the situation before me. The hustle and bustle of the food court dying down in my head.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'The rest of the world is melting away outside my ever-narrowing cone of vision.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'One, two, three.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'Ah crap.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'They\'\re all girls!'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'I steel myself as I make first contact with these strangers from a strange land.'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'Breathe in...'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'Breathe out...'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

'Breathe in...'

show sayori 2b zorder 2 at t32
show natsuki 1c zorder 2 at t31
show monika 3j zorder 2 at t33

mc'Hey guys. You\'\re Kuribayashi High, yeah?'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1i zorder 2 at t33

'I do a quick recount on what I just said and internally facepalm at my own expense.'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1i zorder 2 at t33

'For one, they\'\re all girls.'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1i zorder 2 at t33

'Two, they think that I think they\'\re all called Kuribayashi. '

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1i zorder 2 at t33

'Three, ending a sentence with "yeah" is cryptic as hell for them.'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1i zorder 2 at t33

'Then to wrap things up, I don\'\t even know if they understood all that!'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1e zorder 2 at t33

'What a great start.'

'The girls exchange cursory glances at one another, before deciding the one with the white bow is the one to respond to that mismatch of diplomatic vomit.'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1b zorder 2 at t33

play music kofuku

m'Yes, we are! I\'\m Monika! This is Sayori and Natsuki!'

show sayori 1g zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1j zorder 2 at t33

'Okay, lesson learnt from last time, keep it simple.'

show sayori 1a zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1j zorder 2 at t33

mc'G-good to see all of you.'

show sayori 1a zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1j zorder 2 at t33

m'Likewise.'

show sayori 1a zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1a zorder 2 at t33

'I take note of Monika, I suspect she\'\s the host I\'\ve been assigned to.'

show sayori 1a zorder 2 at t32
show natsuki 1g zorder 2 at t31
show monika 1a zorder 2 at t33

'I exchange handshakes with them then take my seat, after which one of them speaks up.'

show sayori 1i zorder 2 at t32
show natsuki 2m zorder 2 at t31
show monika 1a zorder 2 at t33

'The pink haired one - who I believe going by seating order is Natsuki - says something in an inquisitive tone, which gets a stern reply from the red bow.'

show sayori 1d zorder 2 at t32
show natsuki 2o zorder 2 at t31
show monika 1e zorder 2 at t33

'Natsuki\'\s face then emerges with a hue of crimson, with the rest of the group laughing at her expense I think. All I could gather from that little exchange was "boy". I guess they\'\re talking about me.'

show sayori 1a zorder 2 at t32
show natsuki 2s zorder 2 at t31
show monika 1a zorder 2 at t33

'All of them soon reach into their bags. I glance over to Monika as some desperate plea as to what to do.'

show sayori 1a zorder 2 at t32
show natsuki 2s zorder 2 at t31
show monika 1b zorder 2 at t33

m'We\'\re having lunch, would you like to join us?'

'Screw it, if she is the person who I think she is I\'\m sure she\'\s fluent enough.'

mc'Sure thing.'

show sayori 1a zorder 2 at t21
show natsuki 2s zorder 1 at thide
hide natsuki
show monika 1a zorder 2 at t22

'I retrieve my lunchbox from my bag, whilst catching onto little tidbits of the conversation the girls are having between them, with the word "write" showing up here and there.'

show sayori 1b zorder 2 at t21
show monika 1a zorder 2 at t22

'As soon as my eyes are redirected from my bag to the tabletop I\'\m met with two pairs of inquisitive eyes.'

'One I\'\m fairly familiar with but the other one wants to say something but can\'\t quite communicate.'

show sayori 1l zorder 2 at t21
show monika 1a zorder 2 at t22

'As soon as I catch on, Sayori glances away, staring down at her own lunch.'
show sayori 1l zorder 1 at thide
hide sayori
show monika 1a zorder 2 at t11

mc'You know, I thought you\'\d be a guy, Monika.'

show monika 1b zorder 2 at t11

m'We\'\d all thought you\'\d be a girl, hehe~'

show monika 1a zorder 2 at t11

mc'The exchange channel abbreviates our first names, so I had a feeling something like this would happen.'

show monika 1j zorder 2 at t11

mc'In any case, Ms. Starke, it\'\s good to finally see you in person.'

show monika 1a zorder 2 at t11

'We all continue with unpacking lunch, until Sayori pipes up to Monika.'

show monika 1a zorder 2 at t22
show sayori 5b zorder 2 at t21

'Monika\'\s hand gestures tell me it\'\s got something to do with me and my lunch. Sayori appears to relent to Monika and looks at me, eye contact breaking with every time she touches her indexes together.'

show monika 1a zorder 2 at t22
show sayori 5a zorder 2 at t21

s'M-may I have one?'

'Ah.'

show sayori 4r zorder 2 at h21
show monika 1k zorder 2 at t22

'I slide over my bento to her and give her a nod, her eyes lighting up after doing so. This seems to get a giggle out of everyone else.'

'Sayori asserts herself and grabs a piece of fried tofu from my bento, self-satisfaction plastered on her face.'

'Given her eagerness to take a bit of my lunch I retract my bento, away from the range of her chopsticks.'

show sayori 1o zorder 2 at t21
show monika 1e zorder 2 at t22

'Monika nudges Sayori back and says something to her in an authoritative tone.'

m'{color=#9FA100}What do you say afterwards?{/color}'

'Huh, guess I caught what she said.'

show sayori 4q zorder 2 at t21
show monika 1a zorder 2 at t22

s'Thank you!'

mc'You\'\re welcome.'

show sayori 4q zorder 1 at thide
hide sayori
show monika 1a zorder 1 at thide
hide monika

scene bg foodcourt
with wipeleft_scene

'The lot of us finished our lunch 10 minutes ago, and the rest of the group have been engaged in idle chit-chat.'

'I somewhat strain my ears into what they\'\re saying, picking up words that are often brought up.'

'I focus on a couple, especially on this "Literature Club" I keep hearing about.'

'Curiosity gets the best of me, and I press Monika for answers.'

show monika 1a zorder 2 at t11

mc'Monika, you\'\re in a club I presume?'

show monika 1b zorder 2 at t11

m'Yes. Actually, these two are in it as well. If we had one more come over this would\'\ve been a club meeting of sorts.'

m'I\'\m the club president and Sayori is the vice-president.'

show monika 1a zorder 2 at t11

'Huh. So there is a pecking order!'

mc'I see. What\'\s your club about?'

show monika 1m zorder 2 at t11

m'It\'\s umm. How do you say..'

show monika 4b zorder 2 at t11

m'Poetry, books, we talk about them and write some as well.'

mc'Huh.'

show monika 4m zorder 2 at t11

m'I know it doesn\'\t sound all too exciting but-'

show monika 4d zorder 2 at t11

mc'Oh no, I\'\m fully interested. The club could be a massive help in my learning.'

show monika 1d zorder 2 at t11

mc'It\'\s partly the reason why I got transferred anyways, language enrichment and so on.'

'...'

'My mind rushes back to what JJ told me.'

'Leave your old self back at St. Hewlett\'\s bruv.'

'...'

'Fuck it.'

mc'Consider this my application.'

show monika 1j zorder 2 at t11

'Monika shoots me a warm smile, soon outstretching a hand to me. I do the same.'

show monika 5a zorder 2 at t11

m'Application accepted! Welcome aboard!'

mc'Glad to be here, thank you.'

show monika 1a zorder 2 at t33
show sayori 1b zorder 2 at t32
show natsuki 2c zorder 2 at t31

'I notice the two other girls glance at each other speculatively, with Natsuki being the most vocally interrogative.'

'This back and forth comes to a close, with Sayori facing Monika in an equally puzzled demeanour Natsuki had with her a moment ago.'

show sayori 1c zorder 2 at t32

s'{color=#9FA100}Monika, did he just join?{/color}'

mc'{color=#9FA100}Yes.{/color}'

show sayori 4m zorder 2 at h32

s'WAWA-'

'I\'\m guessing I just shook up the vice-president over a combination of granting her club a new member and the fact I can understand a modicum of Japanese.'

'Displays of awe and excitement vie for control over her face, before deciding on just awe.'

show sayori 2c zorder 2 at t32

s'{color=#9FA100}You can speak Japanese?{/color}'

mc'{color=#9FA100}Yes, only some though. I came to Japan to learn.{/color}'

mc'{color=#9FA100}May your club be good to me.{/color}'

show sayori 1o zorder 2 at t32

'That didn\'\t sound right, but I\'\m sure she\'\ll get the gist of it.'

show sayori 4r zorder 2 at t32

s'Yes! Very good!'

s'Natsuki will make cupcakes for you!'

show natsuki 1p zorder 2 at t31

'I shoot Natsuki an eyebrow, her mouth agape in shock.'

mc'Wow, just for me?'

show monika 2e zorder 2 at t33

m'{i}snnrrk-{/i}'

show natsuki 5o zorder 2 at t31
show sayori 1n zorder 2 at t32

n'Sayori! You dummy!'

stop music

play sound "sfx/slap.ogg"

show sayori 4m zorder 2 at h32

'Natsuki slams an upright hand onto the top of Sayori\'\s head, as if to split it open with a light-hearted karate chop.'

show monika 1j zorder 2 at t33

'Monika and I share a laugh at the pair\'\s expense.'

show sayori 4l zorder 2 at t32

s'Oww.'

'Natsuki\'\s chop to her head may have not been as light-hearted as I thought, if it warrants that type of reaction from Sayori.'

show natsuki 5r zorder 2 at t31

'I glance back to Natsuki, curious if she\'\s somewhat remorseful, but I see she\'\s beet red and slightly out of breath.'

show natsuki 5h zorder 2 at t31
show sayori 4b zorder 2 at t32
show monika 4e zorder 2 at t33

m'What I think she meant to say was that this is a special occasion, so catering is in order.'

show sayori 4q zorder 2 at t32
show natsuki 5t zorder 2 at t31

mc'Well, you\'\re all too kind.'

show sayori 4q zorder 2 at thide
hide sayori
show natsuki 5t zorder 2 at thide
hide natsuki
show monika 4e zorder 2 at thide
hide monika

'An awkward silence soon falls onto our group, with the commotion of the airport serving as our salvation out of it.'

'I scramble my brain trying to find another way out of it, only to find it focusing on the very situation I find myself in.'

'Just some foreigner surrounded and building rapport with 3, quite frankly, cute schoolgirls.'

'Now that I think about it like that, this seems strikingly familiar.'

'...'

'Oh!'

play music t2b

'Bingo!'

'I rifle through my bag to find my sunglasses, the rest of the girls catching onto me making haste of my rucksack.'

'I find the pair stowed in the front pocket, just barely tangled on a phone charger wire.'

'A delightfully devilish grin finds itself growing on my face as I pull out my phone, unlocking it with my fingerprint and opening the camera app.'

'I put on my sunglasses carefully trying not to poke any eyes out.'

'As all of the girls had their eyes already trained on me they picked up on what I\'\m about to do. Peace signs form from my peripheral view.'

'I raise my phone to try to get everyone in frame, and try to replicate one of those gang signs JJ taught me.'

'I take the photo.'

mc'Thanks everyone!'

'I take off my sunglasses and put them back into the front pocket of my bag, with as much forethought as last time.'

'I inspect the photo for a moment, before spotting the time and immediately feeling a sense of urgency take over.'

show monika 1d zorder 2 at t11

mc'Hey Monika, you said over the exchange channel there would be other things you would show me after meeting at the airport? It\'\s uhh...'

'I lock the phone to show her the lock screen, time of day as large as it could be on my phone.'

show monika 1b zorder 2 at t11

m'Oh! Right! We have to hurry back to the station, the airport is very far from mine and the rest of the others.'

'Monika then stands, quickly turning her head to the other two.'

m'{color=#9FA100}Sayori! Natsuki! Let\'\s go!{/color}'

show monika 1b zorder 2 at thide
hide monika

'The rest follow suit, as I press the button on my luggage to extend its carrying handle.'

'I kick the lower end of my luggage while on the move to get it into a more ergonomic position.'

'It isn\'\t long until we reach the exit of the airport, the sliding doors let loose a brisk gust of January wind.'

stop music fadeout 2.0
scene bg train
with fade_scene_transition
play music trainride

'It hasn\'\t been long since we\'\ve boarded the airport express train, so much so that a few of us were nearly swept off our feet from the sudden change in motion once the train got going.'

'I look out the window to watch an ever-increasing density of buildings fly past me. A few minutes pass and this landscape broadens out into the horizon.'

'An endless concrete ecumenopolis, caked in grey skies.'

'I feel miserable about it, but I try my best to keep a neutral face, constantly reminding myself that it could always be worse.'

'At least there\'\s no graffiti, no assholes doing pullups on the hand rails in the train, no random puddles of god-knows-what on the floor.'

'At least it\'\s clean.'

'Maybe when the snow comes around it\'\ll be better.'

show monika 1c zorder 2 at t11

'I see Monika\'\s head turn towards me in my peripheral vision, dwelling for a few seconds before returning.'

#INSERT MONIKA BUS CG HERE

'Monika.'

'She\'\s been a big help so far.'

'The last thing she taught me was how to buy tickets from the machines.'

'She explained that not every train ride needs tickets but for this one it needed it.'

'I mull over the process of buying tickets from these types of stations, ultimately deciding to just go over the video I recorded of Monika pointing out which buttons to press and in which order.'

'All the differing colours provide a nice contrast to the litany of Japanese text, lending them a great amount of readability.'

'Going over the video several times I pick up on certain bits of kanji that show up a couple of times.'

'I feel like I gotta remember them for later, but I know damn well I won\'\t unless I write \'\em down somewhere.'

mc'Hmm.'

show monika 1d zorder 2 at t11

mc'Hey, Monika? How long is this train ride?'

show monika 3d zorder 2 at t11

m'A little over an hour from now I think.'

mc'Hm. Alright.'

$renpy.music.set_volume(0, 0.4, "trainride")

play music yasuragi

'I take out my notebook and pen from my bag that\'\s in front of my feet.'

'Time spent moving and doing nothing else seems wasteful, so I might as well be a little productive.'

show monika 1c zorder 2 at t11

'I unfold the folding table between Monika and I, trying to figure out how and where it\'\s supposed to spin.'

'Eventually it lies flat above my lap, barely bending from its joint as I place my notebook and phone on top of it.'

'I press play on the video again and pause to a specific point showing a text box with kanji in it.'

'I try to replicate it as best as I can in my notebook, after which I end it with a dash.'

mc'Hey Monika, what does this mean?'

show monika 1d zorder 2 at t11

m'Mm, purchase, buy, something like that.'

mc'And the other one?'

m'If it\'\s with the same one it means the same thing, but if it\'\s on its own it means enter.'

show monika 1c zorder 2 at t11

mc'Ah, thanks.'

'I write out their definitions after their respective dashes, after which I end with another dash.'

mc'And how would you say them?'

show monika 1d zorder 2 at t11

m'{color=#9FA100}Buy and enter.{/color}'

show monika 1a zorder 2 at t11

mc'Thanks.'

show monika 1a zorder 2 at thide
hide monika

'I write out how they\'\re said in hiragana after their final dashes.'

'Monika and I continue this back and forth until there\'\s no more video left to analyse.'

'A good chunk of a page in my notebook\'\s got new kanji translations now. I must\'\ve doubled the amount of it in a span of a few minutes.'

'I flip through the other pages of my notebook to see how far I\'\ve come learning Japanese, feeling somewhat embarrassed at how pell-mell my organisation of certain topics are throughout it.'

'Especially when I know I\'\m being watched, and especially because they know how to read both languages in my notebook.'

'Because of this I make an effort not to cross over the halfway mark of it.'

'...'

'Content with my work I fold my table back into its little crevice and stow my pen and notebook back into my bag.'

'I stretch out before reclining back into my seat.'

show monika 2d zorder 2 at t11

m'[player]...'

m'Do you have any friends back home?'

'Subtle.'

'I know she didn\'\t mean it like that, so I don\'\t comment on it.'

'However, I still find it pretty funny in my self-deprecating mind.'

mc'Yeah, but they always had to go to some other school or move away.'

mc'I didn\'\t really keep in contact with many of them afterwards.'

mc'But there\'\s one guy I\'\ve been friends with for quite a while.'

'I remember the original purpose I took that photo for back at the airport, but I gotta send it to him before I hit the hay.'

'I know for a fact he\'\ll attempt an international call over it. Multiple times.'

mc'I still keep in touch with him, he\'\s been real keen on what I\'\ve been up to.'

m'Mmm.'

mc'What brought this up?'

show monika 2m zorder 2 at t11

m'Oh! Umm, it\'\s just that before we went through that video and analysed it together, you reminded me of a friend we have.'

m'The one that didn\'\t come with us to meet with you.'

m'She isn\'\t really lively, like those two over there.'

show monka 2d zorder 2 at t11

'Monika turns her head over to Sayori and Natsuki, both leaning over to their left, drool seeping from the corner\'\s of their mouths, the pair out like a light.'

mc'Bad timing, but point taken.'

show monika 2l zorder 2 at t11

m'Ehe, anyways...'

show monika 1b zorder 2 at t11

m'She tends to keep to herself a lot, and always looks like she\'\s in deep thought.'

show monika 1a zorder 2 at t11

mc'I see the similarities I guess. She\'\s not one for loud places or crowds either I assume?'

show monika 1b zorder 2 at t11

m'Yeah, hence her absence.'

show monika 1a zorder 2 at t11

mc'Hm.'

mc'And her English? How much does she know?'

show monika 3b zorder 2 at t11

m'Oh she\'\s quite good actually.'

m'She reads a lot, she has a translated copy of a novel and the original English one side by side while she reads.'

m'I would say that she\'\s almost as good as me, but she doesn\'\t really know how to form sentences properly.'

show monika 1b zorder 2 at t11

m'But she would occasionally say some really long English word that none of us know then never explain it.'

mc'Ah.'

'I prepare myself to put on the best pirate voice I could muster.'

show monika 1c zorder 2 at h11

mc'Hark! Salvation has come for thee, Winslow.'

'...'

show monika 1d zorder 2 at t11

m'W-What?'

show monika 1c zorder 2 at t11

mc'It means that help is on the way.'

show monika 1d zorder 2 at t11

m'Oh.'

show monika 1c zorder 2 at t11

'That was funnier in my head.'

show monika 1m zorder 2 at t11

m'A-Anyways, my point is that she\'\s really shy, but I\'\m sure she\'\ll open up to you, as she did to everyone else.'

mc'I see.'

show monika 1a zorder 2 at t11

mc'Thanks for the heads up.'

show monika 1a zorder 2 at thide
hide monika

'I use the rest of this time to catch up on any sleep I might have missed out on my flight, as I didn\'\t get a chance to grab an energy drink back at the airport.'

'I rest my head farther back into my seat, as if to bury it deeper akin to a pillow, though the seat gives only a firm push back against my skull.'

'Closing my eyes, I try to think about nothing.'

stop music fadeout 2.0
scene black
with eye_shut

'...'

'Void.'

'...'

'Noises all meld together, indecipherable in my current state, with only sudden, slightly louder noises being of note. Moot points over a sea of nothing.'

'...'

'Minutes pass as if they were mere moments, fleeting blinks of time.'

'...'

'I can feel myself falling.'

'I can feel myself in freefall.'

scene bg train
with eye_open

'I suddenly twitch awake, very much aware of where I am, what I am, who I am.'

show monika 1h zorder 2 at t11

mc'Mmh.'

m'Are you okay?'

mc'Yeah, I\'\m uh...'

mc'I\'\m fine...'

mc'Though, I don\'\t know when I am.'

'...'

'What?'

mc'How long do we have left?'

m'Death comes to us all, some sooner than others.'

scene black
with eye_shut

'I close my eyes, partly to process whatever she just said and to also give them an extra moment\'\s rest.'

mc'The train ride, Monika. How long do we have left to go?'

m'Oh! We\'\re nearly there!'

'What the fuck, Monika.'

play music trainride
scene bg train
with eye_open

'I open my eyes and look out the window, we\'\re surrounded by residences and apartments now.'

'I feel the train\'\s slow and gradual deceleration as it nears the station, commotion growing within the train as passengers gather their things and ready their bags.'

'I ready myself, placing my backpack onto my lap.'

'A few moments later we all stand, as I thread my arms through the straps. The rest of the group egress save for Monika, who takes out my luggage from the overhead storage for me.'

mc'Thank you.'

stop music fadeout 2.0
scene bg train_station
with fade_scene_transition
play music t2b

'With me being the last person out, we regroup at one of the platforms.'

'Clear skies have driven the dark clouds far away, basking everything in a warm light.'

show sayori 2q zorder 2 at t21
show natsuki 5g zorder 2 at t22

'I notice Sayori waving one arm in the air as if she weren\'\t a few metres away from me.'

'I also notice Natsuki being a little standoff-ish and anxious looking.'

show sayori 2r zorder 2 at h21

s'[player]!'

'I approach her, the station platform making my luggage rumble with a newfound loudness.'

show sayori 2a zorder 2 at t21

s'{color=#9FA100}Natsuki wants to ask you a question!{/color}'

'Now that I\'\ve gotten a closer look, Sayori\'\s smile is just as radiant as her eyes when I relented to her demands over lunch.'

'...'

'Settle down, Romeo, damn.'

mc'Oh?'

mc'{color=#9FA100}What is it, Natsuki?{/color}'

show natsuki 5q zorder 2 at t22

'Sayori turns to face Natsuki, her smile unwavering.'

n'Are... you going to stay in the club?'

'Natsuki seemed hesitant when asking me that question, as if she had her reservations or something.'

'I really can\'\t get a read on her, I suppose I have to reassure her of this.'

show natsuki 5k zorder 2 at t22

mc'{color=#9FA100}Yes.{/color}'

mc'{color=#9FA100}All of you have been really helpful, I can learn really well.{/color}'

mc'Really well in the literature club.'

'I curse myself for not knowing how to say \'\specifically\'\ in Japanese.'

show natsuki 5t zorder 2 at t22

'No matter though, it seems that my message got through as Natsuki adopts a wry smile, turning her head away to hide it.'

s'Happy now?'

show natsuki 5s zorder 2 at t22

'Natsuki pouts, eliminating her smile.'

show sayori 1s zorder 2 at t21

'We all share a chuckle before heading off to the station\'\s exit.'

show sayori 1s zorder 2 at thide
hide sayori
show natsuki 5s zorder 2 at thide
hide natsuki

scene bg crossroads
with wipeleft_scene

'We arrive at a crossroads, with Sayori and Natsuki splitting off in the other direction, with Sayori twirling around to give Monika and I a wave.' 

s'{color=#9FA100}Bye you two!{/color}'

m'Bye Sayori! Bye Natsuki!'

mc'Goodbye.'

'Natsuki raises an arm and flashes a peace sign, keeping her head and eyes forward.'

'The two groups gain distance from each other, returning to an amiable silence only broken by the nearby city\'\s ambience and my luggage.'

show monika 1b zorder 2 at t11

m'You don\'\t talk much do you?'

show monika 1a zorder 2 at t11

'Well, I thought it was amiable.'

mc'That\'\s not what my teachers think back home.'

mc'But yeah, I don\'\t really start conversations.'

mc'Though I do keep them rolling on.'

mc'I just, do a lot of observing.'

mc'But somehow I do all of that observing and I still do things without an ounce of forethought.'

mc'Even now, I just talk and talk.'

'I look at Monika, then straight ahead, letting out a small huff.'

show monika 1d zorder 2 at t11

mc'I dunno, maybe I just like having a friend lend a pair of ears and take what I say to heart.'

mc'But enough about me, what about you?'

mc'Excuse my prejudices but when I saw you, you kinda struck me as the outgoing type.'

show monika 4n zorder 2 at t11

m'Th-thank you. I guess I do have to keep appearances. I got into being a lot more confident because of all the roles I had to take up over the years.'

m'That and also I seem to be quite popular, if that\'\s the word.'

show monika 4m zorder 2 at t11

'A bit up yourself, aren\'\t you?'

'Ugh, knock it off, she didn\'\t mean it like that.'

show monika 4n zorder 2 at t11

m'People always come up and invite me to all sorts of things.'

m'But I wish they didn\'\t.'

show monika 4m zorder 2 at t11

mc'Why\'\s that?'

show monika 4g zorder 2 at t11

m'I don\'\t feel like they actually want to be my friends.'

show monika 4p zorder 2 at t11

m'Um, how do I say this?'

m'It\'\s...'

show monika 1q zorder 2 at t11

m'{color=#9FA100}It\'\s all fake.{/color}'

'...'

mc'{color=#9FA100}I see.{/color}'

'I decide not to press on, the whole tone of that just teems with baggage that I don\'\t really wanna discuss with a person I met mere hours ago.'

show monika 1q zorder 2 at thide
hide monika

scene bg monika_house
with wipeleft_scene

'We arrive at a street lined with two-storey houses, and judging from Monika\'\s fiddling and the jangling emanating from her pockets I\'\d say we\'\re nearly there.'

'I take notice of how much more affluent and pristine this neighbourhood is compared to the numerous one\'\s we passed by.'

'Guess I got lucky.'

'In more ways than one-'

'No, stop it.'

'Monika puts the keys in the lock, a hefty and crisp click resonates through the front door before swinging open.'

scene bg Living_Room
with wipeleft_scene

'I enter through the front door and immediately notice that the rest of the house\'\s floor is raised apart from a small section of the entrance.'

'I knew this would happen, so I rid myself of my bag and pull out my pair of slippers that\'\s been stowed and marinating ever since I packed for this trip.'

show monika 2b zorder 2 at t11

m'Huh.'

show monika 1a zorder 2 at t11

'I take off my shoes and push them off against the genkan step.'

mc'Something on your mind?'

show monika 1b zorder 2 at t11

m'Ah, nothing. I just thought I had to remind you.'

show monika 1a zorder 2 at t11

mc'What, this?'

mc'They taught us manners in Japanese class back home.'

show monika 1e zorder 2 at t11

mc'Wish they did in every class, to be honest.'

show monika 1e zorder 2 at thide
hide monika

'As I say this, I lift up my luggage to clear the step, only to hit it on the way up.'

'Oh god damn it.'

'I look at the edge of the step to see if it had any marks on it.'

'Any damage I do see is way out on the other side, giving a sigh of relief to myself.'

'I grab the side handle to hopefully avoid future collisions and create a pig sty out of my host\'\s house.'

scene bg hallway
with wipeleft_scene

'Going up the stairs was less daunting than I thought, as keeping left whilst going up seemed to have mitigated any chance of leaving god-awful black streaks against the pristine white walls.'

show monika 1d zorder 2 at t11

m'That door there is your room. The door at the very end is the bathroom.'

mc'M\'\kay.'

m'We\'\ll be heading out soon so just put away your things in your room for now, I\'\ll go get changed.'

'I give her a nod and approach my room.'

scene bg bedroom
with wipeleft_scene
stop music fadeout 2.0

'This room looks pretty \"\lived in\"\, there\'\s all sorts of books in this bookshelf, as well as a desk with a keyboard on it.'

'I take a closer look in and around the desk, it looks like there isn\'\t an actual computer there, nor a monitor or mouse.'

'Strange.'

'I put down my luggage, as well as resting my bag against the bed.'

'Having freed myself from the weight of my effects I stretch out and yawn, only to collapse onto my bed.'

'I must\'\ve lucked out or something, this bed\'\s a double.'

'Taking advantage of this fact I stretch out as much as humanly possible, feeling every single joint and tendon of my body release tension.'

'A swift and heavy bout of fatigue sets in, and I close my eyes.'

scene black
with wipedown

'...'

'Eurgh.'

'It\'\s only been a minute and I feel rejuvenated already, but I don\'\t want to get up.'

'I just wanna lay here till the sun comes down and up again.'

scene bg bedroom

'Guess I\'\ll get on my phone and doomscroll for a bit.'

'{i}No Connection.{/i}'

'Ah shit, I forgot to ask.'

'And that reminds me, I need to get a sim card too.'

'Guess I\'\ll snatch one while Monika and I are out for errands.'

'I get back up on my feet and put on my flip-flops.'

'I had my hand close enough to my room\'\s door handle that I was a fingertip\'\s length away, until it jolted open.'

'I retract my hand back so as to not get slammed by an untimely visitor.'

show monika 1bg zorder 2 at t11

play music mhouse

m'Woah! Sorry!'

show monika 1bh zorder 2 at t11

'I notice Monika\'\s change in attire, donning a faded green hoodie.'

'...'

'Is she slumming it with me?'

mc'You\'\re all good, besides I wanted to ask you for the wifi password.'

show monika 1bi zorder 2 at t11

m'Oh, right. It\'\s 1995.'

show monika 1bj zorder 2 at t11

'I pull out my phone, going to the nearest wifi network and punching in the numbers.'

mc'19, 95...'

mc'Is this a birthdate or something?'

show monika 1bi zorder 2 at t11

m'No, it\'\s when-'

stop music

show monika 1bk zorder 2 at t11

'She abruptly stops herself.'

'I notice Monika\'\s face display a slight sadness, eyes dropping down to the floor.'

'My mind conjures up the worst assumptions on what this date could possibly mean.'

'I really don\'\t want to pry into the death of a loved one.'

'Or at least, that\'\s what I think it is, I\'\d rather prepare for the worst.'

mc'It\'\s okay, you don\'\t have to tell me if you don\'\t want to.'

show monika 1bl zorder 2 at t11

m'Okay.'

show monika 1bk zorder 2 at t11

'...'

mc'{color=#9FA100}Shall we get going?{/color}'

show monika 1bk zorder 2 at thide
hide monika

'Monika, without a signal, turns around and out the door, her footsteps echoing off of the corridor walls.'

'...'

'I really hope I didn\'\t strike a nerve.'

m'{color=#9FA100}[player]! We\'\re going!{/color}'

mc'{color=#9FA100}Okay!{/color}'

'I hope to god the change in her tone means we set things straight.'

scene bg crossroadsdusk
with wipeleft_scene
play music t2b

'The sun\'\s close to setting, with it\'\s orange light casting stretched sharp shadows on every surface, beneath a warmly lit layer of clouds.'

'It\'\s radiance providing a smidgen of heat as the narrow streets funnel in wind that would chill Monika and I to the bone if it weren\'\t for our hoodies.'

show monika 1bh zorder 2 at t11

'Monika\'\s just a few metres in front of me when another breeze hits.'

'A moment passes before a thought crosses my mind.'

'Isn\'\t Monika cold?'

'I don\'\t think skirts offer much in the way of warmth, yet I saw damn near every woman wearing one in this weather.'

'How do they do it?'

'Another gust of wind barrels down to the two of us, Monika\'\s skirt going haywire.'

'I panic, briefly running ahead until I\'\m shoulder to shoulder with Monika.'

'I don\'\t have an issue being seen as reclusive or anything, but I really don\'\t want to be taken as some lecherous bastard.'

show monika 1bi zorder 2 at t11

m'...'

show monika 3ba zorder 2 at t11

m'You took a peek, didn\'\t you?'

'As much as I dislike her putting on that dumb smug smile, there\'\s at least comfort in the fact that whatever happened back at my room is water under the bridge now.'

mc'I looked away as soon as it started flapping, I swear.'

m'Hehe~ whatever you say, boy.'

'I chuckle and give Monika a slight smile, shaking my head to acknowledge her doubts.'

stop music fadeout 2.0
scene bg store
with wipeleft_scene
play music kokishin

'We soon arrive at a supermarket, its artificial light piercing my eyes as dusk approached not far behind us.'

'Centralised heating provides much needed warmth to my hands and face. Any longer outside and I could\'\ve sworn they would\'\ve rotted off.'

'I tune out everything to focus on the main reason why I came here.'

'Hmm. Anything tech-related should point me in the right direction.'

'Oh hey! A mobile phone section! There\'\s gotta be some mobile plan section somewhere.'

'I beeline over to it.'

'Bingo, helps to have \"\SIM\"\ emblazoned everywhere on a portion of your store.'

'I browse through the options, a wide range of data plans organised by length.'

'Hmm.'

'{i}One year plan.{/i}'

'This one seems like the most value for money.'

'Plus I\'\m only here for one year anyway.'

'I grab it and go over to the counter.'

scene bg counter
with wipeleft_scene

mc'{color=#9FA100}Hi.{/color}'

c'{color=#9FA100}Welcome. Is this all?{/color}'

mc'{color=#9FA100}Yeah.{/color}'

'I open my wallet and take out my card, paying for my expenses.'

c'You wouldn\'\t happen to be with her, would you?'

stop music

show monika 1bm zorder 2 at t11

'The cashier points behind me to a sight of Monika with quite a sour look on her face.'

show monika 1bm zorder 2 at thide
hide monika

mc'{color=#9FA100}...I am.{/color}'

'I am a bit startled by the cashier\'\s sudden English skills.'

'That, and the equivalent of death staring me down.'

play audio scan

'The brief beep of the card reader confirms my purchase.'

'The Cashier laughs, as if he knows I\'\m about to be in some serious trouble when I return to my acquaintance.'

c'{color=#9FA100}Never make a woman mad, kid.{/color}'

c'{color=#9FA100}Hehe, have a nice night.{/color}'

mc'...You too.'

'I walk away from the counter and towards Monika, curious as to why I\'\m about to get chewed out.'

scene bg store
with wipeleft_scene
play music mall

show monika 1bm zorder 2 at t11

mc'What\'\s up?'

show monika 1bn zorder 2 at t11

m'Well, first off, I was halfway through asking you a question, only to see you ran off, second, you\'\re my responsibility! How would it look if I just happened to lose a transfer student from another country?'

show monika 1bm zorder 2 at t11

'Oh.'

'I didn\'\t know I mattered that much.'

'I need to defuse this, Monika\'\s the last person I need to be on bad terms with.'

mc'I see.'

mc'I\'\m sorry for running off from you.'

mc'I just had to run an errand of my own. Should of mentioned that earlier so, sorry.'

'She\'\s not buying it. If disappointment was a scent then I\'\d be gasping for fresh air right now.'

'C\'\mon think.'

'...'

'I present her with the sim card I just got.'

mc'Hey, if you ever lose me, you could call me now.'

mc'You got a hairpin handy?'

show monika 1bo zorder 2 at s11

'Monika smacks her lips, an arm extending out into a pocket to retrieve a hairpin.'

stop music fadeout 2.0
play music kokishin

m'{color=#9FA100}What a pain.{/color}'

'I open my mouth only to close it again, I feared I might\'\ve said something without thinking it through.'

show monika 1bo zorder 2 at thide
hide monika

'Taking the hairpin out of her hands I poke it in the hole on the side of my phone to open the sim card tray, replacing my old one with the new one.'

'Closing the tray, I turn on my phone to configure it, noticing Monika has repositioned herself to be right by my side, peering down on my phone.'

show monika 2hb zorder 2 at t11

mc'What?'

show monika 2bi zorder 2 at t11

m'Show me your number, I wanna test if it works.'

show monika 2hb zorder 2 at t11

'I swear there\'\s gotta be 5 stages of disappointment, and Monika\'\s going through the not-so-passive aggression phase.'

'I go over to my contacts list and show her the number of my phone.'

'After a few moments of glancing back and forth from her phone to mine, my phone vibrates from an incoming call.'

mc'Sweet, so wa-'

show monika 3ba zorder 2 at h11

mc'Hey!'

'Monika tugs me by my hoodie\'\s arm, clearly in a rush to get her stuff done too.'

'She turns her head to me, a devious smile signifying a cathartic comeback to all of this.'

m'I\'\ve got plans for you, boy~'

'Ah shit.'

scene bg counter2
with wipeleft_scene 

'For the past fifteen minutes I\'\ve been lugging around groceries as some sort of repentance for my little stunt back there.'

'It isn\'\t all too bad, but if I have to go on another fifteen minutes my arms are gonna give in.'

'Monika tosses a packet of bouillon cubes into one of the shopping baskets I\'\m carrying before turning to me.'

show monika 1bh zorder 2 at t11

m'Okay! We\'\re done!'

show monika 1bg zorder 2 at t11

mc'Hallelujah.'

'How she manages a wide range of expressions and tones with a smile is beyond me.'

'Having put down the baskets, I pull out my phone, giving my arms a brief moment to stretch out.'

show monika 2eb zorder 2 at t11

m'Could you help?'

mc'In a sec, I\'\m saving your number to my contacts.'

show monika 2eb zorder 2 at thide
hide monika

'Let\'\s see here.'

'{i}Contacts{/i}'

'{i}Most Recent{/i}'

'{i}1 Missed Call - Unknown Number{/i}'

'{i}Save Contact{/i}'

'{i}Enter Contact Name{/i}'

'Hmm.'

'...'

'{i}Save Contact Name: Monker{/i}'

'{i}Saved{/i}'

stop music fadeout 2.0

'I put my phone back in my pocket and start stowing the groceries into the bags.'

scene bg crossroadsnight
with wipeleft_scene

'Monika and I start heading through the same streets as before.'

'Mercifully, the wind has died down to a few gusts here and there.'

'Would\'\ve sucked since it\'\s gotten a lot colder now, with the sun ducking well below the horizon.'

show monika 1bl zorder 2 at t11

play music t2d

m'I\'\m sorry.'

show monika 1bk zorder 2 at t11

mc'Sorry for what?'

show monika 1bl zorder 2 at t11

m'I shouldn\'\t have shouted like that at you back there.'

show monika 1bk zorder 2 at t11

mc'It\'\s fine, really.'

mc'I wasn\'\t really paying attention, I put my needs above yours which was rude to begin with.'

show monika 1bl zorder 2 at t11

m'Yeah, but...'

m'I shouldn\'\t have been angry at you as much as I did.'

m'It was...'

show monika 1bk zorder 2 at t11

mc'Unnecessary?'

show monika 1bo zorder 2 at t11

m'Yeah.'

'...'

'Aha!'

'An opening!'

show monika 1bi zorder 2 at t11

mc'Look, we\'\re both sorry, so...'

'I strain one of my arms to give Monika a shopping bag.'

mc'Let\'\s spread out the punishment, yeah?'

show monika 2eb zorder 2 at t11

'She takes the bag.'

'Sweet.'

window hide

$ renpy.music.set_volume(0.3, 1)

pause 1

call show_notification("Monika liked that.", 2.0, "Monika", 1) from _call_show_notification_4

window show

$ renpy.music.set_volume(1, 1)

'The two of us walk the rest of the way back home in a reconciled silence, the city\'\s hustle and bustle only growing in strength due to it being a friday night.'

'The occasional rustle from the bags and our footsteps being a source of solace in this quietness.'

stop music fadeout 2.0
scene bg living_room_night
with dissolve_scene_full

show monika 1bg zorder 2 at t11

m'{color=#9FA100}We\'\re home!{/color}'

show monika 1bh zorder 2 at t11

q'{color=#9FA100}Welcome back!{/color}'

'A voice I haven\'\t heard before emanates somewhere inside the house as we make our entrance, catching me a little off guard.'

'A moment later, a woman rounds the corner, jolting a little upon seeing me.'

show monika 1bh zorder 2 at t22
show harumi 2e zorder 2 at t21

q'{color=#9FA100}Oh! Hello!{/color}'

show harumi 2a zorder 2 at t21

mc'{color=#9FA100}H-Hi, good evening.{/color}'

show harumi 2e zorder 2 at t21

q'{color=#9FA100}Are you the new transfer student?{/color}'

show harumi 2a zorder 2 at t21

mc'{color=#9FA100}Yes. I assume you\'\re Ms. Starke?{/color}'

play music mhouse

show harumi 1e zorder 2 at t21

h'{color=#9FA100}Indeed, though no need to be all proper. You can call me Harumi.{/color}'

show harumi 1a zorder 2 at t21

'I give her the best reassuring smile I can, I\'\m assuming she\'\s the one that taught Monika English during her formative years.'

mc'As you wish, Harumi.'

show harumi 1h zorder 2 at t21

'Harumi shoots Monika a befuddled glance, only replying with a faint chuckle.'

'Guess I guessed wrong, whoops.'

show harumi 2e zorder 2 at t21

h'{color=#9FA100}...Anyways, I\'\ll take it from here.{/color}'

show monika 2eb zorder 2 at t22
show harumi 2a zorder 2 at t21

'Monika and I glance at each other, mirroring amused smiles between us before handing Harumi the groceries.'

show harumi 2e zorder 2 at t21

h'{color=#9FA100}Now, run along you two. It\'\ll be ready in an hour.{/color}'

show monika 1bg zorder 2 at t22

m'{color=#9FA100}Okay!{/color}'

show harumi 2e zorder 2 at thide
hide harumi
show monika 1bg zorder 2 at thide
hide monika

scene bg bedroom
with wipeleft_scene

show monika 2eb zorder 2 at t11

m'She doesn\'\t scare you, does she?'

mc'N-no! It\'\s just...'

show monika 1bh zorder 2 at t11

mc'Meeting new people that I\'\ll be interacting with for a while just gets me all anxious.'

mc'Like I have to really focus on what I do, I really don\'\t want to mess up any first impressions.'

mc'Hell I just had one with your mom back there.'

show monika 1bg zorder 2 at t11

m'Oh, it\'\s fine.'

m'She\'\s actually been really keen on having a transfer student over, ever since she heard the news you were coming.'

m'I think a part of that was having someone that regularly spoke English around the house other than Dad was a pretty good plan.'

show monika 1bh zorder 2 at t11

mc'Oh, right.'

mc'I was about to ask you about that.'

show monika 1bi zorder 2 at t11

m'On what?'

mc'On who taught you English to you.'

mc'I gotta say, you\'\re really fluent in it.'

mc'I\'\m guessing your Dad taught you?'

show monika 1bg zorder 2 at t11

m'Yeah, he did.'

show monika 1bp zorder 2 at t11

m'Well, not really.'

m'It\'\s that thing where parents talk and their kid listens and they just learn off of them while they talk.'

m'I was like that with Dad and English.'

m'It\'\s only when I was around 12 he started to teach me proper grammar and stuff.'

show monika 1bq zorder 2 at t11

mc'Huh.'

mc'And where is he now, if you don\'\t mind me asking?'

show monika 2bd zorder 2 at t11

m'Oh umm.'

m'He\'\s a diplomat for a Japanese embassy overseas.'

m'He can\'\t really come home much because of it.'

mc'What a shame.'

mc'Though I would imagine he would be downright ecstatic hearing the news of you following in his footsteps, taking up this transfer student and all.'

show monika 2bb zorder 2 at t11

m'Oh, absolutely.'

show monika 1bg zorder 2 at t11

m'Anyways.'

m'I\'\m off to take a shower, by the time you finish after me dinner should be ready.'

show monika 1bh zorder 2 at t11

mc'Alright, see ya in a bit.'

show monika 1bh zorder 2 at thide
hide monika

scene bg bedroom_night
with wipeleft_scene

'Dinner was great, some sort of onion soup with a bready crust on top.'

'We talked about the usual introductory stuff, like what I\'\ll be doing for the year, how I got here, what I\'\m supposed to do, and so on, as well as the mildly surprising fact that I am indeed a guy.'

'Though, stuff like that always leads to the \"\why\"\ of it all.'

'Why I\'\m here in the first place.'

'I gave Harumi the same bullshit cover story I give everyone, \"\language enrichment program\"\.'

'{i}Sigh{/i}'

'Though I really can\'\t complain, everyone and everything has been amazing save for a few hiccups here and there.'

'...'

'I\'\m kinda starting to like it here to be honest. A bit early for that kind of conclusion, but a strong start nonetheless.'

'I start comparing things from here to back home.'

'The thought of home reminds me something I had reserved until now.'

'I grab my phone off the bedside table, turning it away so I don\'\t get concussed by the sudden brightness when I press the power button.'

'{i}JJ{/i}'

'{i}Send Attachment{/i}'

'{i}Photos{/i}'

'There it is.'

'{i}Send 1 image?{/i}'

'{i}Sent{/i}'

'...'

'{i}Notification Settings{/i}'

'{i}Do Not Disturb: On{/i}'

'The pitch black darkness of my room doesn\'\t hide the fact that I can feel myself smiling ear to ear like an idiot.'

'I put my phone down back on the table, the case clacking against the hardwood top panel.'

'I feel myself drifting off into a deep slumber.'

'...'

'What a day.'

scene black
with dissolve_scene_full
stop music fadeout 2.0

q'Go! That\'\s the guy!'

play music akumu

'I run as fast as I possibly could, the walls either side of me a mere blur, with only what\'\s directly in front of me in full focus.'

'...'

'I think they lost sight of me.'

q'Oi!'

'Fuck\'\s sake.'

'I turn corner after corner, broadening the gap between me and whoever those guys are.'

'A familiar face presents itself just in time in my peripheral vision through a window, his figure rushing to the door I\'\m just about to pass.'

'The door opens.'

JJ'Here bro, I got you.'

'He grabs my arm and swings me inside.'

'JJ and I hide beneath some tables, hoping the angles from the outside won\'\t reveal us.'

'Broad gasps stifle my efforts to get a few words out, until I just get enough air to say what I want to say.'

mc'Thanks for the save.'

JJ'What the fuck\'\s wrong with you, bro?'

stop music fadeout 2.0

'...'

'I really can\'\t say.'

'I do nothing but stare, my panting being enough to constitute a noise complaint.'

'I\'\d love to answer him, but I can\'\t think right now.'

'I\'\m too out of breath for this.'

'I know that they know where we are.'

'Doors on both sides of the room burst open.'

scene bg bedroom

mc'Gah!'

'I\'\ve woken up in a cold sweat.'

'My face and back are all chilly because of it.'

'My heart\'\s practically pounding out of my chest.'

'I can see a little bit of the sun\'\s light refracting off some clouds and into the curtains, it hasn\'\t risen above the horizon yet.'

'It\'\s gotta be early in the morning I guess.'

'I pick up my phone to see exactly how early I\'\ve been rudely woken up.'

'{i}5:13 AM{/i}'

'Huh.'

'Six-ish hours of sleep doesn\'\t sound too bad.'

'Hmm.'

'Maybe I can get a run in before anyone else gets up.'

'Looks a little chilly out there, I\'\ll wear an extra layer under my tee before putting on a fresh pullover hoodie.'

scene bg kitchen
with wipeleft_scene
play music t2b

'I browse the local area to see if there\'\s any interesting spots I can run off to this morning.'

'Breakfast isn\'\t really much, just an apple, a mandarin and a glass of water for the cottonmouth I\'\ve gained last night.'

'I spot an interesting little place nearby, maybe ten minutes away, less if I really hoof it.'

'A park on a weekend will probably be packed but it\'\s early in the morning, there should be only a few joggers doing their rounds. Including me I guess.'

'Right, it\'\s settled.'

'I download a map for the local area, just in case.'

'I hop off one of the dining chairs and make my way to the entrance.'

stop music fadeout 2.0
scene bg park
with wipeleft_scene
play music nature

'Neither Monika or Harumi bothered giving me a spare key, so their front door\'\s unlocked.'

'Ah well, you live and you learn.'

'I\'\ve taken a seat at one of the benches in the park, sucking up the cold winter air after my little jog.'

'The sun came up while I was on my way here, unimpeded by any stray clouds and letting its warmth grace my face.'

'This park\'\s got something to it.'

'The lack of people, sunlight peeking through the tree canopies, the gentle nippy wind...'

'They all come together to give off a certain air of tranquillity that I don\'\t think I\'\ve ever experienced before.'

'I think I\'\ll rest here for a little longer.'

'...'

'Oh, another person.'

'Looks like another person out for a jog.'

'As soon as I spot this figure in the distance, the wind picks up.'

'Something I\'\ve already grown accustomed to yesterday. Doesn\'\t mean I like it though.'

'I pull my phone out, checking out any messages I may have gotten overnight before I run back home.'

'{i}Do Not Disturb: Off{/i}'

'A flurry of texts gushes out from the top of my phone screen.'

'{i}Mom - 1 Notifications{/i}'

$ phone.register_group_chat(mc_mom, "mc", "mom")
$ phone.register_message("mc_mom", "mom", _("Did you land safely?"))

label mc_mom_convo:          
    $ phone.discussion(mc_mom)

    pause 3

    $ phone.end_discussion()

'I ponder for a bit on what to say, before deciding on the most expedient approach and to just send her the photo I took at the airport.'

'{i}Send Attachment{/i}'

'{i}Photos{/i}'

'{i}Send 1 Image?{/i}'

'{i}Sent{/i}'

'Alright, next one.'

'{i}JJ - 24 Notifications{/i}'

'Holy shit.'

$ phone.register_group_chat(mc_JJ2, "mc", "JJ")
$ phone.register_message("mc_JJ2", "JJ", _("AYO BRO"))
$ phone.register_message("mc_JJ2", "JJ", _("NAH"))
$ phone.register_message("mc_JJ2", "JJ", _("{i}22 Missed Calls{/i}"))

label mc_JJ2:          
    $ phone.discussion(mc_JJ2)

    pause 4

    $ phone.end_discussion()

'Yeah, no, I don\'\t feel ready talking to him about what happened yesterday, not yet at least.'

'...'

'That jogger\'\s coming in my direction, they\'\ve got an arm outstretched in front of them.'

'Awfully strange way to jog, but I\'\m not one to get in the way of people\'\s grinds.'

'...'

'Huh?'

'{i}Monker - 1 Notification'

$ phone.register_group_chat(mc_m, "mc", "m")
$ phone.register_message("mc_m", "m", _("Where the hell did you go?"))

label monika_scolding:
    $ phone.discussion(mc_m)
    
    'Oh shit, she sent that like a minute ago.'

    $ phone.message("mc", _("Outside."))

    $ phone.message("m", _("I know that! Where exactly did you go? And why did you leave the front door unlocked?"))

    $ phone.message("mc", _("A park."))

    $ phone.message("mc", _("You didn't give me a spare key."))

    $ phone.message("mc", _("Look I know you're worried, I'll get back home right now."))

    '...'

    'The lack of messages does not bode well.'

    $ phone.message("mc", _("I won't get hurt I promise."))

    'That\'\s about as reassuring as I can get.'

    'Having a distance between Monika and I with no direct line of sight doesn\'\t shake the fact that I can practically feel her disappointment.'

    'If only there was a way to properly convey-'

    $ phone.image("m", "mod_assets/phone/emojis/eyeroll.png", time=1.0, delay=None)

    stop music fadeout 2.0

    'There we go.'

    play music chaos

    $ phone.message("m", _("Just get back here."))

    $ phone.message("mc", _("In a jiffy."))

    $ phone.end_discussion()

'I stand up from the bench, sliding my phone back into my pocket before running back the way I came at the behest of my ever so gracious host.'

'I do some stretches before getting back into the groove of it.'

'I pick up speed, not caring for anything on either side of me, there weren\'\t much people at the park to pose that much of a risk of bumping into each other anyhow.'

scene bg crossroads
with wipeleft_scene

'There\'\s an intersection in the path in front of me.'

'No time for caution.'

play sound fall
scene black
stop music

'I feel my body get hit with a sudden force to my side, toppling me over and landing on my back.'

'The impact knocks the wind out of my lungs as the pain settles in.'

mc'Argh...'

scene bg crossroads
with wipeleft_scene

'It takes me a few seconds to recompose myself and sit straight back up, my arms doing most of the lifting.'

'I notice one of my hands landing on a piece of laminated paper on the ground.'

show yuri 3bp zorder 2 at t11

'I don\'\t have a moment to analyse what it says as I look up to notice a woman staring down at me with shock in her eyes.'

'They dart between me and the laminated paper for a few seconds.'

'I stand back up, strainfully on account of the unscheduled hyper-chiropractic session.'

'She\'\s still doing it.'

'...'

'Does she want it?'

'I extend her the paper, noticing it\'\s been slightly crumpled.'

show yuri 3bo zorder 2 at t11

y'{color=#9FA100}Sorry!{/color}'

show yuri 3bo zorder 2 at thide
hide yuri

'She gives a swift bow, before running off in the completely opposite direction, long locks of lavender flowing.'

'All words escape me in this situation.'

'I\'\m left standing there with a sore back and whatever this is.'

'I inspect the laminated paper.'

'{i}KURIBAYASHI HIGH LIBRARY - HEIGHTS OF ART AND CULTURE{/i}'

'Huh, this has got to be some sort of bookmark. From my school no less.'

'I\'\ll keep it on me for now, chances are I\'\ll probably see that girl again.' #End Of Demo

'Well, I suppose this landing is fate telling me to return home.'

scene bg residential_day
with wipeleft_scene

'Nnrgh...'

'That less-than-gracious landing on the concrete is really doing a toll on my back.'

'I don\'\t think I can hide this from Monika or Harumi.'

'And I reassured Monika something specifically like this wouldn\'\t happen.'

'Go me.'

'Gonna have to suck it up and power through, I wouldn\'\t dare disobey my \"\handler\"\.'

'...'

'Eurgh.'

'That sounded weird.'

scene bg monika_house
with wipeleft_scene

'As I get closer to home, literally walking off the pain, an idea struck me.'

'What if I had more autonomy?'

'I get the feeling that Her Majesty would detest such a notion.'

'Plus I\'\m not in much of a good bargaining position, having just broken a promise of self-preservation.'

'Ah well, I\'\ll bring it up later.'

'I get to the front door, letting myself in as it\'\s still unlocked when I left this morning.'

scene bg Living_Room
with wipeleft_scene

mc'{color=#9FA100}I\'\m home!{/color}'

show harumi 2ca zorder 2 at t11

mc'Oh!'

'I abruptly stop myself as I\'\m greeted by Harumi.'

mc'{color=#9FA100}G-good morning.{/color}'

show harumi 2cg zorder 2 at t11

h'{color=#9FA100}Good morning, [player].{/color}'

show harumi 1cg zorder 2 at t11

h'{color=#9FA100}It\'\s awfully cold out there, where did you run off to?{/color}'

show harumi 1ca zorder 2 at t11

mc'{color=#9FA100}Uh, to the park.{/color}'

mc'{color=#9FA100}Sorry for leaving the front door unlocked.{/color}'

show harumi 1cd zorder 2 at t11

'I can see her doing an ocular patdown on me.'

'...'

'Shit.'

show harumi 1cl zorder 2 at t11

h'{color=#9FA100}That\'\s quite alright, Monika told me why.{/color}'

show harumi 2cp zorder 2 at t11

h'{color=#9FA100}There\'\s a spare key on the hall table for you should you need it.{/color}'

show harumi 2cl zorder 2 at t11

mc'{color=#9FA100}O-okay.{/color}'

show harumi 2cj zorder 2 at t11

mc'{color=#9FA100}Thank you, Harumi.{/color}'

show harumi 2ch zorder 2 at t11

h'{color=#9FA100}You\'\re welcome, [player].{/color}'

show harumi 1cg zorder 2 at t11

h'{color=#9FA100}If everything goes well, I\'\ll be back home around the same time as last night.{/color}'

show harumi 1cg zorder 2 at thide
hide harumi

'Harumi passes by me.'

h'{color=#9FA100}Try to be careful next time okay?{/color}'

mc'{color=#9FA100}Yes ma\'\am.{/color}'

'Oh- seriously?'

'Now my mouth\'\s moving faster than my brain.'

'Harumi shuts the front door, her silhouette gravitating towards the car.'

mc'{i}sigh{/i}'

'I turn around back to a familiar sight.'

show monika 2h zorder 2 at t11

'A disgruntled Monika.'

'Yeah, no running from this one.'

mc'You\'\re right, she does scare me.'

show monika 2i zorder 2 at t11

m'Mmm, maybe it\'\ll teach you to know your place.'

show monika 2h zorder 2 at t11

mc'What, house arrest?'

show monika 1i zorder 2 at h11

m'Hey!'

show monika 1h zorder 2 at t11

mc'I\'\m sorry Monika, but that\'\s what it kinda feels like.'

mc'I appreciate you looking out for me and all, but having me all cooped up is a bit much.'

show monika 3i zorder 2 at t11

m'Right, right, and what\'\s this about you being more careful next time?'

mc'Oh, umm...'

mc'That was...'

show monika 1q zorder 2 at t11

mc'Yeahhhh.'

show monika 1r zorder 2 at t11


m'Honestly [player]? I just wished you would\'\ve told me beforehand where you were going before you left.'

m'That way I could have dragged you all the way back home myself.'

show monika 2p zorder 2 at t11

m'But in the meantime, stay in the house, okay? I can tell you\'\re hurting from here.'

show monika 2o zorder 2 at t11

'As soon as she mentions it, the dull pain in my back grows a little more.'

'Mmh, fair.'

scene bg bedroom
with wipeleft_scene

'I spent the better part of the day on my laptop after getting the last bits of my stuff in their places.'

'The rest of my clothes, electronics, gizmos and doohickeys, and so on.'

'I\'\m on my bed halfway through a season of some dated sci-fi show I pirated, trying to ease the pain.'

'...'

'Man, in retrospect this is some really thinly veiled propaganda, these guys always seem to be in the right.'

'I\'\m interrupted from my train of thought as I get a notification from JJ.'

play music mhouse

JJ'yo'

JJ'wanna play?'

mc'sure'

mc'i aint got anything better to do'

JJ'aight'

JJ'hop in vc'

'...'

'{i}da-ding{/i}'

'{i}da-ding{/i}'

'{i}Connected{/i}'

mc'Good evening.'

JJ'Sup cuz.'

JJ'You wanna tell me about what\'\ going on with those girls bud?'

mc'Ah shit.'

mc'Dude, I\'\m gonna say it and gonna keep saying it.'

mc'They\'\re complete strangers, we don\'\t even speak the same language!'

JJ'Bruv you\'\re gonna be hanging out with them day after day, they won\'\t be strangers for long.'

'Hmm, he\'\s got a point but I\'\m not gonna concede and give him ground.'

JJ'And they\'\re even your age! You won\'\t have to fumble like you did with Ms. Van de Kaap.'

mc'Oh fuck off dude!'

JJ'Hahaha!'

mc'Never speak of that absolute withering prune of a teacher! Ever!'

mc'Look man, can we just play? I\'\ve been bored out of my mind for the past few hours.'

JJ'Aight fam, settle.'

scene bg bedroom_night
with wipeleft_scene

JJ'Aight I got that one.'

mc'Okay, the other one\'\s glued to me, you got this.'

JJ'Yeah coming.'

'...'

JJ'I\'\m on him.'

mc'Hurry dude, he\'\s about to blow me.'

JJ'Yeah yeah just wait.'

mc'Dude-'

mc'Come!'

JJ'I\'\m already there!'

'A few tense seconds pass, hearing the last enemy jet howl closer and closer.'

'Just as the bandit\'\s about to get a missile off, JJ lets loose a burst of cannon fire, blowing up the assailant.'

'The game ends, with JJ\'\s plane and mine flying in formation, touting the victors of this match.'

mc'Let\'\s fucking goooo!'

JJ'Whew! That was insane!'

JJ'Bro I\'\m almost out of storage, I recorded the whole thing.'

mc'Really? Fuck yeah.'

JJ'Oh man, what a dub.'

mc'With that I gotta call it, I don\'\t wanna end tonight on a loss.'

JJ'Aight bud catch ya later.'

JJ'Wait, shit, actually...'

'JJ turns on his webcam feed, prompting me to do the same.'

'He\'\s out of view, with his upper torso leaning aggressively to grab something that\'\s far from where he\'\s sitting.'

'He returns with a CD in hand, text written in black sharpie on the cover side unintelligible from the camera not being in focus.'

mc'Eurgh.'

JJ'What?'

mc'Did you always look like that?'

JJ'Like what?'

mc'Nevermind.'

JJ'...'

'He furrows his eyebrows and squints.'

JJ'What the fuck?'

JJ'Are you in bed right now?'

mc'Yeah, fucked up my back this morning, its been sore ever since.'

JJ'Cuz, not one week and you\'\ve already fucked yourself.'

mc'Old habits die hard.'

JJ'Bruv, you\'\re gonna die hard at that rate.'

'I roll my eyes at him.'

mc'Whatever.'

stop music fadeout 2.0

'JJ then presents the CD, front and center in the camera\'\s view.'

JJ'Do you know what this says? You speak Japanese, yeah?'

mc'I can speak it for sure, reading though? Not so much.'

mc'Bring it closer.'

'The camera now autofocuses on the CD, the text now being more readable.'

'I take a screenshot of JJ\'\s camera feed.'

mc'You can stop holding it now.'

'The text is mostly a mish-mash of kanji, with only a few bits of hiragana here and there.'

'The only kanji I know in there is \"\god\"\ but everything else is a wash.'

JJ'What does it say?'

mc'No clue dude, it might as well be Chinese.'

JJ'Oh shit, so it is Japanese.'

mc'Yeah.'

mc'Where the fuck did you find that?'

JJ'It was on the ground on the way to school.'

'...'

'I\'\m so glad we\'\re video-chatting, I can convey so much more emotions through facial expressions.'

'I call this one \"\Unbridled Disappointment\"\.'

JJ'What?'

mc'Has no one taught you not to put random CD\'\s and USB\'\s you found on the ground somewhere into your PC?'

JJ'Chill, cuz.'

JJ'I\'\m smarter than that.'

mc'Uh huh.'

JJ'But I really wanna see what\'\s on it.'

mc'And?'

mc'What do you want me to do?'

JJ'I dunno bruv, gimme a solution.'

mc'Dude, have you ever heard about curiosity killing the cat?'

JJ'Bro it can\'\t be that bad.'

'I am not going to convince this man to not look at it.'

mc'Ugh, alright. Lemme think.'

mc'Does the school library PCs have CD readers?'

JJ'Pretty sure, they haven\'\t updated their shit since the 2000s.'

mc'Ah, Sticky Sarah.'

JJ'Yeahh cuz, Sticky Sarah.'

mc'Alright if you\'\re still curious you should open it there.'

mc'But if it starts making the PC all sentient and shit with malware and viruses, hold down the power button \'\till it shuts off and walk away.'

mc'Remember what happened during the sports carnival?'

JJ'No?'

mc'Remember when that marquee fell on top of pretty much all of the heads of the upper management of the school?'

mc'When you were fucking with it too much?'

JJ'Ohhh shit, yeah.'

mc'Remember what I said to them to bail you out?'

JJ'Yeah, yeah.'

JJ'It was like that when I got here.'

mc'If some shit goes down with the PC and someone catches you making a break for it just say those magic words.'

'The door to my room slowly opens, with Monika\'\s head slowly poking out of it.'

show monika 1j zorder 2 at t11

mc'Oh, hey Monika.'

show monika 1i zorder 2 at t11

JJ'Da fuck? Who\'\s Monika?'

mc'My parole officer, apparently.'

show monika 1m zorder 2 at t11

'I see her pout from across the room.'

show monika 1n zorder 2 at t11

m'I heard some.... suspicious things and I was curious.'

show monika 1m zorder 2 at t11

mc'You did?'

show monika 2b zorder 2 at t11

m'Yes.'

show monika 5a zorder 2 at t11

m'First off, what\'\s this about someone blowing you? And who\'\s Sarah?'

'...'

mc'That\'\s need-to-know.'

show monika 2d zorder 2 at t11

mc'Wanna say hi to the guy who apparently has a higher body count than Stalin?'

show monika 1a zorder 2 at t11

'Monika makes her way over to me, getting on the bed and sitting next to me against the headboard.'

'I pull out my headphones from the jack so the both of us can hear JJ, and I make sure she\'\s in frame too.'

play music mhouse

show monika 1b zorder 2 at t11

m'Hi! My name\'\s Monika!'

show monika 2b zorder 2 at t11

m'I\'\ll be hosting [player] until December.'

show monika 2a zorder 2 at t11

JJ'Uh, hi...'

JJ'M-my name\'\s Jadu.'

'Oh my god, he\'\s red as a tomato.'

mc'Jadu?'

JJ'J-Jamshidi.'

'I can\'\t stop grinning like an idiot.'

JJ'Shut up!'

show monika 2e zorder 2 at t11

mc'What? I didn\'\t say anything!'

show monika 2j zorder 2 at t11

'Me and Monika share a laugh at his expense.'

show monika 2a zorder 2 at t11

mc'Hey JJ, this is a perfect opportunity to practise some of that Japanese you\'\ve learnt in anime.'

mc'Try introducing yourself.'

JJ'{color=#9FA100}Good morning.{/color}'

JJ'{color=#9FA100}M-My name is Jadu.{/color}'

JJ'{color=#9FA100}Nice to meet you.{/color}'

show monika 2e zorder 2 at t11

'My smile\'\s still plastered on from all the embarrassment coming through the screen.'

show monika 4k zorder 2 at t11

m'Huhu~ very good!'

show monika 4m zorder 2 at t11

mc'Mmm, very good, very good.'

mc'You\'\re almost naturalised, JJ.'

JJ'Really?'

mc'No.'

JJ'Damn.'

show monika 4m zorder 2 at thide
hide monika

'A moment passes, with JJ staring into his screen, eyes darting left and right getting a good look at me and Monika.'

JJ'So lemme get this straight.'

JJ'You, right now, are living with Monika.'

mc'Yep.'

JJ'And the school\'\s just fine with this?'

mc'Why wouldn\'\t they be?'

JJ'Bro come on.'

mc'I seriously don\'\t know what you\'\re on about.'

'I totally know what he\'\s on about.'

JJ'Bro pleeeease.'

mc'Please what? I can\'\t just ask them for another host.'

mc'They\'\ve dug their heels on this one, you and I should know how \"\final\"\ our school is on these things.'

mc'Besides, this place is actually pretty nice.'

mc'Way better than home.'

JJ'That\'\s not saying much.'

mc'Yeah, I know.'

mc'There\'\s parents around this time at least.'

mc'Well... parent.'

JJ'Nice, they\'\re good to you?'

mc'Yeah, yeah, a little on the scary side though.'

JJ'...Like Van de Kaap?'

mc'I thought we reached an agreement never to speak of her, but yeah.'

mc'It\'\s a little less scary \'\cause she\'\s-'

'No.'

show monika 1d zorder 2 at t11

'You are not about to call Harumi hot while Monika\'\s right next to you.'

show monika 1d zorder 2 at thide
hide monika

mc'Uhhh.'

JJ'She\'\s what?'

JJ'Also, I don\'\t remember agreeing to shit, bruv.'

JJ'Not until you save me one.'

mc'{i}sigh{/i} This fucking guy.'

mc'Anyways-'

mc'I dunno about you, but it\'\s getting late over here.'

JJ'Oh, word.'

JJ'I was getting ready for school.'

JJ'This was cooked.'

mc'Sure was.'

JJ'I\'\ll message you whenever I\'\m free if you\'\re down to play again.'

mc'Alright, I\'\ll let you know.'

mc'See ya.'

JJ'See ya.'

'{i}beep{/i}'

'I keep my eyes on the screen.'

show monika 1d zorder 2 at t11

mc'Ooooooh~ he liked you~'

'I shut my laptop down and close the lid, setting it aside.'

show monika 2e zorder 2 at t11

m'W-what?'

mc'Kidding, kidding.'

show monika 2m zorder 2 at t11

mc'He gets flustered whenever a girl talks to him is all.'

mc'Wish it weren\'\t the case though, poor guy.'

show monika 1n zorder 2 at t11

m'Sounds more like you, really.'

show monika 1m zorder 2 at t11

'I turn and give Monika an eyebrow, only to realise how close we\'\ve gotten.'

'My face grows hotter.'

mc'Woah!'

'I recoil away from her, getting off the bed to get a good distance away from her.'

'Now I get why JJ asked me that.'

'Never getting in the same bed as Monika, that shit almost killed me.'

show monika 1j zorder 2 at t11

m'Hehe~'

show monika 3b zorder 2 at t11

m'I was going to ask you if your back\'\s fine to walk tomorrow, but it looks like that answers that.'

show monika 1a zorder 2 at t11

'I stretch out, having just laid bed-ridden for the last several hours.'

mc'Mmh, oh that\'\s good.'

mc'Still kinda there, but I should be fine in the morning.'

mc'Why\'\d you ask?'

show monika 2b zorder 2 at t11

m'I\'\m going to the mall to meet up with Natsuki and Sayori.'

show monika 2a zorder 2 at t11

mc'And you want me to tag along so I don\'\t go running off without you knowing?'

show monika 2n zorder 2 at t11

'Monika ponders this for a fleeting moment.'

show monika 5a zorder 2 at t11

m'Yes.'

m'Fool me once, shame on you.'

m'Fool me twice, shame on me.'

show monika 4d zorder 2 at t11

m'Fool me three times, I\'\m uh...'

mc'?'

show monika 4n zorder 2 at t11

m'... A dumbass?'

'Monika and I laugh.'

'Hearing her swear in English just cracks me up for some reason.'

mc'I guess it would.'

show monika 1a zorder 2 at t11

'Monika glances back and forth from my laptop to me.'

show monika 1b zorder 2 at t11

m'So do you have any other hobbies other than gaming and shouting your lungs out?'

mc'Hey!'

show monika 1e zorder 2 at t11

m'{i}snrrk{/i}'

'My brain does a hard reset as I just proved her point.'

show monika 1a zorder 2 at t11

mc'I\'\ll have you know, my other hobbies include tinkering with electronics, snooping around and... arts & \"\crafts\"\.'

show monika 2b zorder 2 at t11

m'Oh? Like making posters and decorations?'

show monika 2d zorder 2 at t11

mc'Oh, nah, just making... things...'

mc'But I could make a few paper cranes if need be.'

show monika 2m zorder 2 at t11

m'Hmm.'

show monika 2n zorder 2 at t11

m'You\'\ll definitely help during the festival.'

show monika 2m zorder 2 at t11

mc'Is that an observation or a demand?'

show monika 5a zorder 2 at t11

m'I don\'\t know, which do you prefer?'

mc'Heh.'

show monika 1a zorder 2 at h11

'Monika gets up from the bed, dusting herself off.'

'...'

'I\'\m not that crusty, am I?'

show monika 3b zorder 2 at t11

m'Well, whatever skills you may have, I\'\m sure they\'\ll be a big help for us.'

show monika 1a zorder 2 at t11

mc'Mmm, here\'\s hoping.'

mc'You mentioned a festival? What does that entail?'

show monika 4b zorder 2 at t11

m'It\'\s where all the clubs show what they do, it\'\s to help get new members.'

show monika 4p zorder 2 at t11

m'We had one last year but...'

show monika 4o zorder 2 at t11

mc'It didn\'\t work out too well?'

m'Mhm.'

show monika 4n zorder 2 at t11

m'Still, I do want to host another event, though I doubt the others would want to.'

m'I don\'\t want to repeat the same mistakes.'

show monika 4e zorder 2 at t11

m'I\'\m hoping there\'\s something you could do so we don\'\t.'

'Now that the club\'\s been brought up I feel like I\'\m a little out of my depth in terms of selling the concept to other students.'

show monika 1e zorder 2 at t11

mc'We\'\ll see.'

'I decide to get back at Monika for spooking me just then.'

show monika 1d zorder 2 at t11

mc'Now, unless you\'\re planning to get changed inside my room and sleeping with me, the door\'\s right behind you.'

'Yeah, that\'\s right, blush.'

show monika 1l zorder 2 at t11

m'Oh! Right.'

show monika 1n zorder 2 at t11

m'Goodnight, [player].'

show monika 1m zorder 2 at t11

mc'\'\Night. Turn off the lights on your way out, please.'

#find a nighttime lights-on BG. 

show monika 1m zorder 2 at thide
hide monika

'*click*'

mc'Thank you.'

stop music fadeout 2.0

'I lay back down on my bed, pulling the covers over me.'

'...'

'Man, I\'\ve been up since 5.'

'I haven\'\t done much today.'

'I still haven\'\t convinced Monika to let me off the hook.'

'Wonder if sucking up to her would be the call here.'

'I\'\ll put together a proposition, my obedience for the day for my emancipation.'

'Sounds... foolproof...'

'I let the fatigue sink me deeper to sleep.'

scene black
with dissolve_scene_full
play music yume

'...'

'Kara and JJ are off a good 10 metres away from me, trowels picking clumps of earth away to fashion our makeshift defilade.'

k'Hey [player], is this deep enough?'

'Her outside voice echoes off of the trees around us.'

mc'You think it can fit all three of us in there?'

'I hear a racket of jackets ruffling against each other and dirt being readjusted.'

k'Yeah, looks like it.'

mc'Alright if you\'\re ready, then I\'\m ready, just about finished up here too.'

'I do up the last connections to ground on the screw terminals, my fingers working at a reduced pace on account of the cold weather.'

'I double check every single component before flipping the arming switch.'

mc'WE ARE LIVE!'

'I excitedly jog back to the mini trench, gingerly holding the detonator.'

'I jump in the space between Kara and JJ, lining the opposite sides of the trench.'

'The earthy smell of the soil fills my sinuses.'

'I give them both a look of unadulterated giddyness before holding the detonator with both hands.'

'JJ\'\s somewhat neutral, but Kara is all clumped up like a pillbug with her fingers in her ears.'

mc'Fire in the hole!'

'JJ quickly mimics Kara, hands quickly going to the sides of his head.'

'{i}*click click*{/i}'

'The boom from my little weaponized milk carton envelops the entirety of my body and my hearing, a clear thump reverberating in my chest.'

'Tree canopies in our immediate surroundings rustle as the shockwave travels out in the forest we conducted our little experiment in.'

'Everything goes quiet due to my temporary bout of deafness, adding to the eerie atmosphere that the fog helped set up.'

'All three of us arise from the trench to inspect what my bomb did.'

'It did little to nothing, just a small pancake-sized crater on the ground, with all the leaves around it swept away from the source of the explosion.'

'I pat myself down, in case there were any stray bits of shrapnel or wood that may have grazed me anywhere.'

mc'You guys good? Did you get hit anywhere?'

'I can only hear the bassy parts of my voice, listening to everything else is like trying to hear through some thick pillows.'

'I see Kara and JJ check themselves before saying some things to me, reassuring nods are given out to clear up any misunderstandings.'

'The both of them continue to converse with each other, the tone of their voices carry a hint of panic.'

'I guess it\'\s about the ensuing police response, but I\'\m not too concerned with that.'

'I spot a white bit of shrapnel embedded in the trunk of a nearby tree.'

'Getting a closer look I soon find out it\'\s a piece of plastic from the milk carton that was a thing a minute ago.'

'I pull out the piece of plastic, surprised by the amount of force needed to pull it out.'

'Inspecting it, I notice Kara sweeping the blast site, with JJ putting the dirt pile defilade back in the trench.'

show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg" #You can change this sound if you want
pause 0.25
hide screen tear

mc'{sc=3}I catch a glimpse of her pointing upwards, not even\n a chance shows itself for me to look up as I\'\m hit\n in the back of the head from a falling branch.{/sc}'

mc'{sc=4}I\'\m knocked out to the ground, feeling the thumps\n of someone coming to my aid.{/sc}'

mc'{sc=5}I can hear it\'\s Kara, and I can hear her calling out\n my name.{/sc}'

mc'{sc=6}She grabs hold of my upper arm.{/sc}'

mc'{sc=7}Shaking me won\'\t make me any less knocked out.{/sc}'

k'{sc=8}[player]?{/sc}'

k'{sc=10}{color=#ff0000}[player]?!{/sc}'

show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg" #You can change this sound if you want
pause 0.25
hide screen tear

m'[player]!'

m'Wake up, sleepyhead.'

stop music fadeout 3.0
$ pause(1)

define wipeup_fast = CropMove(0.33333, "wipeup")
define wipedown_fast = CropMove(0.33333, "wipedown")
define fade_scene_transition = Fade(2, 3.5, 2, color="#000")

"Monika relentlessly shakes me awake until I give a sign of consciousness."

mc "{i}Mmmh.{/i}"

"I groggily try to attain full alertness, but everything's too comfortable and cosy."

scene bg bedroom with eye_open
scene black with eye_shut

"I try opening my eyes only for them to fall shut again."

"Maybe I'll wake up one sense at a time, starting with hearing."

mc "Sleepyhead?"

mc "Who taught you that one?"

m "Natsuki did."

m "She made me watch an anime in English dubs so I'd understand the plot more."

mc "Well did you?"

m "No, not really. I still didn't like it."

"I scoff at the thought of Monika watching anime."

m "Now get up, we have a large day ahead."

mc "That...{w=0.33} sounds weird."

mc "Its usually a \"big\" day, or a \"long\" day ahead of us."

m "{i}Hmm{/i}. I see."

m "Still, you gotta get up, I gotta look after you all day today."

mc "{i}Mmmm, but bed soft and warm...{/i}"

mc "{i}World...{w=0.33} hard and cold...{/i}"

m "Well, we wouldn't have nice things if we didn't put up with life, [player]."

m "Now..."

"Monika yanks away my blanket, the freezing cold soon enveloping my body."

"I shiver a little, trying to yank back the blanket before it retreats further in Monika's cruel control."

"If touch wasn't already awake it sure as hell is now."

m "Wake up, breakfast is ready."

mc "Oh damn, that's all you had to say!"

show bg bedroom
with eye_open

show monika 7a at t11 # pyjamas sprite 

"I turn to my other side to see Monika in her pyjamas."

mc "Oh."

"Aaaand sight is online."

mc "Morning."

show monika 7b at t11

m "Good morning~"

show monika 7c at t11

m "Shall we?"

show monika 7d at t11

mc "After you."

"I follow Monika downstairs."

show monika at thide
hide monika 
window hide(dissolve)
$ pause(0.5)
scene bg kitchen with fade_scene_transition
play music mhouse
$ pause(2.0)

"Walking into the kitchen I'm soon greeted with a smell that's been too long since I've last smelled it."

"One more down, taste is the last one to go."

mc "Are those..."

mc "Oh man, pancakes?"

show monika 7e at t11

m "Yep!"

show monika 7f at t11

mc "I was under the impression that you hated me for yesterday."

mc "..."

mc "And sorta the day before, essentially ever since I stepped foot outside the airport."

show monika 7g at t11

mc "What's with the sudden niceties?"

m 7h "Well..."

show monika 7i at s11

"Monika and I take seats across from each other, a stack of pancakes atop our plates flanked with a glass & cutlery with a carton of orange juice between us."

m 7j "I was hoping to convince you that being in my company would be just as good as being alone."

show monika 7i

"I raise an eyebrow."

mc "What do you mean by that?"

window hide(dissolve)
$ pause(1)
show monika 7k
$ pause(1)
window show(dissolve)
$ pause(0.3)

m 7l "I don't really understand why you run off and do your own things [player], but I hope I can convince you that sometimes staying isn't so bad."

m "Looking back, I sort of had a realization last night that I really shouldn't treat you as another burden like everything else I deal with."

m "Like another task."
 
show monika 7k

mc "Huh."

window hide(dissolve)
show monika 7m
$ pause(1)
window show(dissolve)
$ pause(0.3)

m 7n "You're another person with likes and dislikes, and experiences just as unique as everybody else."

m "I may have overreacted when you got hurt, sure, but when you came back I was more than sure I could trust you."

window hide(dissolve)
show monika 7i
$ pause(1)
window show(dissolve)
$ pause(0.3)

m 7j "But, for some peace-of-mind, please stick around, for today at least."

show monika 7i

"Monika props up her elbows on the tabletop, resting her chin on her fingers."

m 7o "You might get something good out of it, after all~"

show monika 7a

"I look down to the waiting heavenly pile of carbs and sugar on my plate and grab my fork & knife."

mc "I sure did get something good out of it, and it ain't getting any warmer."

show monika 7p

m "{i}Huhu~{/i}"

window hide(dissolve)
show monika 7q
$ pause(1)
window show(dissolve)
$ pause(0.3)

m 7e "{color=#9FA100}{i}Itadakimasu.{/i}{/color}"

show monika 7a

mc "{color=#9FA100}{i}Itadakimasu.{/i}{/color}"

"Monika and I dig in."

window hide(dissolve)
$ pause(0.35)
stop music fadeout 1
$ pause(1)
scene black with dissolve
scene bg kitchen with wipeleft

"That's all of the five senses checked for the morning, saving the best for last it seems."

"I've been mulling over what Monika said earlier."

"If this is my one chance to finally get my freedom, this is it."

"Thing is, I'm not sure if I can even trust myself not wandering off today."

"It's a mall.{w=0.33} So much to do, so much to see."

"{i}Ugh{/i}, why am I like this?"

show monika 7r at t11

m "[player]?"

show monika 7s

"Maybe I can have one of Monika's friends keep watch of me?"

m 7t "Is everything okay?"

show monika 7s

"Sayori seems nice but Natsuki..."

show monika 7u

"I feel like she hates or dislikes me for some reason."

show monika 7v at h11

m "[player]!"

show monika 7s

mc "Y-yeah?"

m 7t "You were staring at your plate for a bit, are you okay?"

show monika 7s

"I reconnect with my senses to see an empty plate with smears of syrup."

show monika 7n

mc "Yeah, I'm good."

mc "Just...{w=0.33} thinking about things."

m 7w "What were you thinking about?"

play music t2d

$ pause(1.5)

mc "About Natsuki."

show monika 7x 

mc "Do you think she doesn't enjoy my company?"

show monika 7i

m "Oh, Natsuki."

m "She may seem unfriendly to new people,{w=1} especially boys."

m 7o "But I'm sure she'll warm up to you."

show monika 7a

mc "I see."

mc "Wait,{w=0.33} why boys in particular?"

show monika 7s

mc "I'm guessing she's had bad experiences with them?"

m 7y "Y-yeah,{w=0.33} you could say that..."

mc "More stuff you'd rather not say?"

show monika 7z

"Monika nods."

mc "It's okay."

m 7b "From what I've seen so far though,{w=0.5} Natsuki and you seem to get along."

show monika 7a

"I decide against correcting her English."

m 7ab "Which hopefully will be the case, because I would hate it if you haven't even gone to your first club meeting and already hate one of its members."

show monika 7a

mc "Yeah, I guess that would suck."

show monika 7n

mc "I'll try to be...{w=0.33} accommodating? If that's the right word."

m 7r "{i}Accommodating{/i}? What does that mean?"

mc "{i}Pfff{/i}, I dunno."

"I stand up from my chair with glass and plate in hand."

"I make my way to the sink to wash them off, when I'm interrupted by Monika's arm."

show monika 7b

m "Let me do it for you."

show monika 7a

mc "Ah,{w=0.33} thanks."

show monika 7a at thide
hide monika

"What a gracious host."

"I make my way upstairs to my room to get ready."

stop music fadeout 2.0
scene bg bedroom with fade_scene_transition

"I'm halfway through putting on my hoodie when I hear my phone vibrate against the tabletop."

"I look at the notification."

"{i}JJ - Sent Image Attachment{/i}"

"Looks like he went through with checking out the CD."

"I zoom into the photo as the quality of the photo has drastically been reduced due to JJ taking a photo of the screen itself."

"Skimming through what's on screen I notice it's mostly just text with a few images here and there, probably showcasing the rooms they're displaying."

"I'm interrupted by a series of knocks from my bedroom door."

m "[player]! Are you ready?"

mc "Yeah, one sec."

"I put my phone and wallet into my pockets and head out the door."

scene black with Dissolve(2, alpha=False)
scene bg residential_winter with wipeleft_scene
play music t2b

"Would you look at that?"

"Seems like it actually snowed a little bit last night."

"Luckily I put on my signature black hoodie, as JJ would call it."

"In fact, JJ actually lent this one to me."

"..."

"Hence why he calls it a signature."

"My train of thought is derailed by Monika."

show monika 6bb at t11

m "Are you excited for your first day of school tomorrow?"

show monika 6ab

mc "Ehh, kinda."

show monika 6cb

mc "More of a mix of excitement and anxiousness."

mc "But I'm also feeling kinda underwhelmed by it too."

m 6db "Hmm?{w=0.33} Underwhelmed?"

show monika 6cb

mc "I mean, it's just school isn't it?{w=0.33} I've been doing it for years now."

mc "I get that it's in a completely different country with a radically different structure, culture and time frame, but, in essence, it's all the same isn't it?"

m 6d "Huh, when you look at it like that I can see where you're coming from."

show monika 6c

mc "Oh, and speaking of the time frame, I thought Japanese schools would start off way later in the year?"

m 6b "Oh, right, about that."

m 6bc "Kuribayashi High starts off from late January to December."

m "It's to get in line with all of the other sister schools we're partnered with."

m 6jc "St. Hewlett's College isn't the only sister school of Kuribayashi High, so there's a big chance that there will be other transfer students like you."

show monika 6a

mc "Huh, interesting."

show monika 6a at thide
hide monika

"The thought of some other person that also understands English to a native level at my school brings an odd comfort."

"Not to discredit Monika's proficiency in English,{w=0.5} but talking to her just has that one extra added layer."

"A language barrier that's practically not there, but it shows itself whenever I have to get really complex thoughts across."

"Something that I really don't have to worry about when I talk to JJ or Mom."

"That being said, I hope I don't find myself taking Monika's understanding of the English language for granted."

"Especially when she's essentially self taught as far as I know, on top of her English-related material in school and her father's extracurricular lessons."

"..."

"I wonder how a meeting between Monika's father and I will go."

"Going off of what Monika's father's occupation is, as well as what I've heard from what Monika said from the night I got here, I think Monika's father is pretty much a native speaker."

"Gotta count my blessings here, because if I eventually do meet him I won't have to faff around a language barrier."

"Especially when I've gotta explain what my relationship is with his daughter when I'm pretty much living with her until the end of the year."

"I'm sure it'll be fine but I can't help being a little anxious, I guess I'll ask Monika when he'll return so I can mentally prepare myself."

show monika 6a at t11

mc "Hey Monika, do you know when your father will come back to visit?"

m 6c "Hmm?"

m 6d "Oh,{w=0.33} he usually comes back for a month in..."

m 6db "June?"

m "Why do you ask?"

show monika 6c

mc "Well, I've been thinking about how your father would react when the transfer student that his daughter was assigned to is a guy."

mc "I get the feeling that it'll go well, but I also suspect that he won't be entirely keen on me living with you."

m 6l "Oh..."

m 6n "About that..."

show monika 6m

"Monika's sudden change in demeanour doesn't really give off any winning cues."

"I think I've found my answer."

m 6n "Let's just say that the phone call my Mom had with him, she only referred to you with 'they' and 'them'."

show monika 6m

"Yeah."

"Not good."

window hide(dissolve)
show monika 6r at s11
$ pause(0.75)
show monika 6q at t11
$ pause(0.75)
show monika 6eb 
window show(dissolve)
$ pause(0.3)

"Monika huffs and loosens up a bit."

scene bg crossroads_winter
with wipeleft_scene

show monika 6db at t11

m 6db "And what about your Dad?{w=0.33} Is he okay with you going overseas for school?"

show monika 6cb

mc "Oh him?{w=0.33} I'm fairly certain he would be fine with it."

mc "Any time I would go out he'd always tell me to, at the very least, 'not end up in the news, hospital or prison'. and to not 'add or subtract to the population'."

show monika 6e

mc "Though, I can't really confirm how he feels about it since I can't really talk to him anymore."

show monika 6f at h11
$ pause(0.33)
show monika 6gb at t11

m "Oh! I'm...{w=0.33} sorry to hear that."

show monika 6o

"I catch a whiff of sorrow from Monika,{w=0.33} turning to her and seeing her a little downcast."

show monika 6f

mc "Oh no no no, he hasn't passed away, he's just..."

mc "Umm..."

"Oh boy, how do I tell her?"

"How do I tell her the truth without her knowing?"

"..."

"I got it!"

mc "My Dad's...{w=0.5} incarcerated."

m 6d "Incarcerated?{w=0.33} What does that mean?{w=1}{nw}"

show monika 6c at t11
$ pause(1)
show monika 6c at t31
show natsuki 6a at t32
show sayori 6a at t33

mc "{color=#9FA100}Natsuki! Sayori!{/color}"

"A pair of vibrantly coloured heads of hair reveal themselves as soon as Monika and I turn a corner."

"What impeccable timing."

"The pair turn to face us, as I outstretch an arm in the air and wave as the distance closes."

mc "Sup."

show sayori 6rb at h33

s "{color=#9FA100}Hey [player]!{/color}"

show sayori 6ab at t33

n 6dc "{color=#9FA100}Yo.{/color}"

show natsuki 6ac at t32

m 6bb "{color=#9FA100}Good morning you two!{/color}"

show monika 6ab

s 6xd "{color=#9FA100}Monika! Good news!{/color}"

show monika 6e

s "{color=#9FA100}Guess who's back!{/color}"

show sayori 6ad

m 6db "{color=#9FA100}Hmm? Who's back?{/color}"

show monika 6c

s 6xd "{color=#9FA100}Mr. Tucks!{/color}"

s "{color=#9FA100}He's back in town!{/color}"

show sayori 6ab

show natsuki 6a at t32

m 6jb  "{color=#9FA100}Oh? Really?{/color}"

s 6rd "Yeah!{w=0.33} We saw him under a bridge just eating grass while we were coming over to the mall."

show sayori 6ab
show monika 6a

"...?"

"Is Mr. Tucks some famous local bum or something?"

s 6gc "{color=#9FA100}When we got closer though he got scared and ran away.{/color}"

s "{color=#9FA100}We were following him and then you two caught up to us.{/color}"

show sayori 6db
show monika 6r at s31
show monika 6r at t31

m "{color=#9FA100}Hmm.{/color}"

m 6b "{color=#9FA100}Sounds like we're in for some good luck to the start of this year.{/color}"

n 6lb "{color=#9FA100}Heh, only for us though, you and your boyfriend still haven't caught up with him.{/color}"

scene bg crossroads_winter

show sayori 6md at h33
show monika 6m at t31
show natsuki 6jb at t32

$ notebook_enabled = True

"Monika promptly blushes while I throw Natsuki a malicious eyebrow."

show sayori 6lb at t33

mc "Wanna run that by me again?"

n 6mc "{color=#9FA100}Uhh,{w=0.33} what?{/color}"

mc "{color=#9FA100}You know I can understand you right?{/color}"

show sayori 6bb
show monika 6c

n 6zd "{color=#9FA100}Heheh,{w=0.33} that's why I said it.{/color}"

n 6yb "{color=#9FA100}But if you're going to bug me in English you can forget it.{/color}"

mc "Is that so..."

show natsuki 6kd

"I stick my tongue out, a universal sign meaning 'get lost', or at least, I think it is."

show monika 6e
show sayori 6d
show natsuki 6hc

"My conclusion about my universal dismissive gesture seems to be corroborated by Natsuki following suit."

n 6zd "{color=#9FA100}Blehhh.{/color}"

show natsuki 6ac

mc "Blehhh."

show monika 6j
show sayori 6ac

"My little quarrel with Natsuki gets a few laughs out of the administrative heads of the literature club."

"Still, I gotta know if we're gonna run into this elusive 'Mr. Tucks'. I ain't fixin' to get stabbed by a free ranging homeless guy."

"I know the type extremely well, I just know some shit's gonna go down if we see him." #switch to winter city bg?

mc "{color=#9FA100}Sayori,{w=0.33} you saw this Mr. Tucks when you were walking over here?{w} Are we gonna see him again?{/color}"

show monika 6a

s 6xb "{color=#9FA100}Probably, he ran off this way so we'll probably catch up to him.{/color}"

show sayori 6ab

mc "Shit."

s 6cb "{color=#9FA100}What's wrong [player]?{/color}"

show monika 6c
show natsuki 6i
show sayori 6fb

mc "{color=#9FA100}Oh,{w=0.33} nothing.{/color}"

show monika 6a
show natsuki 6a
show sayori 6rd at h33

s "{color=#9FA100}C'mon, you'll love him!{/color}"

mc "{color=#9FA100}I'm afraid I don't swing that way, Sayori.{/color}"

show monika 6nb
show sayori 6fb
show natsuki 6gb

m "Aww."

show monika 6m

mc "Aww? The fuck you mean 'Aww'?"

m 6nb "Well, MC, you're not from around here so I thought you'd be..."

show natsuki 6t
show sayori 6y

m 6n "You know..."

show natsuki 6a
show sayori 6a
show monika 6m

mc "I would say 'sorry to disappoint' but we both know how little that means at this point."

m 6eb "Hmph."

m 6bc "Still,{w=0.33} you're the only guy in a literature club full of girls, so you're either a pervert there to ogle a bunch of girls or..."

show monika 6a

mc "Oh come on,{w=0.33} either choice isn't really fair."

m 6bb "Is there something wrong with being a little..."

show natsuki 6t
show sayori 6y

m 6l "Festive?"

show monika 6m
show natsuki 6a
show sayori 6a

"Festive, huh? Haven't heard that one yet."

mc "No, nothing's wrong with it,{w=0.5} it's just not who I am."

mc "And I ain't a pervert either."

show monika 6e

mc "Promise."

m 6bb "I would take that promise,{w=0.33} but we both know how little that means at this point."

show monika 6ab
show sayori 6ab
show natsuki 6ac

mc "{i}Sigh{/i}"

mc "Touche."

"With that, we make out way to the mall."

label Test:

stop music fadeout 2.0
scene bg big_mall_01 with fade_scene_transition
play music mall

"Natsuki and I have been standing outside the same clothing store for a good 20 minutes."

mc "{i}*Huff*{/i}"

"These feet were made for walking, and I'm starting to get a little sore."

"New places get real familiar once you stand around doing dick all for nearly half an hour."

"It's gotten to the point where even the swimsuit section's practically burned into my peripheral vision, vibrant hues caking their negative colours into my retinas."

"..."

"I'm bored out of my mind."

"I should've never come here."

"I should've expected something like this would happen."

"Just a girls' day out at the mall, o' what could that entail?"

"Monika and Sayori went off into the depths of that self-imprisoning retail chain, with the former leaving me in Natsuki's 'care'."

"Of which more or less involved her giving me a couple of glances before quickly turning her gaze back to her phone, just standing next to me."

"She seems to be more and more wired up with each passing moment."

"Her looking around, tapping her feet, ritualistically pulling out her phone, glancing at it then putting it back."

"That look of deep discomfort."

stop music fadeout 2.0

"I can't just ignore it anymore."

play music watashi

show natsuki 6sb at t11

mc "{color=#9FA100}Are you okay?{/color}"

n 6qb "{color=#9FA100}Yeah.{/color}"

show natsuki 6sb

mc "{color=#9FA100}You don't look like you're okay.{/color}"

n 6mb "{color=#9FA100}So?{w=0.33} Why do you care?{/color}"

show natsuki 6gb

mc "{color=#9FA100}Because I don't want to stand around doing nothing.{/color}"

show natsuki 6nb

mc "{color=#9FA100}I want to talk to you.{/color}"

"Having a bit larger vocabulary in Japanese would be a big plus, having Natsuki or anyone else roll their eyes at me would be a less common sight."

n 6x "{color=#9FA100}Ugh, I should've came here on my own so I wouldn't have to babysit Monika's pet.{/color}"

show natsuki 6u

mc "{color=#9FA100}Excuse me?{/color}"

n 6yc "{color=#9FA100}What, you don't understand Japanese anymore?{/color}"

show natsuki 6ic

mc "{color=#9FA100}I understood you perfectly.{/color}"

n 6lc "{color=#9FA100}Then what didn't you get?{/color}"

show natsuki 6z

"Yeesh."

"And now she's back to being her wired old self last seen not a mere moment ago."

show natsuki 6g

mc "{color=#9FA100}Wait.{/color}"

mc "{color=#9FA100}Why did you say you should have come here on your own?{/color}"

show natsuki 6ib

"Natsuki recomposes herself to a more relaxed state with the tapping ceased as she pulls out her phone from her pocket."

"She presents her phone to me with a web page for a bookstore on it."

"I'm assuming it's inside this mall."

n 6mb "{color=#9FA100}I was planning to go here to pick up a book I want but I got hitched to loverboy here, and now the book I want is about to go out of stock.{/color}"

show natsuki 6ib

"I get back at her and roll my eyes."

"You will rue the day I learn some more Japanese to quip at you back, Natsuki."

"At least I found out why she's all twitchy and anxious now."

mc "{color=#9FA100}How far is the store?{/color}"

n 6kb "{color=#9FA100}Just on the other side of this mall.{/color}"

show natsuki 6ib at h11

mc "The fuck are we waiting for? Let's go."

n 6hb "{color=#9FA100}Huh?{/color}"

show natsuki 6gb

mc "{color=#9FA100}I said let's go, then.{/color}"

n 6mb "{color=#9FA100}But, Monika-{nw}{/color}"

show natsuki 6nb

mc "{color=#9FA100}I'll tell her.{/color}"

mc "{color=#9FA100}Don't worry.{/color}"

"With that, Natsuki scrambles off in the opposite direction where we approached the store we were standing outside of with me tailing her."

return

#all the scripting has been revised up until this part.

# scene bg big_mall_02 with wipeleft_scene
# show natsuki 6s at l11

# "The eternity the both of us found ourselves in mere minutes ago really pumped us up as we're speed walking down the length of the mall."

# "Well, speed walking for Natsuki, somewhat expedited walking for me."

# "Our difference in height is what's making me put in a conscious effort to pace myself correctly to not bump into her."

# "Then of course I would also have to not scrape my toes against her heels because of our difference in strides."

# "All of this effort could have gone to waste four abrupt turns ago."

# "..."

# "Whup!"

# "Make that five."

# "Keeping track of Natsuki wouldn't be so much of a problem if she were a little taller."

# "Pink hair's pretty hard to lose track of, which is especially useful considering the amount of turns we're making."

# "I trust Natsuki's judgement in finding the shortest path to wherever we're going though, but this feels a little drawn out."

# "Like, how big is this damn mall?"

# "Every last turn felt like I'm being plunged deeper into a labyrinth of commerce."

# "..."

# "Whup."

# "There's another one."

# "I'm tempted to look back and see how far we've gone."

# "Hmm."

# "A quick glance wouldn't hurt."

# "I turn to see even more mall."

# show natsuki at rhide
# hide natsuki 

# "Each and every bit of it is more unrecognisable as the rest."

# "Taking a peek to see our progress was kinda stupid, considering the amount of turns we took."

# "There was no way we would've stayed on the same straight line at this point."

# "Anyways, back on track."

# "I turn back towards Natsuki-{w=1}{nw}"

# stop music

# "Oh."

# "Shit."

# "I lost her."

# "Uhhh."

# "Okay."

# "Don't panic."

# "The worst thing to do right now is panic."

# "Uhhh."

# "We were going..."

# "This way?"

# "Yeah, that seems about right."

# "I'm trying to look out for a pink head of hair, which is made all the more difficult by the vast amount of people that are also out doing their Sunday shopping."

# "I should probably keep going this way."

# "..."

# "..."

# "Yeah no, I've completely lost her."

# "Ergh... No!"

# "No no no!"

# "Huhh."

# "..."

# "I guess now's a good time than ever to let Monika know Natsuki's dragged me off to fetch a personal errand of hers."

# "I pull my phone out of my pocket to notice a thin patch of thigh sweat has caked itself on my phone's screen."

# mc "Eugh."

# "I wipe it off with my jeans, taking note of how sweaty I get when I get all anxious and panicky."

# # Phone section
# # Messages
# # Monker

# "Wait a sec-"

# "Who's that in the background in Monika's profile picture?"

# "Oh, it's Sayori."

# "I would've guessed they'd be close friends, especially when the pair of them meandered off to do some window shopping."

# "Then actual shopping."

# # Phone section
# # Hey natsukis taking me to a book shop in case if you were wondering
# # Okay, just stay close to her.
# # K will do

# "{i}Ooof.{/i}"

# "I can sweep this minor mishap under the rug."

# "That is if I can catch up to Natsuki."

# "...Of which I cannot, for the life of me, can spot."

# "In my very limited time in knowing her she woulda continued hauling ass to her destination, arbitrary turns and all."

# "I guess I oughta do the same."

# "Phone time."

# # Phone section
# # Maps
# # â€˜ã€ŒBookstoresã€â€™
# # Search

# "Oookay, let's see."

# "Mmm, too bougie."

# "..."

# "Too far."

# "Too specialised."

# "Witches' apothecary- what the fuck? How is this a bookstore?"

# "..."

# "Too small{w}- oh actually..."

# "This might be the one Natsuki showed me earlier."

# "On closer inspection this is the exact bookstore."

# "..."

# "Okay, just a three minute walk away, let's go."

# stop ambience_noise
# scene black with wiperight

# "These directions were a lie."

# "I've been plunged deeper into the heart of this mall."

# "I'm fairly certain this constitutes trespassing."

# "I know old habits die hard but this time it's unintentional."

# "Though it's not like anyone's gonna know, I haven't seen another person in the past few minutes."

# "Which is strange, I would've suspected these corridors to have workers pushing carts around or something along those lines."

# "Sucks to be them though, each one of these passes just seem to go on forever until it intersects with another perpendicular hall."

# "The only thing keeping me company is the incessant hum-buzz of the incandescent lights above."

# "Aside from that and my footsteps, everything else is dead silent."

# "The rabble of a Sunday's mall seems like a distant memory to me now."

# window hide(dissolve)
# # Tense music (to be made)
# $ pause(3)
# window show(dissolve)
# $ pause(0.3)

# "The ETA set by the app has long passed."

# "Every turn I take my phone spits out a new route that leads me to nowhere."

# "..."

# "Okay, another turn."

# "Woah, woah! Jesus."

# "Almost lost my balance."

# "I place a hand on a cold concrete wall while I pull out my phone to see if I'm still going in the right way."

# "..."

# "Yeah, I figured it would be in the complete opposite direction."

# "I take my hand off the wall, trying my best to regain my composure."

# "Which evidently isn't good enough at all as I topple over to the opposite side of the hall, firmly knocking myself in the head."

# "I can feel myself get a little more dizzy every single 180 I take when I reach an intersection."

# "Am I turning too fast?{w} Am I doing this to myself?"

# "Have I suddenly become claustrophobic, making these halls look smaller and smaller as time goes on?"

# "Is there a concoction of chemicals left over from operations and construction that's vaporised in the air that I'm just now feeling the effects of?"

# "Is it a mix of all of these factors including the fact that I headbutted the wall a moment ago?"

# "Well, whatever it is, staying here is most certainly not a good thing."

# "Not for my personal health nor my already spotty record."

# "..."

# mc "Huh?"

# "I just heard something."

# "A door opening somewhere."

# "Shit."

# "Shit shit shit."

# "I am NOT going to get caught out trespassing here!"

# "C'mon phone!"

# "..."

# "Are you shitting me? I was just there!"

# "You know what, fuck you, I've got a better idea."

# "I'll just run completely straight in one direction."

# "..."

# "Yeah no, those footsteps aren't getting any farther, gotta go."

# "I bolt down the length of the hallway I'm in, completely the opposite direction to where I heard that sound a moment ago."

# "If no one knew I was here they sure do now, me hauling ass isn't exactly stealthy, especially when my runners squeak against the floor like an NBA match."

# "Especially when I'm about to slam into double crash bar doors-{w=1}{nw}"

# mc "Oomph!"

# "I stumble for a bit before picking up speed again."

# "Looking ahead I see..."

# "Even more corridor."

# "It just doesn't end!"

# "I pick up the pace again."

# "I start to notice other stuff on the walls that don't seem familiar."

# "A crack here, a safety poster there, a different coloured pipe on the ceiling."

# "These little things give me a little more motivation to run a little faster."

# "..."

# "Hey, I haven't seen that door before-{w=1}{nw}"

# "Oh fuck- It just opened!"

# "My runners squeak as I take a left to another corridor and bolt."

# "I spot a singular crash bar door at the very end."

# "This looks very promising-{w=1}{nw}"

# "Eurgh, what's that smell?"

# "It's like a mix of every single cleaning chemical under the cupboard!"

# "Nope!"

# "{i}*cough cough*{/i}"

# "That is definitely not good to breathe in."

# "The stench grows stronger."

# "Every stride I take becomes more uncalculated and uncoordinated, a step too far or too short would send me straight to the floor."

# "Every hurried breath of air saturates my lungs with stinging vapour."

# "Every gasp is akin to swallowing knives."

# "The chemicals are in the way of the clean air I so desperately need."

# "Haste and desperation clouds my higher judgement as the door grows bigger in my vision."

# "I can barely think."

# "Having a closer look of it, there's a window just above its crash bar."

# "I ready myself to make contact with the door."

# scene bg big_mall_03

# mc "Mmf!"

# q "{color=#9FA100}Eep!{/color}"

# mc "{color=#9FA100}*cough cough*{/color}"

# q "{color=#9FA100}What the...{/color}"

# "I hear the door close so forcefully behind I feel a small gust as I put my hands on my knees."

# "I'm caught between taking gasps of air and coughing."

# "I can physically feel the good air flush out the bad air from my lungs."

# "It's a good half minute of hacking my lungs out when I realise someone's been standing right next to me the entire time."

# "I get up from my dazed state to appear semi-functional to the people around me."

# "..."

# "Oh."

# show natsuki 4bw at t11

# n "{color=#9FA100}Weren't you just behind me?{/color}"

# show natsuki 4bx

# mc "{color=#9FA100}Yes.{/color}"

# mc "{color=#9FA100}I lost you while we were coming here.{/color}"

# n 2bm "{color=#9FA100}What?{w=0.33} How?{/color}"

# show natsuki 2bn

# mc "{color=#9FA100}I uhh...{/color}"

# mc "{color=#9FA100}Wanted to see how far we walked.{/color}"

# mc "{color=#9FA100}So I looked behind me.{/color}"

# mc "{color=#9FA100}And then I didn't see you.{/color}"

# n 2bg "{color=#9FA100}...{/color}"

# n 2bh "{color=#9FA100}Lemme guess,{w=0.33} I'm too short and you lost me in the crowd?{/color}"

# show natsuki 2bi

# mc "..."

# mc "Well, when you put it like that-{nw}"

# n 3be "{color=#9FA100}Speak Japanese!{/color}"

# show natsuki 1bf

# "I tense up and position my body like I'm about to defuse a bomb."

# mc "{color=#9FA100}Yes, you...{/color}"

# mc "{color=#9FA100}...are?{/color}"

# show natsuki 1bo at h11

# "Fuck!"

# "Death approaches in measured tippy taps."

# "Please don't blow up."

# mc "Look man, you were turning so many damn times-{w=1}{nw}"

# n 2bv "{color=#9FA100}Blegh-{/color}"

# n "{color=#9FA100}{i}*cough*{/i} Ergh, why do you smell like that?{/color}"

# show natsuki 2br at t11

# mc "{color=#9FA100}Yeah, about that...{/color}"

# mc "{color=#9FA100}My phone directed me through a path that wasn't correct.{/color}"

# show natsuki 1bs

# "She waves a hand in front of her to dispel any more of that god-awful stench away."

# "Natsuki notices the door behind me and leans to her left to take a peek behind me whilst small coughs escape her mouth."

# "I turn around to do the same."

# "The door I rammed through a moment ago is thoroughly shut."

# "I peer through the window, following Natsuki's suit."

# "We spot a figure in the distance carrying a pair of gas tanks, donning a full face respirator."

# "The pair of us seemed to catch their attention, a moment passes between us and the masked figure staring at each other before they disappear from sight."

# "I wonder if it would've been better to hold my breath and just walk out rather than run and flush out my lungs with whatever gas that was in there."

# n 2bt "{color=#9FA100}You're not supposed to be back there you know?{/color}"

# show natsuki 2bi

# mc "{color=#9FA100}Well, now I know.{/color}"

# "Areas under fumigation aren't generally open to the public."

# mc "{color=#9FA100}But, I'm here now, so it all works.{/color}"

# "I spot a brightly coloured book in Natsuki's hands."

# mc "{color=#9FA100}Got what you were looking for?{/color}"

# n 3bd "{color=#9FA100}Yeah.{/color}"

# show natsuki 3ba

# "She's grasping it so tightly."

# "It ain't going nowhere, Natsuki."

# mc "May I take a look at it?"

# n 1bu "{color=#9FA100}...{/color}"

# "Don't think too hard, dude."

# n 1bq "{color=#9FA100}Be gentle...{/color}"

# show natsuki 2bs

# "Natsuki hands me her book she's been coddling."

# "I delicately hold her book with both hands, making a conscious effort not to crease the soft covers."

# "..."

# "The blurb?"

# "Oh, right, Japan."

# "I flip the book to the other side."

# "Moving my thumb away, it reveals an exceptionally pink & pastel coloured cover."

# "{i}Parfait Girls{/i}"

# 「Volume 27」

# Four characters adorn a sizable space on it. 

# They’re all so… girly… 

# Hold on.

# I glance back and forth between the manga and Natsuki.

# …

# Hmm…

# Manga.

# Natsuki.

# Manga.

# Natsuki.

# My goodness.

# I’m willing to bet my week’s allowance that this manga had a drastic impact on Natsuki’s personality.

# 「What are you looking at?」

# MC
# 「Ah-」

# 「Sorry.」

# Noted, no eye contact.

# Kinda like with those ankle-biting dogs.

# …

# Looking through page after page, it’s immediately apparent to me that I’m not the target demographic for this.

# Everything about it is just so… sweet… 

# To an exceptional degree.

# The characters, their design, the cover art…

# Even it’s… smell? It’s a little hard to tell since my sinuses are still filled with the aroma of industrial strength chemicals.

# But I swear there’s a hint of perfume in this book.

# …

# I stop reading after I catch myself.

# …

# Hold on.

# Am I actually understanding most of this?

# Getting a hold of what I’m actually reading shows furigana atop some of the kanji in the speech bubbles.

# Neato.

# Natsuki
# 「Are you done?」

# MC
# 「What?」

# 「Oh, right.」

# I give her manga back.

# Right back into her overly protective hands.

# Natsuki
# 「Well…」

# …

# My eyes are fixated on the manga, but I can tell she’s not looking at me now.

# Maybe I can… Look at her?

# MC
# 「What’s wrong?」

# Natsuki
# 「What… did you think?」

# MC
# “Well-”

# Natsuki
# 「No spoilers!」

# MC
# 「It was very…」

# 「Sweet.」

# 「And girly.」

# 「And for kids.」

# Natsuki
# 「...Really?」

# MC
# 「I uh-」

# Oh shit.

# Why did I say that?

# Oh yeah.

# 「It’s got furigana, right? I thought those were for kids to learn kanji.」

# Natsuki
# 「Yes… It does…」

# 「But that doesn’t mean it’s only for kids!」

# 「It has a lot more going for it than just the technical stuff!」

# 「If you get a lot deeper into it, each of the character’s ``relationships`` with each other are pretty complex.」

# 「Not that you’d care or anything.」

# MC
# 「Actually I was going to ask you why Minori-」

# Natsuki
# 「Nnnn!- no spoilers!」

# MC
# 「I understand.」

# 「That doesn’t mean I didn’t like it though.」

# 「This manga can really help me with learning kanji.」

# 「I just don’t want to be seen reading it.」

# Natsuki
# 「Why not?」

# MC
# 「Natsuki.」

# I quickly but tactfully snatch the manga from her hands.

# Natsuki
# 「Hey!」

# MC
# 「Look.」

# I present myself as ‘guyish’ as can be while holding her manga in full display.

# 「Now, when was the last time you seen a boy read ‘Parfait Girls’?」

# Natsuki takes a few paces back, her eyes dart up and down, sizing me up before taking the book out of my hands again.

# Natsuki
# 「Yeah, you do look a little weird.」

# MC
# 「See.」

# 「And weird people get looked at a lot.」

# 「And I don’t want that.」

# I’d rather not have a pair of eyes on me all the time, especially with what I just did a few minutes ago.

# Natsuki
# 「Without the book though, you look pretty plain.」

# MC
# 「Mhm. Plain is what I like.」

# Black hoodie, jeans. Undefeated urban camouflage.

