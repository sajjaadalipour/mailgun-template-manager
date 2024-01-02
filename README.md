# mailgun-template-script

Python script to migrate mailgun templates from a domain to another.

To run this script follow steps:

- Clone this project
- Replace these words with yours in **mailgun-template-migration.py** : `API_KEY`, `SOURCE_DOMAIN_URL`, `DESTINATION_DOMAIN_URL`
- Run `python3 mailgun-template-migration.py`

Sample config:

```payton
api_key = "key_asljdaspasdpasdas_fake"
from_url = 'https://api.mailgun.net/v3/mail.domain1.com'
to_url = 'https://api.mailgun.net/v3/mail.domain2.com'
```