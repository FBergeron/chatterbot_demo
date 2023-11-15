# README

## Try via Docker

Build the chatbot image:

```
docker build -t chatbot .
```


To start the chatbot:

```
docker run -v $PWD/data:/app/data -it chatbot
```

You can edit the data files and restart the chatbot again to test.


## Local Installation

### Requirements

- pyenv
- pip


### Installation

This uses a custom version of ChatterBot so you need to clone it at the top-level of the project directory:

```
git clone https://github.com/FBergeron/ChatterBot.git
git checkout english
```

Check current available Python versions:

```
pyenv versions
```

If Python 3.8.18 is not shown, install it:

```
pyenv install 3.8.18
```

Set the local Python version:

```
pyenv local 3.8.18
```

Install dependencies:

```
pip install spacy
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
pip install pyyaml
```

Install the custom version of ChatterBot:

```
pip install --ignore-requires-python ./ChatterBot
```

Launch the chatbot:

```
python test.py
```

## Using the chatbot

Once the chatbot is running, you can enter some requests and it will responds accordingly.
To end the conversation, just type: bye
