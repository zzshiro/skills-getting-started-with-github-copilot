"""
MCP Server for Mergington High School Activities API

Exposes the activities management system as MCP tools so AI assistants
can view activities and sign up students on behalf of users.
"""

import sys
import os

# Add the src directory to path so we can import app data
sys.path.insert(0, os.path.dirname(__file__))

from mcp.server.fastmcp import FastMCP
# Import the shared activities dictionary from the FastAPI app.
# Both the web API and MCP server operate on the same in-memory data,
# so changes made through either interface are immediately reflected in the other.
from app import activities

mcp = FastMCP("Mergington High School Activities")


@mcp.tool()
def get_activities() -> dict:
    """Get all available extracurricular activities with their details and current participants."""
    return activities


@mcp.tool()
def signup_for_activity(activity_name: str, email: str) -> dict:
    """Sign up a student for an extracurricular activity.

    Args:
        activity_name: The name of the activity to sign up for (e.g. "Chess Club")
        email: The student's school email address (e.g. "student@mergington.edu")
    """
    if activity_name not in activities:
        return {"error": f"Activity '{activity_name}' not found"}

    activity = activities[activity_name]

    if email in activity["participants"]:
        return {"error": f"Student {email} is already signed up for {activity_name}"}

    if len(activity["participants"]) >= activity["max_participants"]:
        return {"error": f"Activity '{activity_name}' is full"}

    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


if __name__ == "__main__":
    mcp.run()
