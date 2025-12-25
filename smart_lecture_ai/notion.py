import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def upload_to_notion(title, content):
    url = "https://api.notion.com/v1/pages"

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"text": {"content": content}}]
            }
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.status_code
