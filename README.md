# Flask To-Do App ⚡

This is a simple application To-Do development in Flask
with Docker compose

## 📑 Getting Started

### Prerequisites

- Docker
- Editor code

### Installing
1. Clone the repository
2. In root directory run the command
    ```sh
    docker-compose up -d
    ```
3. Run the following command to recreate the database schema
    ```sh
    docker exec -it web flask init-db
    ```
4. Check if containers are running
    ```sh
   docker ps
   ```
5. Open the browser in the port [localhost:5000](http://localhost:5000/)


## 🚀 Deployment
You can deploy this project on Heroku

## ⚙ Built with

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework
* [Docker](https://docs.docker.com/) -  App Containerization
* [MySQL](https://dev.mysql.com/doc/) - Database engine
* [Bootstrap 4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - CSS Framework

## 👦 Author

* **Anderson Pozo**
