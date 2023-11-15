FROM debian:11

WORKDIR /app

RUN apt update && apt dist-upgrade && \
    apt install -y pip vim git make build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev && \
    curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

ENV PYENV_ROOT=/root/.pyenv
ENV PATH="$PATH:$PYENV_ROOT/bin"

RUN pyenv install 3.8
RUN git clone https://github.com/FBergeron/ChatterBot.git && \
    cd ChatterBot && \
    git checkout japanese && \
    cd ..
RUN pyenv local 3.8.18 && \
    eval "$(pyenv init -)" && \
    pip install --upgrade pip && \
    pip install spacy && \
    python -m spacy download ja_core_news_lg && \
    pip install pyyaml && \
    pip install --ignore-requires-python ./ChatterBot

COPY test.py . 
COPY bin/run .

CMD ["./run"]
