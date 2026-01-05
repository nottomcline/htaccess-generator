# htaccess-generator

This project provides a Python script to generate or update `.htaccess` files for basic authentication, simplifying the process of securing web directories.

## Workflow

Follow these steps to set up basic authentication for your web directory:

1.  **Prepare your web directory:**
    *   Place your `index.php` (or any other web-accessible file you want to protect) in the dedicated web directory you intend to secure. This is where the generated `.htaccess` file will reside.

2.  **Determine AuthUserFile Path:**
    *   Identify the absolute path to your `.htpasswd` file. This file contains the usernames and encrypted passwords for authentication. For example: `/var/www/html/auth/.htpasswd`.

3.  **Install Dependencies:**
    *   Ensure you have `passlib` installed, which is required by the Python script:
        ```bash
        pip install passlib
        ```

4.  **Execute the Generator Script:**
    *   Run the Python script `htaccess_generator.py`, providing the necessary information when prompted. The script will generate or update the `.htaccess` file in your target directory.
        ```bash
        python htaccess_generator.py
        ```
    *   The script will prompt you for:
        *   The directory to protect (where `index.php` is located).
        *   The `AuthUserFile` path (from step 2).
        *   Usernames and passwords to add to the `.htpasswd` file.

5.  **Verify `.htaccess`:**
    *   After the script runs, a `.htaccess` file will be created or updated in your specified web directory, configuring basic authentication.
