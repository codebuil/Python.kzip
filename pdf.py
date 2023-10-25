from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys

def text_to_pdf(input_text, output_pdf):
    y=700;
    try:
        c = canvas.Canvas(output_pdf, pagesize=letter)
        hh=input_text.split("\n")
        for j in range(len(hh)):
            
            c.drawString(100,y,hh[j])
            y=y-30
        c.save()

        print(f"Arquivo PDF gerado com sucesso: {output_pdf}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python text_to_pdf.py <arquivo_de_entrada.txt> <arquivo_de_saida.pdf>")
    else:
        input_text_file = sys.argv[1]
        output_pdf_file = sys.argv[2]
        
        with open(input_text_file, 'r') as input_text_file:
            input_text = input_text_file.read()
        
        text_to_pdf(input_text, output_pdf_file)
