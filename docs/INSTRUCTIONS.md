# GRC Control Gap Analyzer: Execution Instructions

This guide provides instructions for setting up and running the Automated GRC Control Gap Analyzer utility. This tool is designed to quickly identify missing security controls by comparing a defined checklist against a vendor's documented policies.

## 1. Prerequisites

1. **Python:** Python 3.x must be installed on your system.
2. **Git:** Basic Git knowledge or the use of an integrated development environment (IDE) like VS Code for cloning the repository.

## 2. Setup

1. **Clone the Repository:**
 ```bash
 git clone [Your HTTPS Git URL Here]
 cd GRC-Automated-Control-Gap-Analyzer
 ```
2. **Verify Directory Structure:** Ensure the following folders exist in the project root:
 * `controls/` (Input files)
 * `reports/` (Output files)
 * `docs/` (Documentation)

## 3. Input Data Configuration

The analysis relies on two primary input files located in the `controls/` directory:

| File Name | Purpose | Format |
| :--- | :--- | :--- |
| `required_controls.txt` | The authoritative list of mandatory security controls. | One control requirement per line. |
| `vendor_profile.txt` | The target vendor's self-assessment or policy document text. | Single body of text, all content will be converted to lowercase for comparison. |

**NOTE:** For a successful analysis, the unique keywords in your control list must be present in the vendor's profile text for a 'Compliant' finding.

## 4. Execution

1. Open your terminal or command prompt in the root of the project directory.
2. Run the main Python script:
 ```bash
 python gap_analyzer.py
 ```

## 5. Interpreting the Report

Upon completion, a summary will be printed to the console, and a detailed audit report will be saved to the **`reports/`** directory with a timestamped filename (e.g., `gap_report_YYYY-MM-DD_HHMMSS.txt`).

The report contains:

* **Summary Metrics:** Total controls, compliant controls, and the number of identified gaps.
* **Detailed Gaps:** A prioritized list of required controls that were **not** found within the `vendor_profile.txt`. These represent areas of high risk and require immediate follow-up (e.g., remediation, compensating controls, or risk acceptance).

---