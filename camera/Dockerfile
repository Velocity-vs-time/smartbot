FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-opencv
WORKDIR /app
COPY camera.py .
CMD ["python3", "camera.py"]

