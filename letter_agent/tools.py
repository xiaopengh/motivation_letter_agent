def analyze_user_profile(profile_file: str) -> dict:
    """Analyzes the user's profile/CV/resume to extract relevant information."""
    user_profile = ""
    try:
        with open(profile_file, "r", encoding="utf-8") as f:
            user_profile = f.read()
    except FileNotFoundError:
        return {"error": f"Profile file not found: {profile_file}"}
    except UnicodeDecodeError:
        with open(profile_file, "r", encoding="latin-1") as f:
            user_profile = f.read()

    return {"user_profile": user_profile}


def save_motivation_letter(letter: str, filename: str) -> dict:
    """Saves the motivation letter to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(letter)
        return {"status": "success", "message": f"Letter saved to {filename}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def load_opportunity_info(info_file: str) -> dict:
    """Loads information about the job/scholarship/program opportunity."""
    opportunity_info = ""
    try:
        with open(info_file, "r", encoding="utf-8") as f:
            opportunity_info = f.read()
    except FileNotFoundError:
        return {"error": f"Opportunity info file not found: {info_file}"}
    except UnicodeDecodeError:
        with open(info_file, "r", encoding="latin-1") as f:
            opportunity_info = f.read()

    return {"opportunity_info": opportunity_info}
