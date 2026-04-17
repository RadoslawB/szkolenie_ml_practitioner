FROM python:3.10-slim


WORKDIR /app
RUN apt-get update

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Uruchom Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
