from fpdf import FPDF


class Shirtificate(FPDF):
    """
    Create an object of a shirt with "(name of person) took CS50" printed on and return it as a pdf.
    """

    def header(self):
        # Setting font:
        self.set_font("helvetica", "B", 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 70, "CS50 Shirtificate", align="C")

    def shirt(self):
        # Printing shirt:
        self.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x=10, y=70, w=190)

    def name_text(self, name):
        self.name = name
        # Setting font:
        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)
        # Printing text:
        self.cell(-30, 240, f"{self.name.title()} took CS50", align="C")

    def run(self, name):
        sommie.add_page()
        self.shirt()
        self.name_text(name)
        sommie.output("shirtificate.pdf")



sommie = Shirtificate()
sommie.run(input("Enter your name: "))
