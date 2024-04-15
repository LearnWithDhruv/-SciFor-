import requests

base_url = 'https://jsonplaceholder.typicode.com'

def update_resource_with_put(resource_id, new_data):
    url = f'{base_url}/posts/{resource_id}'
    response = requests.put(url, json=new_data)
    return response.json()

def update_resource_with_patch(resource_id, updated_fields):
    url = f'{base_url}/posts/{resource_id}'
    response = requests.patch(url, json=updated_fields)
    return response.json()


if __name__ == "__main__":
    resource_id = 1

    new_data = {
        "userId": 1, 
        "title": "Updated Title",
        "body": "Updated Body"
    }

    updated_fields = {
        "title": "Updated Title"
    }
    put_response = update_resource_with_put(resource_id, new_data)
    print("PUT Response: ", put_response)
    patch_response = update_resource_with_patch(resource_id, updated_fields)
    print("PATCH Response: ", patch_response)

