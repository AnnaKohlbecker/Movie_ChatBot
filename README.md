# Weather_ChatBot
# Chatbot that can give you information about the weather
A ... interface for a chatbot deployed on [OpenAI](https://platform.openai.com/api-keys).
The chatbot uses a [langchain](https://python.langchain.com/en/latest/index.html) agent to access some tools.
## Setup and Installation
### Setup developmnet environment (Ubuntu-22.04)
I used this [Tutorial](https://www.youtube.com/watch?v=R88B_ldc6O8&t=384s).
Open Ubuntu-22.04 via Remote Explorer for VS Code.
Install Python & Pylance extension in WSL.
### Install repository
```
git clone https://github.com/AnnaKohlbecker/Weather_ChatBot.git
cd ~/Weather_ChatBot
```
### Install Anaconda
Download the [Anaconda Distribution](https://docs.anaconda.com/free/anaconda/install/linux/). I used the installer version "Anaconda3-2023.09-0-Linux-x86_64.sh".
```
curl -O https://repo.anaconda.com/archive/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
bash ~/Downloads/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
source <PATH_TO_CONDA>/bin/activate
conda init
```
### Create environment
```
# Create new conda environment
conda create -n chatbot_env python=3.11.5 --yes
# To activate this environment, use
conda activate chatbot_env
# To deactivate an active environment, use
conda deactivate
```
### Environment installations
After activating the environment, make sure that you are using the right python interpreter. Should be: ~/anaconda3/envs/chatbot_env/bin/python. (F1 -> Python: Select Interpreter)
```
pip install -r requirements.txt
```
### Change environment setup
```
cp .env-example .env
```
Change `OPENAI_API_KEY` variable to the key given the by the OpenAI resource.
See [OpenAI](https://platform.openai.com/api-keys).
### Run
```
```