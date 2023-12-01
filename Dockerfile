FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Create a startup script
RUN echo "#!/bin/sh\npython manage.py makemigrations\npython manage.py migrate\npython manage.py runserver 0.0.0.0:8000" > /app/start.sh
RUN chmod +x /app/start.sh

# Use the startup script as CMD
CMD ["/app/start.sh"]
