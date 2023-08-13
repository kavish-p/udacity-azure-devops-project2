# Udacity - Building a CI/CD Pipeline

![Build](https://github.com/kavish-p/udacity-azure-devops-project2/actions/workflows/main.yml/badge.svg)

# Project Plan

Trello Board - https://trello.com/b/xp0TWgAK/udacity-devops

Project Management Spreadsheet - https://docs.google.com/spreadsheets/d/1bqPJ-2aDkCJGl4yBkFtZAZzYJxTQQ9VXvcFPRmM7nu0/edit?usp=sharing

# Architecture

![alt text](screenshots/00-architecture.png)

# Instructions

## Azure Cloud Shell / GitHub Actions

- Create a fork of this repository to be used for the rest of the instructions.
- Enable GitHub Actions for the forked repository.
  ![alt text](screenshots/misc/01-enable-actions.png)
- Login to the Azure Portal and open an Azure Shell session.
- Generate an SSH key and add it to your GitHub account.

```
ssh-keygen
```

- Clone the Git repository.
  ![alt text](screenshots/03-azure-shell.png)
- `cd` into the cloned repository and run `make all`.
  ![alt text](screenshots/misc/02-make-all.png)
- After enable Github Actions, the workflow execution would be as shown here, similar to the Cloud Shell output.
  ![alt text](screenshots/02-github-actions-output.png)
- Create the App Service by running the following command in Azure Cloud Shell. You may need to change some parameters such as name, resource group, or add parameters such as location (region), sku, and so on.

```
az webapp up --name k123webapp --resource-group hackaton --runtime "PYTHON:3.8"
```

![alt text](screenshots/04-deployed-app-service.png)

- Edit the endpoint in the `make_predict_azure_app.sh` script and run the script to test the deployed app.
  ![alt text](screenshots/06-run-predict.png)
  ![alt text](screenshots/05-verify-app-service.png)

## Azure DevOps

- Login to Azure DevOps and create a project if none exist.
- Under project settings, create a new Azure Resource Manager service connection.
- Create a new pipeline and select GitHub as the source. After authenticating, select your repository and choose Existing YAML file.
  ![alt text](screenshots/misc/03-pipeline-new.png)
- You would need to make changes to the pipeline YAML file and set your App Service name and Azure Subscription.

# Enhancements

<TODO: A short description of how to improve the project in the future>

# Demo

<TODO: Add link Screencast on YouTube>
