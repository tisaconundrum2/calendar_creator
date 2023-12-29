import requests


def update_gist(gist_id, token, description=None, files=None):
    """
    Update a Gist on GitHub.

    Args:
        gist_id (str): The ID of the Gist to update.
        token (str): Your GitHub Personal Access Token for authentication.
        description (str, optional): New description for the Gist (default is None).
        files (dict, optional): Dictionary of files to update with their content (default is None).

    Returns:
        bool: True if the Gist was successfully updated, False otherwise.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Authorization": f"token {token}"
    }

    payload = {}

    if description:
        payload["description"] = description

    if files:
        payload["files"] = files

    response = requests.patch(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Gist updated successfully.")
        return True
    else:
        print("Failed to update Gist.")
        return False


# Example usage:
gist_id = "your_gist_id"
token = "your_personal_access_token"

# Update description and files
description = "New Description"
files = {
    "filename.txt": {
        "content": "Updated content"
    }
}

update_gist(gist_id, token, description, files)
