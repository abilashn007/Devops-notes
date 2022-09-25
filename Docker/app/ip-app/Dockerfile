FROM python
WORKDIR /app
COPY ip_app.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","ip_app.py"]