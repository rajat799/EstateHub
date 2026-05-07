"""
EstateHub — One-Time Password Hashing Migration Script
=======================================================
This script converts all existing plain-text passwords in the database
to Django's hashed format (PBKDF2 with SHA256).

USAGE:
    On PythonAnywhere (or locally):
    $ cd /home/EstateHub/EstateHub
    $ python manage.py shell < hash_existing_passwords.py

    Or in the Django shell:
    >>> exec(open('hash_existing_passwords.py').read())

WARNING:
    - Run this ONCE after deploying the new code
    - Running it twice will double-hash passwords (making them invalid)
    - Back up your database before running!

SAFETY:
    - The script detects already-hashed passwords and skips them
    - Django hashed passwords start with 'pbkdf2_sha256$' or similar prefixes
"""

import os
import sys
import django

# Setup Django if running standalone
if 'django' not in sys.modules or not hasattr(django, 'apps'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    django.setup()

from django.contrib.auth.hashers import make_password, is_password_usable
from app.models import Register, AdminMaster, AdminSeller


def is_already_hashed(password):
    """
    Check if a password is already in Django's hashed format.
    Django hashed passwords contain '$' separators and start with
    algorithm identifiers like 'pbkdf2_sha256$'.
    """
    if not password:
        return True  # Empty passwords, skip
    # Django hashed passwords typically start with these prefixes
    hash_prefixes = ('pbkdf2_sha256$', 'pbkdf2_sha1$', 'bcrypt$', 'argon2$', 'scrypt$')
    return password.startswith(hash_prefixes)


def hash_table_passwords(model, password_field, email_field, table_name):
    """Hash all plain-text passwords in a given model."""
    records = model.objects.all()
    total = records.count()
    hashed = 0
    skipped = 0
    errors = 0

    print(f"\n{'='*60}")
    print(f"Processing: {table_name} ({total} records)")
    print(f"{'='*60}")

    for record in records:
        password = getattr(record, password_field)
        email = getattr(record, email_field)

        if is_already_hashed(password):
            skipped += 1
            print(f"  SKIP (already hashed): {email}")
            continue

        try:
            setattr(record, password_field, make_password(password))
            record.save(update_fields=[password_field])
            hashed += 1
            print(f"  ✓ Hashed: {email}")
        except Exception as e:
            errors += 1
            print(f"  ✗ ERROR: {email} — {str(e)}")

    print(f"\nResults for {table_name}:")
    print(f"  Total:   {total}")
    print(f"  Hashed:  {hashed}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors:  {errors}")
    return hashed, skipped, errors


def main():
    print("\n" + "=" * 60)
    print("EstateHub — Password Hashing Migration")
    print("=" * 60)
    print("\nThis will convert ALL plain-text passwords to secure hashes.")
    print("Already-hashed passwords will be automatically skipped.\n")

    total_hashed = 0
    total_skipped = 0
    total_errors = 0

    # Hash User (Register) passwords
    h, s, e = hash_table_passwords(Register, 'us_password', 'us_email', 'Users (Register)')
    total_hashed += h; total_skipped += s; total_errors += e

    # Hash Admin (AdminMaster) passwords
    h, s, e = hash_table_passwords(AdminMaster, 'ad_password', 'ad_email', 'Admins (AdminMaster)')
    total_hashed += h; total_skipped += s; total_errors += e

    # Hash Seller (AdminSeller) passwords
    h, s, e = hash_table_passwords(AdminSeller, 's_password', 's_email', 'Sellers (AdminSeller)')
    total_hashed += h; total_skipped += s; total_errors += e

    print(f"\n{'='*60}")
    print(f"MIGRATION COMPLETE")
    print(f"{'='*60}")
    print(f"  Total hashed:  {total_hashed}")
    print(f"  Total skipped: {total_skipped}")
    print(f"  Total errors:  {total_errors}")

    if total_errors > 0:
        print("\n⚠️  Some passwords failed to hash. Check the errors above.")
    else:
        print("\n✅ All passwords have been securely hashed!")

    print(f"{'='*60}\n")


# Run the migration
main()
