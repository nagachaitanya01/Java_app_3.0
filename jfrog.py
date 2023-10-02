import requests

artifactory_url = 'https://54.236.8.228:8082/artifactory'
repository = 'example-repo-local'
api_key = 'cmVmdGtuOjAxOjAwMDAwMDAwMDA6c3FZRzRBQ1FmeDhUaGEyRnFMNTk3TWhJVmo5'  # You can use an API key or basic authentication


local_file_path = '/home/ubuntu/git/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

# Construct the URL for uploading
upload_url = f'http://54.236.8.228:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

# Create headers with the API key or basic authentication
headers = {
    'X-JFrog-Art-Api': 'cmVmdGtuOjAxOjAwMDAwMDAwMDA6c3FZRzRBQ1FmeDhUaGEyRnFMNTk3TWhJVmo5',  # Replace with your API key
}

# Open the file and perform the upload
with open(local_file_path, 'rb') as file:
    response = requests.put(upload_url, headers=headers, data=file)

# Check the response status and print a message
if response.status_code == 201:
    print("jar success")
else:
    print(f'Failed to upload jar file. Status code: {response.status_code}')
    print(response.text)
