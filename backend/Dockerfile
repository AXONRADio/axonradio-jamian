FROM continuumio/anaconda

# Install extra packages if required
RUN apt-get update && apt-get install -y \
    libav-tools \
    python-dev \
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
RUN chown -R jamianv:jamianv /backend/main.py

# activate the myapp environment
ENV PATH /opt/conda/envs/axonradio/bin:$PATH
