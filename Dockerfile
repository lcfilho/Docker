FROM centos:7

RUN yum update -y && \
    yum install wget -y && \
    yum install sudo -y && \
    yum install epel-release -y && \
    yum install nano -y 

RUN yum groupinstall "Development Tools" -y && \
    yum install python36 -y && \
    yum install epel-release -y && \
    yum install python36-setuptools -y && \
    easy_install-3.6 pip

EXPOSE 8888

COPY create_db.py /

COPY app.py /



