import os
from datetime import datetime

# ===============================================
# 1. Configuration: Define File Paths
# ===============================================

# Use os.path.join for cross-platform compatibility
CONTROL_FILE = os.path.join('controls', 'required_controls.txt')
VENDOR_FILE = os.path.join('controls', 'vendor_profile.txt')
# Output will go to the 'reports' directory
REPORT_DIR = 'reports'

# ===============================================
# 2. Data Initialization Function
# ===============================================

def load_data():
    """Reads and processes data from input files."""
 
    # 2a. Load Required Controls
    try:
        with open(CONTROL_FILE, 'r', encoding='utf-8') as f:
            # Read each line, strip excess whitespace/newlines, and convert to a list of strings
            required_controls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Required controls file not found at {CONTROL_FILE}")
        return None, None
 
    # 2b. Load Vendor Profile Text
    try:
        with open(VENDOR_FILE, 'r', encoding='utf-8') as f:
            # Read the entire vendor document into a single, clean string, 
            # and convert it to lowercase for case-insensitive matching later.
           vendor_text = f.read().replace('\n', ' ').strip().lower()
    except FileNotFoundError:
        print(f"Error: Vendor profile file not found at {VENDOR_FILE}")
        return None, None
 
    print(f"Successfully loaded {len(required_controls)} required controls.")
 
    # Return the data we'll need for the next step (gap analysis)
    return required_controls, vendor_text


# ===============================================
# 3. Main Execution Block (for testing)
# ===============================================

if __name__ == "__main__":
    print("--- Starting GRC Control Gap Analyzer Setup ---")
 
    # Check if the reports directory exists, create it if not (Error Handling)
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        print(f"Created output directory: {REPORT_DIR}")

    # Load the data
    controls, vendor_data = load_data()
 
    # Simple check to confirm data loaded (for today's test)
    if controls and vendor_data:
        print("\n--- TEST SUCCESSFUL ---")
        print(f"First 3 Controls: {controls[:3]}")
        print(f"Vendor data length: {len(vendor_data)} characters")
        print("Ready for gap analysis on Day 4!")
    else:
        print("\n--- TEST FAILED: Check file names and paths. ---")