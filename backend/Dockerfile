# This is a great way to do the dockerfile
# with anaconda. Credit goes to this duder
# https://beenje.github.io/blog/posts/docker-and-conda/

FROM continuumio/miniconda

# Install extra packages if required
RUN apt-get update && apt-get install -y \
    libjpeg62-turbo-dev \
    libav-tools \
    python-dev \
    python-setuptools \
    golang \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add the user that will run the app (no need to run as root)
RUN groupadd -r jamianv && useradd -r -g jamianv jamianv

WORKDIR /backend

# Install myapp requirements
COPY environment.yml /backend/environment.yml
RUN conda config --add channels conda-forge \
    && conda env create -n axonradio -f environment.yml \
    && rm -rf /opt/conda/pkgs/*

# Install myapp
COPY . /backend/
RUN chown -R jamianv:jamianv /backend/*

#this is important to change keras.json file to use
#theano rather than tensorflow
COPY keras.json /root/.keras/keras.json
COPY . /root

# activate the myapp environment
ENV PATH /opt/conda/envs/axonradio/bin:$PATH
