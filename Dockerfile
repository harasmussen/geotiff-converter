FROM python:3

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y libgdal-dev
RUN pip install numpy==1.14.5
RUN pip install GDAL==2.1.3 --global-option=build_ext --global-option="-I/usr/include/gdal/"
RUN pip install georasters==0.5.12

COPY convert.py convert.py

CMD [ "python", "./convert.py" ]
