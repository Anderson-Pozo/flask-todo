# Flask To-Do App ⚡

This is a simple application To-Do development in Flask
with Docker compose

## 📑 Getting Started

### Prerequisites

- Docker
- Editor code

### Installing
1. Clone the repository
2. In root directory run the next command for up container
    ```sh
    docker-compose up -d
    ```
3. Aply migrations to recreate schema database
    ```sh
    docker exec -it web flask init-db
    ```
4. Verify if containers are running
    ```sh
   docker ps
   ```
5. Open navigator in port [localhost:5000](http://localhost:5000/)


## 🚀 Deployment
You can deploy this project in Heroku in few steps with 
the next tutorial

## ⚙ Built with

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework
* [Docker](https://docs.docker.com/) -  App Containerization
* [MySQL](https://dev.mysql.com/doc/) - Database engine
* [Bootstrap 4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - CSS Framework

## 👦 Author

* **Anderson Pozo**
