# This boolean decides wherever you want to enable or disable
# the notebook button (don't change it from here)
default notebook_enabled = False

# This boolean is used to fix a bug with "selected" property
# of quick menu button, don't change it
default notebook_shown = False

# These variables define the font/size/x alignment of values' text
# "dissolve_nb" is a child of Dissolve()
define gui.text_nb_default_font = "gui/font/Halogen.ttf"
define gui.text_nb_values_size = 47.5
define gui.nb_x_align = 0.31
define dissolve_nb = Dissolve(0.35, alpha=False)

# Style of the values text
style nb_values_style:
    font gui.text_nb_default_font
    size gui.text_nb_values_size
    outlines []
    color "#000"

python early:
    
    # This function is used to determine which screen to show/hide
    # It is called in the "textbuttons" statements
    def notebook_selection_F(called_from):
        if called_from == "Blank":
            renpy.show_screen("notebookUI_blank")
            renpy.show_screen("notebookUI_intelligence_value")
            renpy.show_screen("notebookUI_language_value")
            renpy.show_screen("notebookUI_fitness_value")
        
        elif called_from == "Monika":
            renpy.show_screen("notebookUI_monika")
            renpy.hide_screen("notebookUI_intelligence_value")
            renpy.hide_screen("notebookUI_language_value")
            renpy.hide_screen("notebookUI_fitness_value")

        elif called_from == "Sayori": 
            renpy.show_screen("notebookUI_sayori")
            renpy.hide_screen("notebookUI_intelligence_value")
            renpy.hide_screen("notebookUI_language_value")
            renpy.hide_screen("notebookUI_fitness_value")

        elif called_from == "Natsuki": 
            renpy.show_screen("notebookUI_natsuki")
            renpy.hide_screen("notebookUI_intelligence_value")
            renpy.hide_screen("notebookUI_language_value")
            renpy.hide_screen("notebookUI_fitness_value")
        
        elif called_from == "Yuri": 
            renpy.show_screen("notebookUI_yuri")
            renpy.hide_screen("notebookUI_intelligence_value")
            renpy.hide_screen("notebookUI_language_value")
            renpy.hide_screen("notebookUI_fitness_value")
            
# This is the buttons screen
screen notebook_buttons_UI():
    tag notebook_pages
    modal True
    zorder 15
    
    hbox:
        at notebook_button_animation
        xalign 0.5
        yalign 0.5
        spacing 40
        
        textbutton "Close":
            hovered Play("audio", "gui/sfx/hover.ogg")
            
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    SetVariable("notebook_shown", False),
                    Hide(transition=dissolve_nb),
                    Hide("notebookUI_intelligence_value", transition=dissolve_nb),
                    Hide("notebookUI_language_value", transition=dissolve_nb),
                    Hide("notebookUI_fitness_value", transition=dissolve_nb) ] 
        
        textbutton "Blank":
            hovered Play("audio", "gui/sfx/hover.ogg")
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    Function(notebook_selection_F, "Blank") ]
        
        textbutton "Monika":
            hovered Play("audio", "gui/sfx/hover.ogg")
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    Function(notebook_selection_F, "Monika") ]

        textbutton "Sayori":
            hovered Play("audio", "gui/sfx/hover.ogg")
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    Function(notebook_selection_F, "Sayori")]

        textbutton "Natsuki":
            hovered Play("audio", "gui/sfx/hover.ogg")
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    Function(notebook_selection_F, "Natsuki") ]

        textbutton "Yuri":
            hovered Play("audio", "gui/sfx/hover.ogg")
            action[ Play("audio", "gui/sfx/select.ogg"), 
                    Function(notebook_selection_F, "Yuri") ]

# These are the values' screens
screen notebookUI_intelligence_value():
    zorder 16

    text str(intelligence_value):
        style "nb_values_style"
        align(gui.nb_x_align, 0.328)

screen notebookUI_language_value():
    zorder 16

    text str(language_value):
        style "nb_values_style"
        align(gui.nb_x_align, 0.56)

screen notebookUI_fitness_value():
    zorder 16

    text str(fitness_value):
        style "nb_values_style"
        align(gui.nb_x_align, 0.78)

screen notebookUI_blank():
    tag notebook_pages
    modal True
    zorder 15
      
    use notebook_buttons_UI id "notebook_UI"

    on "show" action(SetVariable("notebook_shown", True))
    
    image "mod_assets/notebook/UI_Notebook_Screen_Blank.png" #at notebook_animation
           
# All of the screens below are pretty self-explanatory
screen notebookUI_monika():
    tag notebook_pages
    modal True
    zorder 15

    use notebook_buttons_UI id "notebook_UI"
    
    image "mod_assets/notebook/UI_Notebook_Screen1.png" #at notebook_animation
    
screen notebookUI_sayori():
    tag notebook_pages
    modal True
    zorder 15

    use notebook_buttons_UI id "notebook_UI"
    
    image "mod_assets/notebook/UI_Notebook_Screen2.png" #at notebook_animation

screen notebookUI_natsuki():
    tag notebook_pages
    modal True
    zorder 15

    use notebook_buttons_UI id "notebook_UI"
    
    image "mod_assets/notebook/UI_Notebook_Screen3.png" #at notebook_animation

screen notebookUI_yuri():
    tag notebook_pages
    modal True
    zorder 15

    use notebook_buttons_UI id "notebook_UI"
    
    image "mod_assets/notebook/UI_Notebook_Screen4.png" #at notebook_animation

# These two transforms define the animations of the buttons and
# of the notebook pages themselves
transform notebook_button_animation:
    subpixel True
    yoffset - 900
    easein 2.0 yoffset - 300
