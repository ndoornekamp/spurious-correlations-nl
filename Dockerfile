FROM python:3.8-slim-buster

ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

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

CMD ["flask", "run", "--host=0.0.0.0"]