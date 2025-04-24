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
        self.play(FadeIn(full_menu), FadeIn(highlight), run_time=.5)

        # Move to "Windows 10"
        self.play(Transform(highlight, make_highlight(1)))
        self.wait(.1)

        # Move to "EchoDRJ Channel"
        self.play(Transform(highlight, make_highlight(2)))
        self.wait(.5)

        ######################################
        ############## SCENCE 2 ##############
        ######################################

        # Fade out the menu and highlight
        self.play(FadeOut(full_menu), FadeOut(highlight), run_time=.5)

        # Simulate boot sequence
        loading = [
            "Booting EchoDRJ Channel...",
            "Initializing video...",
            "Loading YouTube interface...",
            "Mounting new video upload...",
            "Launching EchoDRJ Channel...",
            "Don't forget to Like and Subscribe..."
        ]

        # Add Matrix_Green
        MATRIX_GREEN = "#00FF41"

        # Create Loading Sequence 
        boot_texts = VGroup()
        for i, line in enumerate(loading):
            left_bracket = Text("[", font="Cascadia Code", color=WHITE).scale(0.5)
            ok = Text("OK", font="Cascadia Code", color=MATRIX_GREEN).scale(0.5)
            right_bracket = Text("]", font="Cascadia Code", color=WHITE).scale(0.5)
            txt = Text(f" {line}", font="Cascadia Code", color=WHITE).scale(0.5).to_edge(UL)
            full_line = VGroup(left_bracket, ok, right_bracket, txt).arrange(RIGHT)
            full_line.to_edge(UL).shift(DOWN * i * 0.6)
            boot_texts.add(full_line) 

        # Animate loading sequence
        for boot_line in boot_texts:
            self.play(Write(boot_line), run_time=0.25)
            self.wait(0.1)

        self.wait(1)
