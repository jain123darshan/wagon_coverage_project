import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import inch

class ReportGenerator:
    def __init__(self, reports_dir, train_number, coach_count, selected_frames):
        self.reports_dir = reports_dir
        self.train_number = train_number
        self.coach_count = coach_count
        self.selected_frames = selected_frames

    def generate_pdf_report(self):
        pdf_path = os.path.join(self.reports_dir, 'Wagon_Coverage_Report.pdf')
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Title
        title = Paragraph("Rake(Wagon) Coverage Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Summary
        summary = Paragraph(f"Train Number: {self.train_number}<br/>Total Coaches: {self.coach_count}", styles['Normal'])
        story.append(summary)
        story.append(Spacer(1, 12))

        for coach_dir, frames in self.selected_frames.items():
            coach_name = os.path.basename(coach_dir)
            coach_title = Paragraph(f"Coach: {coach_name}", styles['Heading2'])
            story.append(coach_title)
            story.append(Spacer(1, 12))

            for frame in frames[:5]:  # Limit to 5 images per coach for brevity
                if os.path.exists(frame):
                    img = Image(frame, width=4*inch, height=3*inch)
                    story.append(img)
                    story.append(Spacer(1, 12))

            story.append(PageBreak())

        doc.build(story)
        print(f"PDF report generated at {pdf_path}")

    def generate_html_report(self):
        html_path = os.path.join(self.reports_dir, 'Wagon_Coverage_Report.html')
        with open(html_path, 'w') as f:
            f.write("<html><head><title>Rake(Wagon) Coverage Report</title></head><body>")
            f.write(f"<h1>Rake(Wagon) Coverage Report</h1>")
            f.write(f"<p>Train Number: {self.train_number}</p>")
            f.write(f"<p>Total Coaches: {self.coach_count}</p>")

            for coach_dir, frames in self.selected_frames.items():
                coach_name = os.path.basename(coach_dir)
                f.write(f"<h2>Coach: {coach_name}</h2>")
                for frame in frames[:5]:  # Limit to 5 images per coach
                    if os.path.exists(frame):
                        f.write(f'<img src="{frame}" width="400" height="300"><br>')

            f.write("</body></html>")
        print(f"HTML report generated at {html_path}")
