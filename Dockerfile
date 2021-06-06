FROM python:3.8-slim-buster

ENV FLASK_APP "run.py"

WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

# Create and switch to a new user - running as root user can be a security risk
RUN useradd appuser
USER appuser

ADD . /app

EXPOSE 5000

# Run the app using Flask's development server. That's not recommended (see e.g.
# https://flask.palletsprojects.com/en/latest/deploying/, but will be fine for this simple, low-traffic project
ENTRYPOINT ["python", "run.py"]
