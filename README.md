# Containerized Web Scraping Service Exposed Via API

Source: https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp

<hr>

## TO INSTALL DEPENDENCIES FOR LOCAL "BARE-METAL" DEVELOPMENT
### (I'm using WSL)
    pip3 install -r requirements.txt

(You'll likely need to manually update the version of ```chromedriver-binary``` to latest)
<br>
(You may need to enable long paths if you're using WSL or Windows directly.)
<br>
(You'll probably need to install some other dependencies if using WSL [see the ```RUN``` entries in the ```Dockerfile```])

<hr>

## TO RUN LOCALLY:
- Satisfy pre-reqs for running locally (immediately above)
- To start the server, see the ```CMD``` entry in the ```Dockerfile```.

<hr>

## TO BUILD AND RUN ON DOCKER LOCALLY:
    cd {PATH}:\{TO}\{DIR_WITH_DOCKERFILE}
    docker build --tag scraper:1.0 .  
    docker run -e PORT=8080 --publish 8081:8080 --interactive --name scraper scraper:1.0 
    docker rm scraper

<hr>
<br> 

NOTE: The sections below assume you've installed and configured [gcloud](https://cloud.google.com/sdk/gcloud/).

<br>

## TO SUBMIT GCP BUILD:
    
    gcloud builds submit --tag gcr.io/YOUR_PROJECT/web-scraping-service    

<hr>

## TO DEPLOY SERVICE TO CLOUD RUN: 
    gcloud run deploy web-scraping-service --image gcr.io/YOUR_PROJECT/deploy web-scraping-service --region <REGION> --platform managed

<hr>
<br>

### NOTES FROM THE ORIGINAL AUTHOR
- We're using --no-sandbox to ensure compatibility with the Docker container, so only point such a service towards URLs you trust.
- Be careful when exposing such a service to user input: For example, if the URL we were screenshotting was supplied by the user, they could potentially take a screenshot of any file on the filesystem as well!
- Be sure to create a new service account with no permission and use it as the identity of the service, for better security. See https://cloud.google.com/run/docs/securing/service-identity for an example.
