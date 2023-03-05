import sys
import hvac

# Set the URL and authentication method for your Vault server
vault_url = "http://localhost:8200/"
auth_method = "token"
auth_token = "dev-only-token"

# Authenticate to Vault
if auth_method == "token":
    client = hvac.Client(url=vault_url, token=auth_token)
else:
    # Other authentication methods require additional configuration
    pass

read_response = client.secrets.kv.read_secret_version(path='my-secret-login')

username = read_response['data']['data']['username']
password = read_response['data']['data']['password']

# Confirm that the value we unpacked from the read response is correct
if username != 'Angry_Hashi' or password != 'Hashi123':
    sys.exit('unexpected password')

print('Access granted!')
