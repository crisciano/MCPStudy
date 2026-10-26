# Database Schema for MCP Study

## states
*   `id` (PK)
*   `name`
*   `abbreviation`
*   `created_at`
*   `updated_at`

## cities
*   `id` (PK)
*   `name`
*   `state_id` (FK to states.id)
*   `created_at`
*   `updated_at`

## dealerships
*   `id` (PK)
*   `name`
*   `city_id` (FK to cities.id)
*   `created_at`
*   `updated_at`

## vehicles
*   `id` (PK)
*   `name`
*   `vehicle_type`
*   `price`
*   `created_at`
*   `updated_at`

## salespeople
*   `id` (PK)
*   `name`
*   `dealership_id` (FK to dealerships.id)
*   `created_at`
*   `updated_at`

## customers
*   `id` (PK)
*   `name`
*   `address`
*   `created_at`
*   `updated_at`

## sales
*   `id` (PK)
*   `vehicle_id` (FK to vehicles.id)
*   `salespeople_id` (FK to salespeople.id)
*   `customer_id` (FK to customers.id)
*   `dealership_id` (FK to dealerships.id)
*   `sale_price`
*   `created_at`
*   `updated_at`

4. Create a New Django Project:
`django-admin startproject core .`

5. Create a Django Application:
`python manage.py startapp states`
`python manage.py startapp cities`
`python manage.py startapp dealerships`
`python manage.py startapp vehicles`
`python manage.py startapp salespeople`
`python manage.py startapp customers`
`python manage.py startapp sales`

6. Create Django Models:
`python manage.py makemigrations`
`python manage.py migrate`

`python manage.py createsuperuser`
cris@cris.com
C0nnect123
Sup3rR00t

`python manage.py runserver`

## kill port
`sudo lsof -i :8000`
```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  21074 root    3u  IPv4  69446      0t0  TCP localhost:8000 (LISTEN)
```
`kill 21074`

## run service
`mcp run services/mcp_test.py --transport sse`
`mcp run services/mcp_test.py --transport sse --verbose`
`mcp dev services/mcp_test.py`
`mcp dev utils/mcp_tools_sql.py`


## install packages
`pip install -U mcp[cli]`
`pip install -U typer`

## inspect 
`npx @modelcontextprotocol/inspector`

## check func
`mcp run --url http://localhost:8000 get_total_sales_revenue`


## 1 - config pyenv
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

## 2 - init venv
`python -m venv venv`

## 3 - activate venv
`source venv/bin/activate`

## 4 - install pip-tools
`pip install pip-tools`


# django mcp

pip install django-mcp

https://pypi.org/project/django-mcp/
