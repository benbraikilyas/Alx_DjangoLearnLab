#  Advanced API Project - Django REST Framework

##  Overview
This project is an API for managing books and authors, built using Django REST Framework. It supports CRUD operations with authentication-based restrictions.

## Endpoints
### Books API
| Method | Endpoint | Description | Auth Required |
|--------|---------|-------------|--------------|
| GET | `/api/books/` | Get all books |  No |
| GET | `/api/books/<id>/` | Get book details |  No |
| POST | `/api/books/create/` | Create a new book |  Yes |
| PUT | `/api/books/<id>/update/` | Update a book |  Yes |
| DELETE | `/api/books/<id>/delete/` | Delete a book |  Yes |

## 🛠 Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/benbraikilyas/Alx_DjangoLearnLab.git
