from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import calendar
import sys

def create_year_calendar_pdf(year):
    try:
        c = canvas.Canvas(f"calendario_{year}.pdf", pagesize=letter)

        days_of_week = list(calendar.day_abbr)
        months = list(calendar.month_abbr)[1:]

        x_offset = 50
        y_offset = 750
        day_box_size = 50

        c.setFont("Helvetica", 10)

        for i, day in enumerate(days_of_week):
            c.drawString(x_offset + day_box_size * (i+1), y_offset, day)

        for i, month in enumerate(months):
            day_box_size = 50
            yyday_box_size = 60
            c.drawString(x_offset, y_offset - (i + 1) * yyday_box_size, month)


            yday_box_size = 11

            cal = calendar.monthcalendar(year, i + 1)
            for week_num, week in enumerate(cal):
                for day_num, day in enumerate(week):
                    if day != 0:
                        pass
                        c.drawString(x_offset + day_box_size * (day_num+1), y_offset - (yyday_box_size*(i) + (week_num+1) * yday_box_size), str(day))

        c.save()
        print(f"Calendário do ano {year} gerado com sucesso no arquivo: calendario_{year}.pdf")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python create_year_calendar_pdf.py <ano>")
    else:
        year = int(sys.argv[1])
        create_year_calendar_pdf(year)
