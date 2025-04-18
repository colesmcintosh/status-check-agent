# Status Check Agent System

A multi-lingual, multi-agent service status checking system that uses specialized agents to respond to status inquiries in different languages.

## Overview

This project demonstrates a service status monitoring system where a router agent directs incoming status inquiries to language-specific agents based on the query's language. The system supports status checks in English and Spanish, making it accessible to users of different languages.

## Features

- Multi-language service status inquiries
- Automated language detection and routing
- Status checking for different locations
- Asynchronous operation

## Components

### Agents

1. **Router Agent**
   - Routes status inquiries to appropriate language agents
   - Handles language detection and delegation

2. **Language Agents**
   - Spanish Agent for Spanish status inquiries
   - English Agent for English status inquiries
   - Each agent provides service status information in its designated language

### Tools

- `get_service_status`: A mock implementation of a service status checker
  - Currently returns simulated status (online, offline, or maintenance)
  - Can be replaced with actual service monitoring functionality
  - Designed to be easily swappable with real status checking implementations
  - Provides responses in the user's preferred language

## Usage

```python
# Run the status check demonstration
python main.py
```

Example output:
```
Spanish request
----------------
El servicio de correo en Madrid está en mantenimiento.

English request
---------------
The email service in Oregon is currently offline.
```

## Requirements

- Python 3.9+
- OpenAI API key
- `agents` package