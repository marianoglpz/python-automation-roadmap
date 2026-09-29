# Email Cleaner and Validator

correos_raw = [
    "  juan.perez@EMPRESA.com ",
    "CORREO_INVALIDO.com",
    "maria.gomez@empresa.com",
    "   pedro.alvarez@OTRODOMINIO.COM  ",
    "admin@empresa.com",
    "usuario_sin_arroba_gmail.com"
]

emails_by_domain = {}
invalid_emails = []

for email in correos_raw:

    # 1. Clean the email
    email_clean = email.strip().lower()

    # 2. Validate that it has exactly one @
    if email_clean.count("@") != 1:
        invalid_emails.append(email_clean)
        continue # This email is no longer valid. Stop processing it and move on to the next email.

    # 3. Separate user and domain
    user, domain = email_clean.split("@")

    # 4. Validate that the domain has a dot
    if "." not in domain:
        invalid_emails.append(email_clean)
        continue

    # 5. Group the email by domain
    if domain not in emails_by_domain: # Does `"empresa.com"` not yet exist as a key in my dictionary? -> If it doesn't exist -> create it -> and add the email.
        emails_by_domain[domain] = []

    emails_by_domain[domain].append(email_clean)


print("Valid emails grouped by domain:")
print(emails_by_domain)

print("\nInvalid emails:")
print(invalid_emails)
