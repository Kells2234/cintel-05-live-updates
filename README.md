# Continuous Intelligence App

- Repository: [cintel-05-live-updates](https://github.com/Kells2234/cintel-05-live-updates)
- Website: [cintel-05-live-updates](https://s557075ks.shinyapps.io/cintel-05-live-updates/)
- Author: [Kelly Simmons](https://github.com/Kells2234)

-----

## Forex Trading Data

### Purpose

To create a Shinyapp.io that will continuously update the data concerning the seven most populare Forex currency pairs and provide visuals that will hopefully show trends in the data.

### STEP 1

Find current Forex data that is in csv form.
Data was found using Kaggle. URL is https://www.kaggle.com/datasets/diqiland/major-forex.

### STEP 2

Combine all seven CSV file in to one organized CSV file.

The CSV file contains seven of the most populare currency pairs. 
Create a code that will concatenate all the files into one file and save it to the folder. 
The first 10 lines were printed in the output as a QA.

### Update nesseccary files that will create the create app .

1. After making changes, you want to send them back to GitHub.
1. In VS Code, find the "Source Control" icon and click it.
1. Important: Enter a brief commit message describing your changes.
1. Change the "Commit" button dropdown to "Commit and Push" to send your changes back to GitHub.

-----

## Create a Local Virtual Environment

Open a PowerShell terminal in this cintel-05-live-updates folder on your machine. 
Create a virtual environment named .venv in the current directory. 
Verify that a .venv folder was created after running the command. 

```shell
python -m venv .venv
```

If VS Code asks to use it as the workspace folder, select Yes.

## Activate the Environment

Run the following command to activate the virtual environment we just created.
Verify that the PowerShell prompt now shows (.venv) at the beginning of the line.

```shell
.venv\Scripts\activate
```

## Prepare the Environment

Run the following commands to upgrade pip and install required packages.
Rerun as needed until everything is successfully installed.

```shell
python -m pip install --upgrade pip wheel pyodide-py
python -m pip install --upgrade -r requirements.txt
```

Read the requirements.txt file to see the packages we are installing.

Additional information can be found in our first Shiny repo: 
[cintel-02-app/SHINY.md](https://github.com/denisecase/cintel-02-app/blob/main/SHINY.md#step-2-prepare-virtual-environment)

-----

## Run the App

Verify your virtual environment is activated and packages have been installed. 
Run the following PowerShell command to start the app.

```shell
shiny run app.py
```

You may use `shiny run app.py --reload` but it can be harder to stop the app during development.
Open the app by following the instructions provided in the terminal. 
For example, try CTRL CLICK (at the same time) on the URL displayed (http://127.0.0.1:8000).

Hit CTRL c (at the same time) to quit the app. 
If it won't stop, close the terminal window.
Reopen the terminal window and be sure the virtual environment is activated
before running the app again.

## Deploy the App

Add and customize .github/workflows/deploy.yml.
Login to [shinyapps.io](https://www.shinyapps.io/) then Account / Tokens and add 3 repo secrets.
See the earlier [SHINYAPPS.md](https://github.com/denisecase/cintel-02-app/blob/main/SHINYAPPS.md) for details.

- Name: SHINYAPPS_ACCOUNT, Secret: Paste shinyapps.io account name
- Name: SHINYAPPS_TOKEN, Secret: (paste token )
- Name: SHINYAPPS_SECRET, Secret: (paste secret)

-----

## ⚠️ Delete Hosted App Before Pushing to GitHub

Reminder: The GitHub action deploy.yml may not automatically delete an existing app from shinyapps.io so we can redeploy.

Before pushing to GitHub, login to [shinyapps.io](https://www.shinyapps.io/) and view the list of applications. 

- First archive the app.
- Then delete the archived app.