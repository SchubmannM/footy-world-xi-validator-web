# Pull base image
FROM python:3.8.2
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory
ENV APP_HOME=/code/
WORKDIR $APP_HOME
RUN mkdir $APP_HOME/staticfiles

# Install dependencies
COPY Pipfile Pipfile.lock $APP_HOME
RUN pip install pipenv && pipenv install --system --dev

# Copy project
COPY . $APP_HOME
