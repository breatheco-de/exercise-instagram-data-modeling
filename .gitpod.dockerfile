FROM gitpod/workspace-full
# Install image generator
USER root

RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

RUN pyenv install 3.10 && pyenv global 3.10

ENV IP=0.0.0.0
ENV PORT=3000
