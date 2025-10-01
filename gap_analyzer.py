import os
from datetime import datetime

# ---------------------------------------------------------------------
# GRC-Automated-Control-Gap-Analyzer
# Purpose: Compares a set of required security controls against a vendor policy document to automate third-party risk assessment.
# Author: GnanaDeepak Yadav Nammi
# ---------------------------------------------------------------------

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
    """Reads input data, converting vendor text to lowercase for analysis."""
 
    # 1. Load Required Controls
    try:
        with open(CONTROL_FILE, 'r', encoding='utf-8') as f:
            # Read each line, strip excess whitespace/newlines, and ensure the line isn't empty
            required_controls = [line.strip() for line in f if line.strip()]
 
        if not required_controls:
            print(f"Warning: The required controls file ({CONTROL_FILE}) is empty.")
            return None, None
 
    except FileNotFoundError:
        print(f"Error: Required controls file not found at {CONTROL_FILE}")
        return None, None
 
    # 2. Load Vendor Profile Text (converted to lowercase)
    try:
        with open(VENDOR_FILE, 'r', encoding='utf-8') as f:
            # Read the entire vendor document into a single, clean, lowercase string
            vendor_text = f.read().replace('\n', ' ').strip().lower()

        if not vendor_text:
            print(f"Warning: The vendor profile file ({VENDOR_FILE}) is empty.")
            return None, None
 
    except FileNotFoundError:
        print(f"Error: Vendor profile file not found at {VENDOR_FILE}")
        return None, None
 
    return required_controls, vendor_text

# --- NEW: Dictionary for robust keyword searching ---
# Map the full control text to a concise, unique phrase expected in the vendor document.
control_keywords = {
    "Multi-Factor Authentication (MFA) is enforced for all external access.": "multi-factor authentication (mfa)",
    "Data at rest is encrypted using AES-256 or stronger cipher.": "data at rest is encrypted",
    "Annual independent penetration testing is conducted and remediation tracked.": "annual independent penetration testing",
    "Formal vendor offboarding process exists and is tested.": "vendor offboarding process",
    "System access logs are retained for a minimum of 90 days.": "logs are retained for a minimum of 90 days",
    "Disaster Recovery (DR) plan is tested annually.": "dr plan is tested annually",
    "All systems are patched within 30 days of critical vulnerability release.": "patched within 30 days of critical vulnerability",
    "Employee background checks are conducted pre-hire.": "employee background checks",
    "Security awareness training is mandatory every 12 months.": "security awareness training is mandatory every 12 months",
    "Customer data is logically segmented from other client data.": "data is logically segmented",
    "A formal Incident Response (IR) plan is documented and tested.": "incident response (ir) plan is documented and tested",
    "Data is backed up daily and stored offsite or in a separate zone.": "data is backed up daily",
    "WAF (Web Application Firewall) is deployed for all internet-facing apps.": "waf (web application firewall) is deployed",
    "Data processing agreements (DPAs) are in place for PII handling.": "data processing agreements (dpas)",
    "Formal risk register reviewed by management quarterly.": "formal risk register reviewed by management quarterly",
    "Principle of Least Privilege is applied to all user accounts.": "principle of least privilege is applied",
    "Code changes require formal peer review and approval before deployment.": "code changes require formal peer review",
    "Data encryption keys are managed and rotated using a centralized vault.": "data encryption keys are managed and rotated",
    "Vulnerability scans are performed monthly against all production assets.": "vulnerability scans are performed monthly",
    "Security configuration baselines are defined and enforced (e.g., CIS Benchmarks).": "security configuration baselines are defined and enforced",
    "Termination of access is performed within 2 hours of employee separation.": "termination of access is performed within 2 hours",
    "Media (e.g., hard drives) containing sensitive data is securely wiped or destroyed.": "media containing sensitive data is securely wiped",
    "Network intrusion detection systems (IDS) monitor key segments.": "network intrusion detection systems (ids) monitor key segments",
    "Vendors must provide documented evidence of their own sub-processor oversight.": "vendors must provide documented evidence of their own sub-processor oversight",
    "Business Impact Analysis (BIA) is performed to determine system criticality.": "business impact analysis (bia) is performed",
}


def analyze_gaps(required_controls, vendor_text):
    """
    Compares required controls against vendor text using predefined keywords 
    to identify missing controls more robustly.
    """
    identified_gaps = []
 
    # Use the static control_keywords map defined above
    for control, search_term in control_keywords.items():
        # NOTE: We use keyword mapping instead of the full control text 
        # for robust, case-insensitive, and flexible matching against the vendor document.

        # Check if the search term is NOT found in the vendor's policy text
        if search_term not in vendor_text:
            identified_gaps.append(control)
 
    return identified_gaps

def generate_report(gaps, required_controls):
    """Writes the identified gaps to a dated, professional report file."""
 
    # Create a unique filename with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_filename = os.path.join(REPORT_DIR, f"gap_report_{timestamp}.txt")
 
    total_controls = len(required_controls)
    gaps_found = len(gaps)
    compliant_count = total_controls - gaps_found
 
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(f"GRC CONTROL GAP ANALYSIS REPORT\n")
        f.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
 
        # Summary Section
        f.write("--- SUMMARY ---\n")
        f.write(f"Total Controls Required: {total_controls}\n")
        f.write(f"Controls Found Compliant: {compliant_count}\n")
        f.write(f"Control Gaps Identified: {gaps_found}\n")
        f.write("-" * 50 + "\n\n")
 
        # Detailed Gaps Section
        if gaps:
            f.write("--- DETAILED CONTROL GAPS (HIGH RISK) ---\n")
            for i, gap in enumerate(gaps, 1):
                f.write(f"{i}. [MISSING] {gap}\n")
        else:
            f.write("CONGRATULATIONS: No significant control gaps were identified.\n")

    return report_filename
# ===============================================
# 3. Main Execution Block (for testing)
# ===============================================

if __name__ == "__main__":
 
    # Check if the reports directory exists, create it if not (Error Handling)
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        print(f"Created output directory: {REPORT_DIR}")

    print("--- Starting GRC Control Gap Analyzer ---")
 
    # Load the data
    controls, vendor_data = load_data()
 
    if controls and vendor_data:
        print(f"Successfully loaded {len(controls)} required controls.")
 
        # --- NEW CODE: Run the Core Analysis ---
        print("\nInitiating Gap Analysis...")
 
        # Call the new analysis function
        gaps = analyze_gaps(controls, vendor_data)
 
        # Print the results to the console (Updated for Day 5)
        if gaps:
            # Generate the professional report file
            report_path = generate_report(gaps, controls)
 
            print(f"\n--- GAPS IDENTIFIED ---")
            print(f"Total Gaps Found: {len(gaps)}")
            print(f"Success! Report generated and saved to: {report_path}")
            print("\nDay 5 complete. Ready for final documentation and polish.")
 
        else:
            report_path = generate_report(gaps, controls)
            print(f"\nNo gaps identified. Compliant report saved to: {report_path}")

    else:
        print("\n--- ERROR --- Data loading failed. Check inputs.")