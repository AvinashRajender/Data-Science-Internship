import re

def extract_fields(doc_type, text):
    fields = {}

    if doc_type == "Aadhaar Card":
        fields["Aadhaar_Number"] = re.search(r"\d{4}\s\d{4}\s\d{4}", text)
        fields["Full_Name"] = re.search(r"Name[:\s]*([A-Za-z\s]+)", text)
        fields["Date_of_Birth"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Address"] = re.search(r"Address[:\s]*(.+)", text)

    elif doc_type == "PAN Card":
        fields["PAN_Number"] = re.search(r"[A-Z]{5}\d{4}[A-Z]", text)
        fields["Full_Name"] = re.search(r"Name[:\s]*([A-Za-z\s]+)", text)
        fields["Father_Name"] = re.search(r"Father.*[:\s]*([A-Za-z\s]+)", text)
        fields["Date_of_Birth"] = re.search(r"\d{2}/\d{2}/\d{4}", text)

    elif doc_type == "Driving Licence":
        fields["DL_Number"] = re.search(r"[A-Z]{2}\d{2}\s\d{4}\s\d{7}", text)
        fields["Name"] = re.search(r"Name[:\s]*([A-Za-z\s]+)", text)
        fields["Date_of_Issue"] = re.search(r"DOI[:\s]*(\d{2}/\d{2}/\d{4})", text)
        fields["Valid_Till"] = re.search(r"Valid Till[:\s]*(\d{2}/\d{2}/\d{4})", text)

    elif doc_type == "Passport":
        fields["Passport_Number"] = re.search(r"[A-Z]\d{7}", text)
        fields["Date_of_Birth"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Date_of_Expiry"] = re.search(r"Expiry[:\s]*(\d{2}/\d{2}/\d{4})", text)
        fields["MRZ_Line2"] = re.search(r"\n([A-Z0-9<]+)\n", text)

    elif doc_type == "NACH/ECS Mandate":
        fields["Bank_Account_Number"] = re.search(r"\d{9,18}", text)
        fields["IFSC_Code"] = re.search(r"[A-Z]{4}0[A-Z0-9]{6}", text)
        fields["Bank_Name"] = re.search(r"Bank Name[:\s]*(.+)", text)
        fields["Amount"] = re.search(r"₹?\s?\d+[,\d]*", text)
        fields["Frequency"] = re.search(r"Frequency[:\s]*(.+)", text)

    elif doc_type == "FATCA Annexure":
        fields["Policy_Number"] = re.search(r"\d{10,}", text)
        fields["TIN_or_PAN"] = re.search(r"[A-Z]{5}\d{4}[A-Z]", text)
        fields["Father_Name"] = re.search(r"Father.*[:\s]*([A-Za-z\s]+)", text)
        fields["Place_of_Birth"] = re.search(r"Place of Birth[:\s]*(.+)", text)
        fields["Nationality"] = re.search(r"Nationality[:\s]*(.+)", text)

    elif doc_type == "Benefit Illustration Declaration":
        fields["Application_Number"] = re.search(r"\d{10,}", text)
        fields["Policyholder_Name"] = re.search(r"Name[:\s]*([A-Za-z\s]+)", text)
        fields["Date"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Place"] = re.search(r"Place[:\s]*(.+)", text)

    elif doc_type == "Moral Hazard Questionnaire":
        fields["Application_Number"] = re.search(r"\d{10,}", text)
        fields["Name_of_Life_Assured"] = re.search(r"Name.*[:\s]*([A-Za-z\s]+)", text)
        fields["Nominee_Relationship"] = re.search(r"Relationship[:\s]*(.+)", text)
        fields["Date"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Place"] = re.search(r"Place[:\s]*(.+)", text)

    elif doc_type == "Multiple Policies Consent":
        fields["Proposer_Name"] = re.search(r"Name[:\s]*([A-Za-z\s]+)", text)
        fields["Reason"] = re.search(r"Reason.*:\s*(.+)", text)
        fields["Date"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Place"] = re.search(r"Place[:\s]*(.+)", text)

    elif doc_type == "Suitability Profiler Declaration":
        fields["Application_Number"] = re.search(r"\d{10,}", text)
        fields["Name_of_Life_Assured"] = re.search(r"Name.*[:\s]*([A-Za-z\s]+)", text)
        fields["Agent_Name"] = re.search(r"Agent.*[:\s]*([A-Za-z\s]+)", text)
        fields["Date"] = re.search(r"\d{2}/\d{2}/\d{4}", text)
        fields["Place"] = re.search(r"Place[:\s]*(.+)", text)

    # Convert regex matches to values or None
    for key, match in fields.items():
        if match:
        # If regex has a capturing group, use it; else use the whole match
            try:
                fields[key] = match.group(1)
            except IndexError:
                fields[key] = match.group(0)
        else:
            fields[key] = None


    return fields
