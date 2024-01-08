import argparse
import json

from mailgun_api import MailgunApi


def copy(api_key, source_account_url, destination_account_url):
    # Add your logic to copy data from one account to another
    print(f"Copying templates from {source_account_url} to {destination_account_url} using API key {api_key}")

    source_api = MailgunApi(api_key, source_account_url)
    destination_api = MailgunApi(api_key, destination_account_url)

    source_account_templates = source_api.list_templates()

    if source_account_templates.status_code == 200:
        templates = source_account_templates.json()["items"]
        for template in templates:
            template_name = template["name"]
            # Create template in destination account
            destination_api.create_template(template_name, template["description"])

            versions = source_api.get_template_versions(template_name)
            for version in versions:
                template_version_detail = source_api.get_template_version(template_name, version["tag"])

                # Create version in destination account
                destination_api.create_version(template_name, template_version_detail)

            print(f"Template {template_name} done \n")
    else:
        print("Error fetching templates from source domain.")


def delete_all(api_key, account_url):
    confirm = input(f"Are you sure you want to delete all templates from {account_url}? Type 'yes' to confirm: ")
    if confirm.lower() == 'yes':
        # Add your logic to delete all data from an account
        print(f"Deleting all templates from {account_url} using API key {api_key}")
        api = MailgunApi(api_key, account_url)
        api.delete_all_templates()
    else:
        print("Operation canceled.")

    print(f"Deleting all templates from {account_url} using API key {api_key}")


def download(api_key, account_url):
    # Add your logic to download data from an account
    print(f"Downloading templates from {account_url} using API key {api_key}")
    api = MailgunApi(api_key, account_url)

    templates = api.list_templates().json()["items"]

    for template in templates:
        template_name = template["name"]

        versions = api.get_template_versions(template_name)
        template['versions'] = []
        for version in versions:
            template_version_detail = api.get_template_version(template_name, version["tag"])
            template['versions'].append(template_version_detail)

        print(f"Template {template_name} done \n")

    with open("templates.json", 'w') as file:
        file.write(json.dumps(templates, indent=4))


def upload(api_key, account_url, file_path):
    print(f"Uploading template file {file_path} to account {account_url} using API key {api_key}")

    api = MailgunApi(api_key, account_url)

    with open(file_path, 'r') as file:
        templates = json.load(file)

    for template in templates:
        template_name = template["name"]
        # Create template in destination account
        api.create_template(template_name, template["description"])

        for version in template["versions"]:
            api.create_version(template_name, version)

        print(f"Template {template_name} done \n")


def main():
    example_account = "https://api.mailgun.net/v3/mail.domain1.com"

    parser = argparse.ArgumentParser(description="Python CLI for managing MailGun templates.")

    # Subparsers for each operation
    subparsers = parser.add_subparsers(dest='command')

    # copy command
    copy_parser = subparsers.add_parser('copy', help='Copy templates from one account to another')
    copy_parser.add_argument('--apiKey', type=str, help='API key for authentication')
    copy_parser.add_argument('--sourceAccountUrl', type=str, help=f'Source account url, ex: {example_account}')
    copy_parser.add_argument('--destinationAccountUrl', type=str,
                             help=f'Destination account url, ex: {example_account}')

    # deleteAll command
    delete_parser = subparsers.add_parser('deleteAll', help='Delete all templates from an account')
    delete_parser.add_argument('--apiKey', type=str, help='API key for authentication')
    delete_parser.add_argument('--accountUrl', type=str,
                               help=f'Account url to delete templates from, ex: {example_account}')

    # download command
    download_parser = subparsers.add_parser('download',
                                            help=f'Download templates from an account, ex: {example_account}')
    download_parser.add_argument('--apiKey', type=str, help='API key for authentication')
    download_parser.add_argument('--accountUrl', type=str,
                                 help=f'Account ID to download data from, ex: {example_account}')

    # upload command
    download_parser = subparsers.add_parser('upload',
                                            help=f'Upload templates to an account, ex: {example_account}')
    download_parser.add_argument('--apiKey', type=str, help='API key for authentication')
    download_parser.add_argument('--accountUrl', type=str,
                                 help=f'Account ID to upload templates, ex: {example_account}')
    download_parser.add_argument('--filePath', type=str,
                                 help=f'Considered file path')

    # Parse the arguments
    args = parser.parse_args()
    # Call the appropriate function based on the command
    if args.command == 'copy':
        copy(args.apiKey, args.sourceAccountUrl, args.destinationAccountUrl)
    elif args.command == 'deleteAll':
        delete_all(args.apiKey, args.accountUrl)
    elif args.command == 'download':
        download(args.apiKey, args.accountUrl)
    elif args.command == 'upload':
        upload(args.apiKey, args.accountUrl, args.filePath)


if __name__ == '__main__':
    main()
