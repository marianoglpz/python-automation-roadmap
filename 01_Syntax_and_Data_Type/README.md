# 🐍 Module 01: Syntax and Data Types

This module covers fundamental Python syntax, data structure manipulations, and defensive error handling for automation tasks.

# 📧 Exercise 01: Email Cleaner and Validator

A Python script designed to process raw, unformatted email lists, validate their syntax, and categorize valid emails by domain while isolating invalid entries.

## 🛠️ Exercise Requirements
* Clean each email string by removing leading/trailing whitespaces and converting it to lowercase.
* Validate that each email contains **exactly one `@`** symbol and a valid domain format (a dot `.` after the `@`).
* Group valid emails into a dictionary where the keys are the domain names (e.g., `company.com`) and the values are lists of emails.
* Store all invalid email strings in a separate list (`invalid_emails`).

## 🧠 Pseudocode
1. Initialize an empty dictionary `emails_by_domain` and an empty list `invalid_emails`.
2. Iterate through each raw email in `raw_emails`:
   - Strip whitespace and convert the string to lowercase.
   - Check if `@` count is not equal to 1. If true, append to `invalid_emails` and continue.
   - Split the string into `user` and `domain` using `@`.
   - Check if `.` is not in `domain`. If true, append to `invalid_emails` and continue.
   - If `domain` is not yet a key in `emails_by_domain`, initialize it with an empty list.
   - Append the cleaned email to `emails_by_domain[domain]`.
3. Output the structured dictionary and invalid email list.

---

# 📊 Exercise 02: Sales Record Processor with Error Handling

A defensive Python script that parses raw sales records containing missing or corrupted data types, calculating totals securely without crashing.

## 🛠️ Exercise Requirements
* Process a list of dictionaries representing sales records with key-value pairs for `id`, `product`, and `monto` (amount).
* Safely convert each string/null `monto` value into a float using `try-except` exception handling.
* Catch `ValueError` and `TypeError` exceptions to log warning messages for corrupted records (e.g., `"N/A"` or `None`) and skip them without terminating execution.
* Return the cumulative total sales amount and the count of successfully processed records.

## 🧠 Pseudocode
1. Define function `process_sales(records)` initializing `total_amount = 0` and `successful_count = 0`.
2. Iterate through each `record` in `records`:
   - Begin a `try` block:
     - Convert `record["monto"]` to float.
     - Add converted float value to `total_amount`.
     - Increment `successful_count` by 1.
   - Begin an `except (ValueError, TypeError)` block:
     - Print a warning message specifying the skipped record's `id`.
     - Continue to the next iteration.
3. Return `total_amount` and `successful_count`.
4. Call function with sample data and display formatted total sum and count.
