FROM python:3.11.5-slim

WORKDIR /app_python
COPY requirements/requirements-prod.txt requirements-prod.txt

RUN apt-get update && apt-get install -y \
    curl
RUN pip install -r requirements-prod.txt

COPY ./src ./src

RUN addgroup --system user && adduser --system --group user
USER user

EXPOSE 8080
ENTRYPOINT [ "python3", "src/app.py" ]
