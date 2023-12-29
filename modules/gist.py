import requests


def update_gist(gist_id, token, content):
    """
    Update a GitHub Gist with new content.

    Args:
        gist_id (str): The ID of the Gist to update.
        token (str): The GitHub personal access token for authentication.
        content (str): The new content to update the Gist with.

    Returns:
        bool: True if the Gist was updated successfully, False otherwise.
    """
    url = f"https://api.github.com/gists/{gist_id}"

    payload = {
        "description": "An updated gist description",
        "files": {"my_calendar_events.ics": {"content": content}}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("PATCH", url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Gist updated successfully.")
        return True
    else:
        print("Failed to update Gist.")
        return False
