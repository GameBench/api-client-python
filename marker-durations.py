from client import ApiClient
import os

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

markers = client.getSessionMarkers('8ca1ba23-4de5-4701-9482-23e618543e46')

print("Session has", len(markers), "markers")
print()

print(f"{'Label':<12} {'Start':<6} {'End':<6} {'Duration':<8}")
print("-" * 34)

for marker in markers:
    duration = marker['tsEnd'] - marker['tsStart']
    print(f"{marker['label']:<12} {marker['tsStart']:<6} {marker['tsEnd']:<6} {duration:<8}")
