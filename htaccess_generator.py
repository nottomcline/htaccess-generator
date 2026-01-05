import os
from getpass import getpass
from passlib.apache import HtpasswdFile

OUTPUT_DIR = "./auth"
REALM = "Beta Access"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    username = input("Username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty")

    password = getpass("Password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        raise ValueError("Passwords do not match")

    htpasswd_path = os.path.join(OUTPUT_DIR, ".htpasswd")
    htaccess_path = os.path.join(OUTPUT_DIR, ".htaccess")
    creds_path = os.path.join(OUTPUT_DIR, "credentials.txt")

    # Generate Apache-compatible .htpasswd
    ht = HtpasswdFile()
    ht.set_password(username, password)
    ht.save(htpasswd_path)

    # Write .htaccess without AuthUserFile
    with open(htaccess_path, "w") as f:
        f.write(
            f"""AuthType Basic
AuthName "{REALM}"
AuthUserFile #copy correct path here
Require valid-user
"""
        )

    # Optional credentials reference (DO NOT UPLOAD)
    with open(creds_path, "w") as f:
        f.write(
            f"""Username: {username}
Password: {password}
"""
        )

    print("\nFiles generated successfully:")
    print(f"  {htaccess_path}  → upload to /beta (update AuthUserFile manually)")
    print(f"  {htpasswd_path}  → upload to /private")
    print("\nUse your PHP check to determine the correct AuthUserFile path.")


if __name__ == "__main__":
    main()
