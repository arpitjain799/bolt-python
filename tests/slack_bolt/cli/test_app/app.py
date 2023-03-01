import os

from slack_sdk import WebClient
from slack_bolt.app import App

assert "SLACK_BOT_TOKEN" in os.environ
assert "SLACK_APP_TOKEN" in os.environ

mock_api_server_base_url = "http://localhost:8888"
web_client = WebClient(
    token=os.environ["SLACK_BOT_TOKEN"],
    base_url=mock_api_server_base_url,
)

app = App(signing_secret="secret", client=web_client)

# Start Bolt app
if __name__ == "__main__":
    print(f"{os.path.basename(__file__)} ran")
