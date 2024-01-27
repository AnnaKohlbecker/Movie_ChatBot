# Weather_ChatBot
# Chatbot that can give you information about the weather
A ... interface for a chatbot deployed on [OpenAI](https://platform.openai.com/api-keys).
The chatbot uses a [langchain](https://python.langchain.com/en/latest/index.html) agent to access some tools.
## Setup and Installation
### Setup developmnet environment (Ubuntu-22.04)
I used this [Tutorial](https://www.youtube.com/watch?v=R88B_ldc6O8&t=384s).
Open Ubuntu-22.04 via Remote Explorer for VS Code.
### Install repository
```
git clone https://github.com/AnnaKohlbecker/Weather_ChatBot.git
```
Open Weather_Chatbot in new window.
### Additional Installations
Download the [Anaconda Distribution](https://docs.anaconda.com/free/anaconda/install/linux/) (I used "Anaconda3-2023.09-0-Linux-x86_64.sh") and make sure that conda is recognized.
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash ~/Weather_ChatBot/Anaconda3-2023.09-0-Linux-x86_64.sh
conda init
# Install module system for environment module management
install lmod
```
### Create environment
```
# Load modules
ml purge
ml Anaconda3
# Create new conda environment
conda create -n chatbot_env python=3.9.13 --yes
# Activate conda environment
conda activate chatbot_env
```
### Environment installations
make sure that you use the correct python version of the environment (F1)
```
pip install -r requirements.txt
```
### Change environment setup
```
cp .env-example .env
```
Change `OPENAI_API_BASE` and `OPENAI_API_KEY` variables to the base and key given the Azure OpenAI resource.
See https://portal.azure.com/

Add SciFinder Integration API credentials. 
### Run the streamlit server locally
```
streamlit run tools_app.py
```
### Deployment on RStudio Connect
The **pRED** R Studio Connect specific deployment  
1. Request an API Key that allows you to interact with R Studio connect server as described [here](https://rsconnect-pred.roche.com/__docs__/user/api-keys/)
2. Add the R Studio Connect API key
    ```
    # Production server
    rsconnect add --server https://rsconnect-pred.roche.com --name pred-prod --api-key <YOUR_PROD_API_KEY> 
    # Test server
    rsconnect add --server https://rsconnect-pred-test.roche.com --name pred-test --api-key <YOUR_TEST_API_KEY> 
    ```
    The keys are stored in `.rsconnect-python/servers.json`
3. Deploy the streamlit app.
    ```
    rsconnect deploy streamlit -n pred-test --entrypoint tools_app.py .
    ```
    The dot at the end of the command represents the current directory.
4. Click the **Dashboard content URL** and set the environment variables from the `.env` file in the Envs section of the dashboard.
   Or set the environment variables during deployment:
    ```bash
    # Export variables in .env file as environment variables
    export $(grep -v "^#" .env | xargs -d '\n')
    # Deploy the app
    rsconnect deploy streamlit -n pred-test \
     --environment OPENAI_API_TYPE \
     --environment OPENAI_API_VERSION \
     --environment OPENAI_API_BASE \
     --environment OPENAI_API_KEY \
     --environment SCIFINDER_SERVER \
     --environment SCIFINDER_TOKEN_URL \
     --environment SCIFINDER_GRANT_TYPE \
     --environment SCIFINDER_CLIENT_ID \
     --environment SCIFINDER_CLIENT_SECRET \
     --environment SCIFINDER_SCOPE \
     --environment SCIFINDER_CACHE_FILE \
     --entrypoint tools_app.py .
    ```