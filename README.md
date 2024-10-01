# Python Directory Enumeration Tool

A simple Python tool for **directory enumeration** designed for web penetration testing. This tool is faster than Burp Suite Community Edition for discovering hidden directories.


## How It Works

1. Get the target URL from the user.
2. Process a wordlist to create potential paths.
3. Send requests for each path.
4. Log paths that respond with a `200 OK` status.
5. Save the results to a file.

### Example

Run the tool:

```bash
python main.py
```

Input a target like `http://yogenc.com`, and it will check paths like:

- `http://yogenc.com/admin`
- `http://yogenc.com/config`
- `http://yogenc.com/login`


This version is more straightforward and focuses on the essential information. Let me know if you want to make any further adjustments!
