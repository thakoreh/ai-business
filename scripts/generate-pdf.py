"""
Generate the Grand River AI Readiness Checklist PDF.
Real content, 3 pages, branded.
"""
from fpdf import FPDF

class GRPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            # Dark header band
            self.set_fill_color(10, 10, 10)
            self.rect(0, 0, 210, 40, "F")
            # Brand
            self.set_font("Helvetica", "B", 20)
            self.set_text_color(251, 113, 133)
            self.cell(0, 20, "Grand River AI", align="C", new_x="LMARGIN", new_y="NEXT")
            self.set_font("Helvetica", "", 9)
            self.set_text_color(212, 212, 216)
            self.cell(0, 6, "Production AI Systems for Ontario Businesses", align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(8)
        else:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(150, 150, 160)
            self.cell(0, 8, "Grand River AI  |  AI Readiness Checklist", align="R")
            self.ln(12)

    def footer(self):
        self.set_y(-22)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 160)
        self.cell(0, 5, f"Page {self.page_no()}  |  grandriverai.ca  |  hello@grandriverai.ca  |  (226) 975-9417",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, "© 2026 Grand River AI. Paris, Ontario.", align="C")

pdf = GRPDF()
pdf.set_auto_page_break(auto=True, margin=25)
pdf.add_page()

# === PAGE 1: Title + Intro + Categories 1-2 ===

# Accent line
pdf.set_draw_color(249, 115, 22)
pdf.set_line_width(1.5)
pdf.line(20, 48, 60, 48)
pdf.ln(6)

# Title
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(30, 30, 35)
pdf.multi_cell(0, 10, "The Ontario Business\nAI Readiness Checklist")
pdf.ln(3)

pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(100, 100, 110)
pdf.multi_cell(0, 6, "A 20-point self-assessment to find your first AI automation opportunity. Score each item honestly - the goal is to identify where AI can save real hours, not to get a perfect score.")
pdf.ln(4)

# How to score
pdf.set_fill_color(245, 245, 240)
pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(50, 50, 55)
pdf.cell(0, 7, "  How to score:  0 = Not at all    1 = Sometimes    2 = Mostly automated    N/A = Does not apply", fill=True, new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)

def checklist_section(pdf, title, items):
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(236, 72, 153)
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 65)
    for i, item in enumerate(items, 1):
        pdf.cell(8, 7, "")
        pdf.cell(8, 7, "[  ]")  # checkbox
        pdf.multi_cell(0, 7, f"  {item}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

# Section 1: Lead & Customer Handling
checklist_section(pdf, "1.  Lead & Customer Handling", [
    "Leads are responded to within 1 hour during business hours.",
    "After-hours inquiries get an automated response so no lead goes cold.",
    "Every lead is qualified (budget, timeline, need) before a human touches it.",
    "Appointment booking is self-serve or automated (no back-and-forth emails).",
    "Lead data flows into your CRM automatically - no manual data entry.",
])

# Section 2: Customer Support
checklist_section(pdf, "2.  Customer Support & Communication", [
    "Customers can get instant answers to common questions outside business hours.",
    "Repeated questions (hours, pricing, availability) are documented in a searchable knowledge base.",
    "Customer emails are triaged by priority before a team member reads them.",
    "Unanswered questions are logged so you can improve your knowledge base over time.",
])

pdf.add_page()

# === PAGE 2: Categories 3-5 ===
pdf.ln(2)

# Section 3: Operations & Admin
checklist_section(pdf, "3.  Operations & Admin", [
    "Invoices are generated and sent without manual effort.",
    "Recurring reports (weekly KPIs, monthly summaries) are produced automatically.",
    "Data from different tools (CRM, accounting, scheduling) is synced without manual entry.",
    "Internal documents are searchable and organized - nobody wastes time hunting for files.",
])

# Section 4: Document Processing
checklist_section(pdf, "4.  Document Processing", [
    "Incoming documents (PDFs, emails, forms) are sorted and routed automatically.",
    "Data extraction from documents (names, amounts, dates) is handled without manual typing.",
    "Contracts and proposals are generated from templates with auto-filled client data.",
])

# Section 5: Decision Support
checklist_section(pdf, "5.  Decision Support & Reporting", [
    "You have a real-time dashboard showing your most important business metrics.",
    "Anomalies (unusual drop in sales, spike in complaints) are flagged automatically.",
    "You get plain-English summaries of business performance instead of raw spreadsheets.",
])

# Scoring guide
pdf.ln(6)
pdf.set_fill_color(245, 245, 240)
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(50, 50, 55)
pdf.cell(0, 8, "  Your Score", fill=True, new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.set_font("Helvetica", "", 10.5)
pdf.set_text_color(60, 60, 65)
pdf.multi_cell(0, 6.5, "Count how many boxes you checked (0-20):")
pdf.ln(2)

scores = [
    ("0-5 checked", "High opportunity. Your business has significant room for AI-driven time savings. A single automation could save 10+ hours per week."),
    ("6-10 checked", "Moderate opportunity. You have some systems but clear gaps. Targeting 2-3 workflows could yield meaningful efficiency gains."),
    ("11-15 checked", "Good foundation. You are ahead of most small businesses. Focus on the remaining unchecked areas for incremental gains."),
    ("16-20 checked", "Excellent. You are well-automated. AI can still help with advanced tasks: predictive analytics, intelligent decision support, or natural language interfaces."),
]
for score, desc in scores:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(236, 72, 153)
    pdf.cell(38, 6, score)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 65)
    pdf.multi_cell(0, 6, desc, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

pdf.add_page()

# === PAGE 3: Action Plan + CTA ===
pdf.ln(2)

pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(30, 30, 35)
pdf.cell(0, 9, "Your Next Step", new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(60, 60, 65)
pdf.multi_cell(0, 6.5, "Pick the 3 unchecked items that would save the most time if automated. Then answer these questions for each:")
pdf.ln(4)

questions = [
    "How many hours per week does this task currently take?",
    "How many people are involved in this task?",
    "What happens when this task is done late or incorrectly (lost leads, missed deadlines, unhappy customers)?",
    "What tool or system does this task currently live in (email, spreadsheet, CRM, paper)?",
]
for i, q in enumerate(questions, 1):
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(236, 72, 153)
    pdf.cell(8, 7, f"{i}.")
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 65)
    pdf.multi_cell(0, 7, q, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

# CTA box
pdf.ln(4)
pdf.set_fill_color(10, 10, 10)
pdf.rect(15, pdf.get_y(), 180, 38, "F")
pdf.set_xy(20, pdf.get_y() + 5)
pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(251, 113, 133)
pdf.cell(0, 8, "Get your free AI Opportunity Audit", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(20)
pdf.set_font("Helvetica", "", 10.5)
pdf.set_text_color(212, 212, 216)
pdf.multi_cell(170, 5.5, "In 20 minutes, we will review your checklist, map 3 automation opportunities specific to your business, and recommend one quick win you can ship first. No cost, no obligation.")
pdf.ln(2)
pdf.set_x(20)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(251, 113, 133)
pdf.cell(0, 6, "Book your audit: calendly.com/hirenthakore/ai-automation-discovery-call")
pdf.ln(5)
pdf.set_x(20)
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(160, 160, 170)
pdf.cell(0, 5, "Or email: hello@grandriverai.ca   |   Call: (226) 975-9417")

# Save
pdf.output("C:/tmp/grandriver-ai/assets/grand-river-ai-readiness-checklist.pdf")
print("PDF generated successfully!")
