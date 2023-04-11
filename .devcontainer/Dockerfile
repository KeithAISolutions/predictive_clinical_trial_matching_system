FROM postgres:latest

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev curl gnupg2 lsb-release wget && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python 3.11
RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz && \
    tar -xf Python-3.11.0.tar.xz && \
    cd Python-3.11.0 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf Python-3.11.0 Python-3.11.0.tar.xz

# Install TypeScript
RUN npm install -g typescript

# Install Python packages
RUN python3.11 -m pip install --upgrade pip && \
    pip install pylint psycopg2-binary

# Setup user
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_UID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    apt-get update && \
    apt-get install -y sudo && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
