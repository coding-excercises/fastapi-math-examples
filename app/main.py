from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import views
import os

from datadog import initialize, statsd
from ddtrace import patch, config

# Configure and initialize datadog statsd
options = {
    'statsd_host':'0.0.0.0',
    'statsd_port':8125
}
initialize(**options)

# Enable datadog tracing
config.fastapi['service_name'] = 'fastapi-math-examples'
patch(fastapi=True)

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(views.router)