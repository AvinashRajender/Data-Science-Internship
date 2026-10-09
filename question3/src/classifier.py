def classify_document(text):
    if "aadhaar" in text.lower():
        return "Aadhaar Card"
    elif "permanent account number" in text.lower() or "pan" in text.lower():
        return "PAN Card"
    elif "driving licence" in text.lower():
        return "Driving Licence"
    elif "passport" in text.lower():
        return "Passport"
    elif "nach mandate" in text.lower():
        return "NACH/ECS Mandate"
    elif "annexure form" in text.lower():
        return "FATCA Annexure"
    elif "benefit illustration" in text.lower():
        return "Benefit Illustration Declaration"
    elif "moral hazard" in text.lower():
        return "Moral Hazard Questionnaire"
    elif "multiple policies" in text.lower():
        return "Multiple Policies Consent"
    elif "suitability profiler" in text.lower():
        return "Suitability Profiler Declaration"
    else:
        return "Unknown"
