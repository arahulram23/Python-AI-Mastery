# 30-Day Python + FastAPI Mastery Roadmap

**Format:** Each day = ~2-4 hrs. Build one running repo: `python-fastapi-mastery`.
Commit daily, even small progress. Push at end of each day — no exceptions, this is what builds the habit and the portfolio.

Setup once:
```bash
mkdir python-fastapi-mastery && cd python-fastapi-mastery
git init
python -m venv venv && source venv/bin/activate
echo "venv/\n__pycache__/\n.env\n*.db" > .gitignore
git add .gitignore && git commit -m "chore: initial repo setup"
git remote add origin <your-repo-url>
git push -u origin main
```

---

## PHASE 1: Python Core (Days 1–7)

### Day 1 — Syntax, Variables, Data Types
- Variables, dynamic typing, numbers, strings, booleans, `None`
- String methods, f-strings, slicing
- Type casting, operators (arithmetic, comparison, logical, walrus `:=`)
- **Task:** Write `day01_basics.py` — string manipulation exercises (reverse a string, palindrome check, word frequency counter) with no libraries.
- **Push:** `feat(day01): python basics - strings, types, operators`

### Day 2 — Control Flow & Functions
- `if/elif/else`, `for`, `while`, `break/continue/else` on loops
- Function definitions, default/keyword/positional args, `*args`/`**kwargs`
- Scope (LEGB rule), recursion
- **Task:** `day02_functions.py` — FizzBuzz variants, recursive factorial/Fibonacci, a function using `*args`/`**kwargs` for a flexible calculator.
- **Push:** `feat(day02): control flow and functions`

### Day 3 — Core Data Structures
- Lists, tuples, sets, dicts — methods, mutability differences
- List/dict/set comprehensions, nested comprehensions
- `zip`, `enumerate`, `sorted` with custom keys, unpacking
- **Task:** `day03_data_structures.py` — solve 5 small problems (dedupe list, group anagrams, merge dicts, flatten nested list, top-N frequency) using comprehensions where possible.
- **Push:** `feat(day03): data structures and comprehensions`

### Day 4 — OOP Fundamentals
- Classes, `__init__`, instance vs class attributes/methods
- Inheritance, `super()`, method overriding
- Encapsulation conventions (`_protected`, `__private`), properties (`@property`)
- **Task:** Build a small `library_system` module — `Book`, `Member`, `Library` classes with borrow/return logic.
- **Push:** `feat(day04): OOP basics - classes and inheritance`

### Day 5 — Advanced OOP
- Polymorphism, abstract base classes (`abc` module)
- Dunder methods: `__str__`, `__repr__`, `__eq__`, `__len__`, `__iter__`
- Composition vs inheritance, multiple inheritance & MRO
- **Task:** Extend `library_system` — add an abstract `Media` base class, subclasses `Book`/`DVD`, implement custom `__repr__`/`__eq__`.
- **Push:** `feat(day05): advanced OOP - abc, dunder methods, polymorphism`

### Day 6 — Error Handling, Files, Context Managers
- `try/except/else/finally`, custom exceptions, exception chaining
- File I/O (`with open`), `pathlib`, JSON/CSV reading/writing
- Writing your own context manager (class-based and `contextlib.contextmanager`)
- **Task:** Build a `FileLogger` context manager that writes timestamped logs; add custom `InsufficientStockError` to a small inventory script that reads/writes JSON.
- **Push:** `feat(day06): exception handling, file IO, context managers`

### Day 7 — Modules, Packages, Environments
- Module/package structure, `__init__.py`, relative imports
- Virtual environments, `pip`, `requirements.txt` vs `pyproject.toml`
- Intro to `poetry` or `uv` (pick one)
- **Task:** Refactor everything so far into a proper package structure (`src/` layout) with a `pyproject.toml`. Add a `README.md`.
- **Push:** `refactor(day07): restructure into proper package with pyproject.toml`

---

## PHASE 2: Advanced Python (Days 8–13)

### Day 8 — Iterators & Generators
- Iterator protocol (`__iter__`/`__next__`), `iter()`, `next()`
- Generator functions (`yield`), generator expressions
- Memory efficiency: generators vs lists for large data
- **Task:** Build a custom iterator class for a `Range` clone; write a generator that lazily reads a large CSV line by line and yields parsed rows.
- **Push:** `feat(day08): iterators and generators`

### Day 9 — Decorators & Functional Programming
- Function as first-class objects, closures
- Writing decorators (with and without arguments), `functools.wraps`
- `map`, `filter`, `reduce`, `lambda`, `functools.lru_cache`, `partial`
- **Task:** Write `@timer`, `@retry(times=3)`, and `@cache_result` decorators from scratch and apply them to real functions.
- **Push:** `feat(day09): decorators and functional programming`

### Day 10 — Concurrency Fundamentals
- Threading vs multiprocessing vs asyncio — GIL explained
- `threading.Thread`, `concurrent.futures`, `multiprocessing.Pool`
- `asyncio` basics: `async def`, `await`, event loop, `asyncio.gather`
- **Task:** Write a script that fetches 10 URLs three ways (sequential, threaded, `asyncio` + `aiohttp`) and prints timing comparison.
- **Push:** `feat(day10): concurrency - threading, multiprocessing, asyncio`

### Day 11 — Type Hints & Static Analysis
- `typing` module: `List`, `Dict`, `Optional`, `Union`, `Literal`, `TypedDict`, `Protocol`, generics (`TypeVar`)
- `mypy` setup and running it on your codebase
- **Task:** Add full type hints to all code written so far. Fix every `mypy` error until clean.
- **Push:** `chore(day11): add type hints, pass mypy strict mode`

### Day 12 — Testing
- `unittest` vs `pytest`, fixtures, parametrize, mocking (`unittest.mock`)
- Test structure, coverage (`pytest-cov`), TDD mindset
- **Task:** Write a `tests/` directory with `pytest` tests covering the library system and decorators (aim for >85% coverage).
- **Push:** `test(day12): add pytest suite with fixtures and mocks`

### Day 13 — Design Patterns & Capstone Mini-Project
- SOLID principles applied in Python
- Common patterns: Factory, Singleton, Strategy, Observer, Dependency Injection (conceptually)
- **Task:** Build a small CLI app ("Task Manager") using Factory pattern for task types and Strategy pattern for sorting/filtering. Full type hints + tests.
- **Push:** `feat(day13): CLI task manager - design patterns capstone`

---

## PHASE 3: FastAPI Fundamentals (Days 14–20)

### Day 14 — FastAPI Setup & First App
- Install FastAPI + Uvicorn, ASGI vs WSGI concept
- First app, automatic docs (`/docs`, `/redoc`), path operations (`GET`, `POST`)
- **Task:** New `fastapi_app/` inside repo. Build a "Hello World" API with 3 basic endpoints; explore auto-generated OpenAPI docs.
- **Push:** `feat(day14): fastapi project setup and first endpoints`

### Day 15 — Request Handling & Pydantic
- Path params, query params (optional/required, validation constraints)
- Request body with Pydantic `BaseModel`, nested models
- Pydantic v2 validators (`field_validator`, `model_validator`)
- **Task:** Build a `Product` CRUD skeleton (in-memory list) with full request validation.
- **Push:** `feat(day15): pydantic models and request validation`

### Day 16 — Responses & Status Codes
- `response_model`, `response_model_exclude`, status codes, `HTTPException`
- Multiple response types, `JSONResponse`, custom headers
- Error handling patterns, consistent error schema
- **Task:** Add proper status codes, response models, and a custom `NotFoundError` handler to the Product API.
- **Push:** `feat(day16): response models, status codes, error handling`

### Day 17 — Routing & Dependency Injection Basics
- `APIRouter`, splitting routes into modules, route tags, prefixes
- `Depends()` — reusable dependencies for pagination, common query params
- **Task:** Refactor Product API into routers (`products.py`, `health.py`); add a shared pagination dependency.
- **Push:** `refactor(day17): modular routers and basic dependency injection`

### Day 18 — Dependency Injection Deep Dive
- Class-based dependencies, dependency chains, `yield`-based dependencies for setup/teardown
- Sub-dependencies, overriding dependencies (important for testing)
- **Task:** Build a class-based dependency that simulates a "current user" and one that manages a fake DB session lifecycle with `yield`.
- **Push:** `feat(day18): advanced dependency injection with yield`

### Day 19 — Database Integration
- SQLAlchemy 2.0 (async), or `SQLModel` — engine, session, models
- Alembic for migrations
- **Task:** Set up PostgreSQL (or SQLite for local dev) with async SQLAlchemy. Define `Product` and `Category` models with a relationship. Run first Alembic migration.
- **Push:** `feat(day19): async SQLAlchemy setup with alembic migrations`

### Day 20 — Full CRUD with Database
- Repository pattern for DB access, async session dependency
- Full CRUD endpoints wired to real DB, pagination + filtering
- **Task:** Replace in-memory Product store with real DB-backed CRUD (create/read/update/delete/list with filters).
- **Push:** `feat(day20): full CRUD API backed by PostgreSQL`

---

## PHASE 4: Production FastAPI (Days 21–30)

### Day 21 — Authentication & Authorization
- OAuth2 password flow, JWT creation/validation (`python-jose` or `pyjwt`), password hashing (`passlib`/`bcrypt`)
- `Depends` for protected routes, role-based access control
- **Task:** Add `User` model, register/login endpoints, JWT-protected routes, and an admin-only endpoint.
- **Push:** `feat(day21): JWT authentication and role-based access control`

### Day 22 — Middleware & Global Exception Handling
- Custom middleware (logging, request timing), CORS setup
- Global exception handlers (`@app.exception_handler`), request validation error formatting
- **Task:** Add request-logging middleware, CORS config, and a global handler that returns a consistent error JSON shape for all exceptions.
- **Push:** `feat(day22): middleware, CORS, and global exception handlers`

### Day 23 — Background Tasks & WebSockets
- `BackgroundTasks` for fire-and-forget work (e.g., email simulation)
- WebSocket endpoints — connection lifecycle, broadcasting
- **Task:** Add a background task that "sends" a welcome email on registration. Build a simple WebSocket chat/notification endpoint.
- **Push:** `feat(day23): background tasks and websocket endpoint`

### Day 24 — File Handling
- File uploads (`UploadFile`), multipart forms, size/type validation
- Serving static files, streaming responses for large files
- **Task:** Add a product-image upload endpoint with validation and static file serving.
- **Push:** `feat(day24): file uploads and static file serving`

### Day 25 — Testing FastAPI
- `TestClient`/`httpx.AsyncClient`, overriding dependencies for tests, test DB (SQLite or test containers)
- `pytest-asyncio`, fixtures for auth tokens
- **Task:** Write an integration test suite covering auth, CRUD, and error cases. Target >80% coverage on the API layer.
- **Push:** `test(day25): full integration test suite for API`

### Day 26 — Settings, Config & Pydantic Settings
- `pydantic-settings` for environment-based config, `.env` handling
- Separate configs for dev/test/prod, secrets management basics
- **Task:** Replace hardcoded config with `Settings(BaseSettings)`, add `.env.example`, wire different settings per environment.
- **Push:** `refactor(day26): centralized config with pydantic-settings`

### Day 27 — Caching, Rate Limiting & Async Patterns
- Redis integration (`redis.asyncio`), caching strategy for read-heavy endpoints
- Rate limiting (e.g., `slowapi`), async best practices (avoiding blocking calls in async routes)
- **Task:** Add Redis caching to the product list endpoint and rate-limit the login endpoint.
- **Push:** `feat(day27): redis caching and rate limiting`

### Day 28 — Dockerizing the App
- Writing a production `Dockerfile` (multi-stage build), `docker-compose.yml` for app+DB+Redis
- Health checks, environment variable injection
- **Task:** Containerize the full stack; verify `docker-compose up` runs the entire app end to end.
- **Push:** `chore(day28): dockerize app with docker-compose stack`

### Day 29 — CI/CD & Deployment
- GitHub Actions: lint (`ruff`), type-check (`mypy`), test, build on push
- Deployment basics: Gunicorn+Uvicorn workers, Nginx reverse proxy, or deploying to Render/Fly.io/Railway
- **Task:** Add `.github/workflows/ci.yml` running lint+type-check+tests on every push. Deploy the app to a free-tier host.
- **Push:** `ci(day29): github actions pipeline and deployment config`

### Day 30 — Capstone Polish & Documentation
- Review entire codebase: consistent structure, docstrings, remove dead code
- Write a thorough `README.md` (architecture diagram, setup instructions, API overview)
- Tag a `v1.0.0` release
- **Task:** Final cleanup pass, complete README, verify all tests pass and Docker stack runs clean from a fresh clone.
- **Push:** `docs(day30): finalize README and tag v1.0.0 release`
```bash
git tag -a v1.0.0 -m "30-day Python + FastAPI mastery capstone"
git push origin v1.0.0
```

---

## After Day 30 — Where to Go Next
- GraphQL with FastAPI (`strawberry-graphql`)
- Event-driven architecture: FastAPI + RabbitMQ/Kafka
- Observability: structured logging, Prometheus metrics, OpenTelemetry tracing
- Kubernetes deployment of the same stack
- Load testing with `locust` or `k6`

## Daily Habit Checklist
- [ ] Read/study the day's concepts (30–45 min)
- [ ] Write code, no copy-pasting without understanding
- [ ] Run tests / verify it works
- [ ] Commit with a clear conventional-commit message
- [ ] Push to GitHub
- [ ] One sentence in README changelog: what you learned
