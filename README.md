# Rate Limit Tester with Proxy

## Overview
This application tests the rate limit of a specified URL using different SOCKS5 proxies (For testing we're using NordVPN proxies). It simulates requests from various geographic locations to understand the target application's behavior under different IP addresses.

## Prerequisites
- Docker
- Docker Compose

## Configuration

### Proxy Credentials
Create a `.env` file at the root of the project with your proxy credentials:

```env
PROXY_USER=YourProxyUsername
PROXY_PASS=YourProxyPassword
````

### Target URL and Rate Limit Parameters
In the same .env file, specify the URL to be tested, the rate limit, and the interval between requests:

```env
TESTED_URL=https://example.com
RATE_LIMIT=100
INTERVAL=1
```

## Running the Application
To start the application, execute the following command in the terminal:

```bash
docker-compose up --build
```

This command builds the Docker images and starts multiple container instances, each using a different proxy server, as defined in the docker-compose.yml file.

### How It Works
Each Docker container is set up with a unique SOCKS5 proxy server. The application inside each container sends HTTP requests to the TESTED_URL at a frequency determined by RATE_LIMIT and INTERVAL. This setup is useful for testing the response of a URL to requests from different locations and under varying load conditions.

### Services
The application runs several services, each corresponding to a different proxy server location. These are defined in the docker-compose.yml file and include:

Amsterdam
Atlanta
Dallas
Los Angeles
Netherlands
Sweden
Stockholm
United States
New York

### Troubleshooting

If you encounter any issues, ensure that:

The .env file is correctly configured with your proxy credentials and target URL.
Docker and Docker Compose are installed and working correctly.
Your internet connection is active, and the proxy servers are accessible.
