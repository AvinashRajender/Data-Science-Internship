import re

def validate_field(field_name, value):
    """
    Returns a confidence score (0–1) based on regex validation and presence.
    """
    if not value:
        return 0.0

    patterns = {
        "Aadhaar_Number": r"^\d{4}\s\d{4}\s\d{4}$",
        "PAN_Number": r"^[A-Z]{5}\d{4}[A-Z]$",
        "Passport_Number": r"^[A-Z]\d{7}$",
        "DL_Number": r"^[A-Z]{2}\d{2}\s\d{4}\s\d{7}$",
        "IFSC_Code": r"^[A-Z]{4}0[A-Z0-9]{6}$",
        "Date_of_Birth": r"^\d{2}/\d{2}/\d{4}$",
        "Date": r"^\d{2}/\d{2}/\d{4}$",
    }

    # If we have a regex for this field, check format
    if field_name in patterns:
        if re.match(patterns[field_name], value.strip()):
            return 0.95  # high confidence
        else:
            return 0.5   # partial match, low confidence

    # Default: presence only
    return 0.8 if value.strip() else 0.0


def score_fields(fields):
    """
    Takes a dict of fields and returns dict with confidence + needs_review flag.
    """
    scored = {}
    needs_review = False

    for key, value in fields.items():
        confidence = validate_field(key, value)
        scored[key] = {"value": value, "confidence": confidence}
        if confidence < 0.8:
            needs_review = True

    return scored, needs_review
