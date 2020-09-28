# Using ubuntu as the base image

FROM ubuntu:xenial
MAINTAINER Md Rezaur Rahman <reza.rahman@tum.de>


# updates and packages
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y sudo vim
RUN apt-get install -y build-essential

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Add user robotics with no password, add to sudo group
RUN adduser --disabled-password --gecos '' robotics
RUN adduser robotics sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER robotics
WORKDIR /home/robotics/
RUN chmod a+rwx /home/robotics/
RUN echo `pwd`

# Anaconda installing
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
RUN bash Anaconda3-2020.07-Linux-x86_64.sh -b
RUN rm Anaconda3-2020.07-Linux-x86_64.sh

# Set path to conda
ENV PATH /home/robotics/anaconda3/bin:$PATH

# Configuring access to Jupyter
RUN mkdir /home/robotics/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/robotics/.jupyter/jupyter_notebook_config.py

# Jupyter listens port: 8888
EXPOSE 8888

# Installing SPOT library
RUN wget http://www.lrde.epita.fr/dload/spot/spot-2.9.3.tar.gz
RUN tar -xf spot-2.9.3.tar.gz
RUN rm spot-2.9.3.tar.gz
RUN spot-2.9.3/configure --prefix ~/anaconda3/
RUN make
RUN make install

# Installing graph tools
RUN sudo apt-get install -y graphviz

# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/robotics/notebooks", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]


# Build and run the container in local machine
# docker run --publish 8000:8888 spot-docker-img:1.0
# see https://localhost/8000 and put the token as the password. Enjoy ... :)
