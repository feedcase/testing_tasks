FROM python:3.9
MAINTAINER vsevolod.fedoseev@icloud.com
COPY . /testing_tasks
WORKDIR /testing_tasks
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4444
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null