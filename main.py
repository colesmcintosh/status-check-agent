"""
Status Check Agent System - Multi-lingual, multi-agent service status monitoring system

This module implements a service status monitoring system that uses language-specific
agents to handle status inquiries in different languages. The system uses a router agent
to direct incoming status queries to specialized language agents (Spanish and English)
based on the query's language.

Features:
- Multi-language service status inquiries
- Automated language detection and routing
- Status checking for different locations
- Asynchronous operation

The system consists of three agents:
1. Router Agent - Handles language detection and routes status inquiries
2. Spanish Agent - Processes Spanish language status requests
3. English Agent - Processes English language status requests

Note: The current implementation uses a mock service status checker that returns
simulated responses. This can be replaced with actual service monitoring functionality
by implementing a new version of the get_service_status function that connects to
real services while maintaining the same interface.

Requirements:
- Python 3.9+
- OpenAI API key
- agents package
"""

from agents import Agent, Runner, function_tool
import asyncio
import random

@function_tool
def get_service_status(location: str) -> str:
    status_choices = ["online", "offline", "maintenance"]
    return f"The status of the service in {location} is {random.choice(status_choices)}."

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
    tools=[get_service_status],
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    tools=[get_service_status],
)


router_agent = Agent(
    name="Router agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
)


async def main():
    print("Spanish request")
    print("-" * len("Spanish request:"))
    result = await Runner.run(router_agent, input="¿Qué estado tiene el servicio de correo en Madrid?")
    print(result.final_output)
    print()
    print("English request")
    print("-" * len("English request"))
    result = await Runner.run(router_agent, input="What is the status of the email service in Oregon?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())