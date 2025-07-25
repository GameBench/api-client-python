```
python3 -m venv env
. env/bin/activate

pip install -r requirements.txt

export GB_API_BASE_URL=
export GB_API_EMAIL=
export GB_API_TOKEN=
export GB_COMPANY_ID=

python example.py
```

## Clearing up old session data

```
python3 -m venv env
. env/bin/activate

pip install requests click python-dateutil

# Set to the value of your API token, or you will be prompted upon running the command
export GB_API_TOKEN=

python delete-old-sessions.py --company-id <company id> --api-email <API email>

Use python `delete-old-sessions.py --help` for usage instructions such as filtering by app package name
```
