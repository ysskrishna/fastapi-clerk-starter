# FastAPI-Clerk-Starter

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.41-blue.svg)](https://www.sqlalchemy.org/)
[![Clerk](https://img.shields.io/badge/Clerk-Auth-orange.svg)](https://clerk.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A starter template for building secure and scalable FastAPI applications with Clerk authentication integration. 

## Use Cases

This starter template is perfect for:
- Building secure backend APIs
- Creating user authentication systems
- Developing full-stack applications
- Learning FastAPI and Clerk integration
- Prototyping new projects quickly

## Features

- FastAPI backend with SQLAlchemy ORM
- Secure Clerk JWT authentication integration
  - Automatic token validation and parsing
  - Protected route handling
- User management endpoints
- CORS middleware enabled
- SQLite database (can be easily switched to other databases)
- Swagger UI for API documentation

## Prerequisites

- Python 3.12+
- uv (Python package installer)
- Clerk account and project

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-clerk-starter
```

2. Install dependencies using uv:
```bash
uv venv
.venv\Scripts\activate
uv sync
```
(Optional) To add new packages to your project:
```bash
uv add <package-name>
```


3. Set up environment variables:
Create a `.env` file in the project root using `.env.sample` as reference, and update the .env based on your configuration.
```
DATABASE_URL=sqlite:///<database_name>.db
CLERK_JWKS_URL=https://<clerk-project-id>.clerk.accounts.dev/.well-known/jwks.json
CLERK_ISSUER=https://<clerk-project-id>.clerk.accounts.dev
```

## Clerk Setup

1. Create a Clerk project at https://clerk.com
2. Get your project credentials:
   - CLERK_JWKS_URL: Found in `Clerk Dashboard > API Keys > JWKS URL`
   - CLERK_ISSUER: Found in `Clerk Dashboard > API Keys > Frontend API URL`
3. Add these credentials to your `.env` file


## JWT Authentication

This project uses Clerk's JWT authentication with the following features:

- Automatic JWT validation and parsing
- User session management
- Protected route handling

### Using JWT in API Requests

Include the JWT token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

## Project Structure

```
fastapi-clerk-starter/
├── core/               # Core utilities and configurations
│   ├── config.py      # Environment configuration
│   ├── dbutils.py     # Database utilities
│   └── jwtutils.py    # JWT authentication utilities
├── models/            # SQLAlchemy models
├── routers/           # API route handlers
├── main.py           # Application entry point
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## API Endpoints

### User Management

- `POST /user/create` - Create user in database, using clerk jwt payload (requires Clerk JWT)
- `GET /user/me` - Retrieves user details from database (requires Clerk JWT)

## Running the Application

Start the development server:

```bash
python main.py
```

The server will start at `http://localhost:8001`

## API Documentation

Swagger UI documentation is available at: `http://localhost:8001/docs`

## Security Best Practices

- Never expose your Clerk Secret Key in client-side code
- Keep your Clerk Secret Key secure and rotate it periodically
- Use HTTPS for all API requests
- Set appropriate token expiration times
- Validate all claims in the JWT payload

## References
- [Clerk Authentication Overview](https://clerk.com/docs)
- [JWT.io](https://jwt.io/) - Learn about JSON Web Tokens
- [JWT Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)
- [uv Installation](https://docs.astral.sh/uv/getting-started/installation/)
- [uv Managing Dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) - Learn about managing dependencies with uv

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.