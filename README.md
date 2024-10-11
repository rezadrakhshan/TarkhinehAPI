# Tarkhineh API

Welcome to the Tarkhineh API! This API provides functionalities to manage food items, user profiles, addresses, and branches.

## Base URL

```
https://tarkhineh.liara.run/
```

## API Endpoints

### Food Management

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| POST   | /food/create/    | Create a new food item |
| DELETE | /food/remove/    | Remove a food item     |
| GET    | /food/           | Retrieve all food items |

### Profile Management

| Method | Endpoint                                | Description                       |
|--------|-----------------------------------------|-----------------------------------|
| POST   | /authentication/profile/create/         | Create a new user profile         |
| DELETE | /authentication/profile/delete/         | Remove a user profile             |
| PUT    | /authentication/profile/update/         | Update a user profile             |
| GET    | /authentication/profile/                | Retrieve all user profiles        |

### Address Management

| Method | Endpoint                                | Description                       |
|--------|-----------------------------------------|-----------------------------------|
| POST   | /authentication/address/create/         | Create a new address              |
| DELETE | /authentication/address/delete/         | Remove an address                 |
| PUT    | /authentication/address/update/         | Update an address                 |
| GET    | /authentication/address/                | Retrieve all addresses            |

### Branch Management

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| POST   | /branch/create/  | Create a new branch   |
| DELETE | /branch/remove/  | Remove a branch       |
| PUT    | /branch/update/  | Update a branch       |
| GET    | /branch/         | Retrieve all branches |

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For further questions, reach out via [GitHub](https://github.com/rezadrakhshan).

---

Enjoy using the Tarkhineh API!
