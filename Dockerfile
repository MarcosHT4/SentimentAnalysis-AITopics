FROM python:3.11
ENV PORT 8000

COPY requirements.txt /
RUN apt-get update && apt-get install git-all git-lfs -y
RUN git-lfs install



COPY ./src /src
RUN curl -O -L https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.7.0/es_core_news_md-3.7.0.tar.gz
RUN tar -xvzf es_core_news_md-3.7.0.tar.gz
RUN cp -r es_core_news_md-3.7.0/es_core_news_md/es_core_news_md-3.7.0 /src/models
RUN rm -rf es_core_news_md-3.7.0.tar.gz es_core_news_md-3.7.0
RUN cd /src/models && git clone https://huggingface.co/karina-aquino/spanish-sentiment-model
RUN pip3 install torch==2.1.1+cpu torchvision==0.16.1+cpu torchaudio==2.1.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt

CMD uvicorn src.app:app --host 0.0.0.0 --port ${PORT}

