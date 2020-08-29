# Web Scraping Service Exposed Via API

Source: https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp



TO BUILD AND RUN ON DOCKER LOCALLY:
    cd {PATH}:\{TO}\{DIR_WITH_DOCKERFILE}
    docker build --tag scraper:1.0 .  
    docker rm scraper && docker run -e PORT=8080 --publish 8081:8080 --interactive --name scraper scraper:1.0 

TO SUBMIT GCP BUILD:
    gcloud builds submit --tag gcr.io/YOUR_PROJECT/web-scraping-service


TO DEPLOY SERVICE: 
    gcloud run deploy web-scraping-service --image gcr.io/YOUR_PROJECT/deploy web-scraping-service --region <> --platform managed