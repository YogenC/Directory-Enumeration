A simple Python tool for **directory enumeration** designed for web penetration testing. This tool is faster than Burp Suite Community Edition for discovering hidden directories.

## Features

- **HTTP Requests**: Uses the `requests` library to send HTTP requests.
- **Customizable Target**: Specify a target URL based on user input.
- **Wordlist Support**: Use a custom wordlist or a default one to check for paths.
- **Status Code Checking**: Checks HTTP status codes to identify valid paths.
- **Logging**: Logs paths that return a `200 OK` status.
- **Results Saving**: Saves found paths to a text file.

## How It Works

1. Get the target URL from the user.
2. Process a wordlist to create potential paths.
3. Send requests for each path.
4. Log paths that respond with a `200 OK` status.
5. Save the results to a file.

### Example

Run the tool:

```bash
python directory_enum.py
```

Input a target like `http://yogenc.com`, and it will check paths like:

- `http://yogenc.com/admin`
- `http://yogenc.com/config`
- `http://yogenc.com/login`



This version is more straightforward and focuses on the essential information. Let me know if you want to make any further adjustments!
