from set_secrets import RASA_API_KEYS

def get_rasa_api_key():
    return RASA_API_KEYS.get("api_key")

# Example usage
if __name__ == "__main__":
    api_key = get_rasa_api_key()
    print(f"Rasa API Key: {api_key}")
