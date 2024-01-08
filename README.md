# Mailgun Template Manager

## Description

Mailgun Template Manager is a Python command-line interface (CLI) tool designed for managing email templates in your
Mailgun accounts. It allows for copying, downloading, uploading, and deleting all templates from specified Mailgun
accounts.

## Features

- **Copy Templates**: Copy all templates from one Mailgun account to another.
- **Delete All Templates**: Remove all templates from a specified Mailgun account.
- **Download Templates**: Download all templates from a specified Mailgun account and save them to a local JSON file.
- **Upload Templates**: Upload templates from a local JSON file to a specified Mailgun account.

## Requirements

- Python 3.x
- `requests` library (Install using `pip install requests`)
- Mailgun account with API access

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository to your local machine.
3. Install required Python packages:
   ```bash
   pip install requests

## Usage

### Configuration

First, you'll need to have your Mailgun API key and the URLs of your Mailgun accounts. Replace the placeholders in the
script with your actual Mailgun API details:

* API_KEY: Your Mailgun API key.
* SOURCE_ACCOUNT_URL: The URL of your source Mailgun account.
* DESTINATION_ACCOUNT_URL: The URL of your destination Mailgun account.

### Commands

#### Copy

```bash
python script.py copy --apiKey YOUR_API_KEY --sourceAccountUrl SOURCE_URL --destinationAccountUrl DESTINATION_URL
```

#### Delete All

```bash 
python3 script.py deleteAll --apiKey YOUR_API_KEY --accountUrl ACCOUNT_URL
```

#### Download

```bash
python3 script.py download --apiKey YOUR_API_KEY --accountUrl ACCOUNT_URL
```

#### Upload

```bash
python3 script.py upload --apiKey YOUR_API_KEY --accountUrl ACCOUNT_URL --filePath FILE_PATH
```

> Replace these `YOUR_API_KEY`, `SOURCE_URL`, `DESTINATION_URL`, `ACCOUNT_URL`, `FILE_PATH`   with your actual params
> value.

## Detailed Function Descriptions

* `copy(api_key, source_account_url, destination_account_url)`: Copies all templates from the source account to the
  destination account.
* `delete_all(api_key, account_url)`: Deletes all templates from the specified account after confirmation.
* `download(api_key, account_url)`: Downloads all templates from the specified account and saves them as a local JSON
  file.
* `upload(api_key, account_url, file_path)`: Uploads templates from a local JSON file to the specified Mailgun account.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

MIT License - Feel free to use and modify the script as needed for your personal or commercial projects.

## Disclaimer

This tool is provided as-is, and while it has been tested, the creators are not responsible for any misuse or data loss.
Please ensure you understand the operations it performs before using it on your live Mailgun accounts.

## Contact

For any questions, feedback, or concerns, please contact by my gmail: `sajjaad.alipour@gmail.com.`

Thank you for using the Mailgun Template Manager!