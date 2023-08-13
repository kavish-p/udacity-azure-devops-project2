# Azure Web App
az webapp up --name k123webapp --resource-group hackaton --runtime "PYTHON:3.8"

# Locust Test
locust --headless --users 5 --run-time 5s -H https://k123webapp.azurewebsites.net/