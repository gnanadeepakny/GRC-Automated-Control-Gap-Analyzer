# GRC Automated Control Gap Analyzer

### Project Overview
This project is a lightweight, scalable Python utility designed to automate the initial phase of **Third-Party Risk Management (TPRM)** and internal compliance **Audits**. It accelerates the crucial process of identifying control gaps by comparing a pre-defined set of required security controls (mapped to standards like **NIST CSF** or **ISO 27001**) against a target organization's documented policies or self-assessment responses.

This tool demonstrates a practical, scalable approach to GRC that reduces manual effort and enforces a data-driven security posture.

### Key Features & Value Proposition

| Feature | GRC/TPRM Value |
| :--- | :--- |
| **Core Audit Automation** | Eliminates manual comparison of control requirements against policy text, significantly reducing initial assessment time. |
| **Risk Prioritization Ready** | The output is a clear list of missing controls, immediately usable for risk prioritization and remediation planning. |
| **Robust Matching Logic** | Uses keyword-based search to ensure accurate, case-insensitive comparison, mitigating false negatives from minor formatting differences. |
| **Professional Reporting** | Generates a clean, timestamped output file (`.txt`) suitable for direct use as an audit artifact. |

---

### Technologies Used

* **Python 3:** Core logic, file I/O, and string manipulation.
* **Fundamental GRC/TPRM Principles:** Application of control frameworks (NIST CSF, ISO 27001) and risk identification.

### How to Run the Analyzer

1. **Clone the Repository:**
 ```bash
 git clone https://github.com/gnanadeepakny/GRC-Automated-Control-Gap-Analyzer.git
 cd GRC-Automated-Control-Gap-Analyzer
 ```
2. **Configure Input:** Edit the files in the `controls/` directory:
 * `required_controls.txt`: Define your mandatory security requirements (one per line).
 * `vendor_profile.txt`: Paste the vendor's policy text or security response.
3. **Execute:** Run the main script from the root directory:
 ```bash
 python gap_analyzer.py
 ```
4. **Review Output:** The final report, detailing the summary and list of gaps, will be saved to the **`reports/`** directory.

### Project Files

* `gap_analyzer.py`: Main script containing all logic.
* `controls/`: Input files for controls and vendor data.
* `reports/`: Output directory for timestamped `gap_report_*.txt` files.
* `docs/INSTRUCTIONS.md`: Detailed setup and usage instructions.