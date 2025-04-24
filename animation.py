from manim import *

class GRUBBootIntro(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("GNU GRUB  version 20.25", font="Cascadia Code", color=WHITE).scale(0.6).to_edge(UP)

        # GRUB-style menu options
        options = [
            "  Arch Linux",
            "  Windows 10",
            "  EchoDRJ Channel",
            "  System setup"
        ]

        # Create text lines
        options_text = VGroup(*[
            Text(line, font="Cascadia Code", color=WHITE).scale(0.55)
            for line in options
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Add menu box
        menu_box = SurroundingRectangle(options_text, color=WHITE, buff=0.3)
        menu_box.set_width(menu_box.width * 1.5)

        # Postion text in menu box
        options_text.align_to(menu_box, LEFT)
        options_text.align_to(menu_box, UP)
        options_text.shift(DOWN * 0.2)
        options_text.shift(RIGHT * 0.35)

        full_menu = VGroup(title, VGroup(menu_box, options_text)).arrange(DOWN, buff=.5)
        
        # Create Highlight feature
        def make_highlight(index):
            buffer = 0.1
            rect = Rectangle(
                width=menu_box.width -buffer * 2,
                height=options_text[index].height + 0.2,
                color=LIGHT_GREY,
                fill_opacity=0.5,
                stroke_width=0
            )
            # Position Highlight
            rect.move_to(options_text[index].get_center())
            rect.align_to(menu_box, LEFT)
            rect.shift(RIGHT * buffer)
            return rect
        
        # Highlight first option
        highlight = make_highlight(0)
        self.add(highlight)
       
        ######################################
        ############## SCENCE 1 ##############
        ######################################

        # Fade in from black
        self.play(FadeIn(full_menu), FadeIn(highlight), run_time=1)

        # Move to "Windows 11"
        self.play(Transform(highlight, make_highlight(1)))
        self.wait(.25)

        # Move to "EchoDRJ Channel"
        self.play(Transform(highlight, make_highlight(2)))
        self.wait(2)

        ######################################
        ############## SCENCE 2 ##############
        ######################################

        # Add a loading sequence
