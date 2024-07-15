from manim import *

class FashionQuiz(Scene):
    def construct(self):
        self.questions = [
            ("What's your favorite type of outfit?", ["Classic", "Glamorous", "Elegant", "Bold"]),
            ("What's your go-to accessory?", ["Pearls", "Diamonds", "Scarves", "Statement Jewelry"]),
            ("What's your favorite color?", ["Black", "Red", "White", "Gold"]),
            ("What's your ideal evening?", ["Dinner party", "Red carpet event", "Quiet night in", "Gala"]),
            ("What's your preferred footwear?", ["Heels", "Flats", "Boots", "Sandals"])
        ]
        self.answers = []

        for question, options in self.questions:
            self.show_question(question, options)

        result = self.determine_result()
        result_text = Text(result, font_size=36)
        self.play(FadeIn(result_text))
        self.wait(3)

    def show_question(self, question, options):
        question_text = Text(question, font_size=36)
        self.play(FadeIn(question_text))
        self.wait(1)

        option_texts = [Text(option, font_size=24) for option in options]
        option_group = VGroup(*option_texts).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(question_text, DOWN, buff=0.5)

        self.play(FadeIn(option_group))
        self.wait(2)

        # Simulate a random choice (for demonstration purposes)
        chosen_option = option_texts[0]
        self.play(chosen_option.animate.set_color(YELLOW))
        self.answers.append(options.index(chosen_option.text) + 1)
        self.wait(1)

        self.play(FadeOut(question_text), FadeOut(option_group))

    def determine_result(self):
        if self.answers.count(1) > 3:
            return "You relate to Audrey Hepburn!"
        elif self.answers.count(2) > 3:
            return "You relate to Marilyn Monroe!"
        elif self.answers.count(3) > 3:
            return "You relate to Grace Kelly!"
        else:
            return "You relate to Elizabeth Taylor!"

if _name_ == "_main_":
    config.background_color = WHITE
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 7.0
    config.frame_width = 14.0
    scene = FashionQuiz()
    scene.render()