FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-rpi.gpio
WORKDIR /app
COPY motor_control.py .
CMD ["python3", "motor_control.py"]

