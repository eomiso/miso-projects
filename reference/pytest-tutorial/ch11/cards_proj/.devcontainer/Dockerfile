ARG VARIANT=20.04
FROM ubuntu:${VARIANT}

RUN apt-get update \
    && apt-get install -y sudo curl \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && curl -S "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xF23C5A6CF475977595C89F51BA6932366A755776" \
        | sudo gpg --batch --yes --dearmor --output "/etc/apt/trusted.gpg.d/deadsnakes_ubuntu_python.gpg"

RUN apt-get install -y python3 python3-pip python3-venv python3.7-distutils

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends python3.7 python3.8 python3.9 python3.10 \
    && apt-get purge -y imagemagick imagemagick-6-common

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python -m pip install --upgrade setuptools
