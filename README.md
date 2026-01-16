# Age Bold – Eligibility Pipeline (PySpark / Databricks)

## Overview
This project implements a configuration-driven data ingestion pipeline using PySpark for Databricks.  
It processes eligibility files from multiple healthcare partners with different formats and outputs a unified, standardized dataset ready for analytics.

## Features
- Configuration-driven (no hardcoding per partner)
- Handles multiple delimiters & date formats
- Standardizes names, dates, email, and phone formats
- Flexible for onboarding new partners
- Basic validation on `external_id`

## How to Run (Databricks)
1. Upload partner files to DBFS (`/FileStore/tables/`)
2. Update `PARTNER_CONFIG` with file paths & format settings
3. Run the notebook or script
4. View the final standardized dataset

## Adding New Partners
To add support for a new partner:
- Add a new entry in `PARTNER_CONFIG`
- Define `delimiter`, `column_mapping`, and `dob_input_format`
No changes are needed in the core logic.

## Outputs
The final output has:
`external_id, first_name, last_name, dob, email, phone, partner_code`
