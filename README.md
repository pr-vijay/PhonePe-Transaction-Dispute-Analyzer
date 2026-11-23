# PhonePe Transaction Dispute Analyzer 💳🔍

An end-to-end Python & Pandas data operations pipeline developed for PhonePe's Transaction Support Operations team. This system consolidates multi-source transaction, refund, and customer complaint data into a unified dispute resolution master table, detects multi-factor failure signals, and classifies disputes into prioritized support queues.

---

## 📌 Executive Summary & Business Objective

PhonePe processes millions of digital payment transactions every day. While the majority settle seamlessly, payment failures, delayed refunds, and unresolved customer disputes create substantial customer friction.

Historically, transaction data was siloed across three independent data sources:
* **`transactions.csv`**: Core payment logs (CSV)
* **`refunds.xlsx`**: Merchant and customer refund requests (Excel)
* **`customer_complaints.json`**: Support dispute tickets (JSON)

### The Solution:
This project builds an automated, robust data pipeline to:
1. Standardize and clean messy real-world data (duplicate IDs, case variations, invalid amounts).
2. Maintain referential integrity across all three datasets.
3. Pre-aggregate refunds and complaints to prevent row duplication upon merging.
4. Construct a unified **`dispute_master`** dataset (exactly 5,000 unique transactions).
5. Apply a **3-Signal Business Triage Rule** to classify disputes into **High**, **Medium**, and **Low** support priorities.
6. Export operational reports and executive findings for the Customer Support Operations Desk.

---

## 🚀 Key Business Findings & KPIs

* **Total Clean Transactions Analyzed**: `5,000`
* **Failed or Pending Transactions**: `1,453` (Representing ~₹14.28 Lakhs in stuck funds)
* **Transactions with Unresolved Refunds**: `699`
* **Transactions with Active/Repeat Complaints**: `949`
* **High-Priority Escalations Identified**: `535` transactions (requiring immediate senior support outreach)
* **Medium-Priority Transactions**: `1,998`
* **Low-Priority / Clean Transactions**: `2,467`
* **Payment Mode Risk**: **UPI** accounted for the largest volume of issues (600 Failed, 412 Pending transactions).
* **Geographic Concentration**: **Pune** (167 issues), **Chennai** (155 issues), and **Hyderabad** (153 issues) showed the highest transaction dispute density.

---

## 🏗️ 10-Milestone Development Architecture

| Milestone | Phase | Description | Key Tools / Pandas Methods |
| :---: | :--- | :--- | :--- |
| **M1** | Ingestion & Baseline Assessment | Load `transactions.csv`, inspect schema, identify initial duplicates and missing values. | `pd.read_csv`, `.shape`, `.nunique()`, `.isna().sum()` |
| **M2** | Multi-format Issue Inspection | Ingest `refunds.xlsx` and `customer_complaints.json`, uncover status casing inconsistencies. | `pd.read_excel`, `pd.read_json`, `.value_counts(dropna=False)` |
| **M3** | Transaction Cleansing | Deduplicate transaction IDs, standardize casing to Title Case, coerce datetime and numeric amounts, flag data review cases. | `.drop_duplicates()`, `.str.strip().str.title()`, `pd.to_datetime`, `pd.to_numeric` |
| **M4** | Issue & Refund Normalization | Deduplicate refunds and complaints, standardize status strings, check referential integrity against valid transactions. | `.isin(valid_tx)`, bitwise NOT `~` |
| **M5** | Exploratory Payment Behavior | Group by payment mode and customer city to detect failure clusters and financial exposure. | `.groupby().agg()`, `.assign()`, `.sort_values()` |
| **M6** | Refund Aggregation & Linkage | Pre-aggregate refund counts and amounts per `transaction_id`, left join with transactions without row duplication. | `.groupby('transaction_id').agg()`, `.merge(how='left', validate='1:1')`, `.fillna(0)` |
| **M7** | Complaint Analysis & Repeat Tracking | Aggregate complaints per transaction, isolate customers and transactions with repeat complaints (> 1). | `.isin(['Open', 'In Progress'])`, `.groupby().size()` |
| **M8** | Unified Dispute Master Table | Merge transactions, refunds, and complaints into a single 15-column master table; enforce strict validation assertions. | `.merge()`, `assert dispute_master['transaction_id'].is_unique` |
| **M9** | Multi-Signal Priority Classification | Compute boolean issue signals (`payment_issue`, `refund_issue`, `complaint_issue`) and classify priority using `np.select`. | `np.select()`, `.reindex()` |
| **M10** | Export & Operational Reporting | Categorically sort final report by priority and transaction ID; export clean production CSV reports to `phonepe_reports/`. | `pd.Categorical()`, `.to_csv()` |

---

## 🎯 Priority Classification Logic

The system evaluates three distinct failure signals for every transaction:

```
Signal 1: payment_issue   = Transaction status is 'Failed' or 'Pending'
Signal 2: refund_issue    = Unresolved refund count > 0 (Pending or Failed refund)
Signal 3: complaint_issue = Repeat complaints (> 1) OR Unresolved complaint count > 0

Total Signals = payment_issue + refund_issue + complaint_issue  (Range: 0 to 3)
```

### Classification Rules:
* 🔴 **High Priority** ($\ge 2$ signals): Multiple compounding points of failure (e.g. Failed payment + stuck refund + customer complaint).
* 🟡 **Medium Priority** ($= 1$ signal): Single isolated failure requiring standard support turnaround.
* 🟢 **Low Priority** ($= 0$ signals): Successful or resolved transactions requiring no support action.

---

## 📁 Repository Structure

```text
.
├── phonepe_reports/
│   ├── phonepe_transaction_dispute_report.csv  # Final prioritized dispute master dataset
│   └── phonepe_dispute_priority_summary.csv   # High/Medium/Low executive summary counts
├── transactions.csv                           # Raw payment transactions dataset
├── refunds.xlsx                               # Raw refund requests dataset
├── customer_complaints.json                   # Raw customer complaints dataset
├── PhonePe_Transaction_Dispute_Analyzer.ipynb # Completed pipeline notebook with all visible outputs
├── PhonePe_Dispute_Analyzer_Workspace.ipynb   # Interactive development workspace
├── .gitignore                                 # Clean version control exclusions
└── README.md                                  # Project documentation & architecture overview
```

---

## ⚙️ How to Run Locally

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Install Dependencies
```bash
pip install pandas numpy openpyxl jupyter ipykernel
```

### 3. Run the Jupyter Notebook
```bash
jupyter notebook PhonePe_Transaction_Dispute_Analyzer.ipynb
```
Select **Kernel $\rightarrow$ Restart & Run All** to generate the reports and visible analysis tables.

---

## 👤 Author
* **Developer**: P.R. Vijay (`prvijaydev-bli`)
* **Project**: PhonePe Transaction Dispute Analyzer (AlmaBetter Industrial Capstone)
