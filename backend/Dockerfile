FROM python:3.10-alpine

COPY . .
RUN python3 -m venv venv   
RUN source venv/bin/activate    
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]