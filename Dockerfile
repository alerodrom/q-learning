# Use python 3.7
FROM python:3.7

# Set enviroment variable
ENV PYTHONUNBUFFERED 1

# Create folder code
RUN mkdir /code

# Copy file docker-entrypoint.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Change permissions to docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Use /code as default workspace
WORKDIR /code

# Add requirements to code folder
ADD requirements.txt /code/

# Install requirements for python enviroment
RUN pip install -r requirements.txt

# Add current directory files to code folder
ADD . /code/

# Exec entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]