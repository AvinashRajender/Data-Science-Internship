import PyPDF2
import re

class DocumentAgent:
    def __init__(self, file_path):
        self.text = self._extract_text(file_path)
        self.sections = self._split_into_sections(self.text)
        self.answered = set()
        self.last_topic = None

    def _extract_text(self, file_path):
        reader = PyPDF2.PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    def _split_into_sections(self, text):
        """
        General-purpose section splitter:
        - Detects headings dynamically (all caps lines OR numbered headings like 1., 2.1., etc.)
        - Splits content between headings
        """
        # Regex for headings: ALL CAPS or numbered outlines
        heading_pattern = re.compile(r"(^[A-Z][A-Z\s\-]{3,}$|^\d+(\.\d+)*\s.*)", re.MULTILINE)

        matches = list(heading_pattern.finditer(text))
        sections = {}

        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i+1].start() if i+1 < len(matches) else len(text)
            heading = match.group().strip()
            content = text[start:end].strip()
            sections[heading] = content

        return sections

    def answer(self, query):
        query = query.lower()
        for title, content in self.sections.items():
            # Loose keyword match
            if any(word in title.lower() for word in query.split()):
                if title in self.answered:
                    return f"I’ve already covered {title}. Let’s move to another section."
                self.answered.add(title)
                self.last_topic = title

                # Skip heading line itself
                lines = content.split("\n")
                snippet = "\n".join(lines[1:]) if len(lines) > 1 else content

                return f"{snippet[:400]}... (from {title})"
        return "Sorry, I couldn’t find that in the document."
