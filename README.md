# Containerized Web Scraping Service Exposed Via API

Source: https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp

<hr>
<br>

## To install dependencies for local "bare-metal" development (I'm using WSL)
    pip3 install -r requirements.txt

(You'll likely need to update the version of ```chromedriver-binary``` to latest)
(You may need to enable long paths if you're using WSL or Windows directly.)
(You'll probably need to install some other dependencies if using WSL [see the ```RUN``` entries in the ```Dockerfile```])

## To run locally:
- Satisfy pre-reqs for running locally (immediately above)
- To start the server, see the ```CMD``` entry in the ```Dockerfile```.


## TO BUILD AND RUN ON DOCKER LOCALLY:
    cd {PATH}:\{TO}\{DIR_WITH_DOCKERFILE}
    docker build --tag scraper:1.0 .  
    docker rm scraper && docker run -e PORT=8080 --publish 8081:8080 --interactive --name scraper scraper:1.0 


## TO SUBMIT GCP BUILD:
    gcloud builds submit --tag gcr.io/YOUR_PROJECT/web-scraping-service


## TO DEPLOY SERVICE: 
    gcloud run deploy web-scraping-service --image gcr.io/YOUR_PROJECT/deploy web-scraping-service --region <> --platform managed