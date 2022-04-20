#FROM python:3.8.12-slim-bullseye
FROM python:3.8.13-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"
ENV PORT=8000
COPY ./requirements.txt /requirements.txt
COPY ./airconditioner /airconditioner
RUN pip install --no-cache-dir -r /requirements.txt
RUN groupadd -rf -g 1000 django && \
    useradd -r -M -g 1000 -u 1000 django && \
    chown -R django:django /airconditioner
USER django
WORKDIR /airconditioner
EXPOSE ${PORT}
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["entrypoint.sh"]
