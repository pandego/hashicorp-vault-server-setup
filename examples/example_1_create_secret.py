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

# Create or update secret
create_response = client.secrets.kv.v2.create_or_update_secret(path='my-secret-login',
                                                               secret=dict(
                                                                   username='Angry_Hashi',
                                                                   password='Hashi123'),
                                                               )

print('Secrets written successfully!')
