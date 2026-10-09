1. Pipeline Overview

Classification → OCR → Field Extraction → Confidence Scoring → JSON Output.

2. Confidence Threshold Rationale

Threshold = 0.8 chosen because OCR confidence <0.8 often corresponded to mis‑reads in testing.

3. Handwritten vs Printed Handling

Printed IDs (Aadhaar, PAN, DL, Passport): EasyOCR standard mode + regex validation.

Handwritten forms (NACH/ECS, FATCA, Benefit Illustration, Moral Hazard, Consent, Suitability Profiler): EasyOCR handwriting recognition.

Failure cases: smudged digits mis‑read, cursive place names <0.6 confidence, dates with dashes missed regex.

4. Deliverables

results.json → structured extraction.

flagging_report.json → flagged fields below threshold.

Confidence scores per field.

Notes on handwritten handling.