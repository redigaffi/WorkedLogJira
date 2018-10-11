FROM python:2.7-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "/usr/local/bin/python2.7", "/usr/src/app/work.py"]