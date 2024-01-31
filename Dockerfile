FROM python:3.11

WORKDIR /flask-app-endpoint

COPY /flask-app-endpoint /flask-app-endpoint

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=/flask-app-endpoint/api/app.py
ENV BOOK_API_URL=http://sse-book-api-server.fpf7gvfpdfacbxby.uksouth.azurecontainer.io:5000

CMD ["flask", "run", "--host=0.0.0.0"]