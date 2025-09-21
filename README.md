# Cryptocurrency Price Tracker

This project is a Dockerized application that retrieves current cryptocurrency prices from the CoinGecko API and saves the data to a JSON file. The application runs in an infinite loop, updating the prices every 5 minutes.

## Project Structure

```
crypto-docker-stack
├── src
│   └── crypto_precos.py       # Python script for fetching cryptocurrency prices
├── docker-compose.yml          # Docker stack configuration
├── Dockerfile                  # Instructions to build the Docker image
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository:**
   Clone this repository to your local machine.

   ```bash
   git clone <repository-url>
   cd crypto-docker-stack
   ```

2. **NFS Setup:**
   Ensure that you have an NFS server running and accessible at `192.168.1.197:/export/Dados/NAS`. This directory will be used to store the output JSON file.

3. **Docker Installation:**
   Make sure you have Docker and Docker Compose installed on your machine.

4. **Build the Docker Image:**
   Navigate to the project directory and build the Docker image using the following command:

   ```bash
   docker-compose build
   ```

5. **Run the Docker Stack:**
   Start the application using Docker Compose:

   ```bash
   docker-compose up
   ```

## Usage

Once the application is running, it will fetch the current prices of the specified cryptocurrencies every 5 minutes and save the data to a file named `precos_cripto.json` in the NFS mounted directory.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License.