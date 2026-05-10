from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_font("helvetica", "B", 45)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", x=1, y=60)
        self.set_font_size(30)
        self.set_text_color(255, 255, 255)
        self.text(x=42, y=130, text=f"{name.title()} took CS50")

    def save(self):
        self.output("shirtificate.pdf")

    def __str__(self):
        return "a PDF Shirtificate"


def main():
    name = input("Name: ")
    pdf = PDF(name)
    print(pdf)
    # pdf.output("shirtificate.pdf")
    pdf.save()


if __name__ == '__main__':
    main()