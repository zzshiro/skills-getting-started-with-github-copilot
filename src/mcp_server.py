"""
MCP Server for Mergington High School Activities API

Exposes the activities management system as MCP tools so AI assistants
can view activities and sign up students on behalf of users.
"""

from mcp.server.fastmcp import FastMCP
# Import shared data and logic from the FastAPI app.
# Both the web API and MCP server operate on the same in-memory data,
# so changes made through either interface are immediately reflected in the other.
from app import activities, perform_signup

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
    try:
        message = perform_signup(activity_name, email)
        return {"message": message}
    except (KeyError, ValueError) as e:
        return {"error": e.args[0]}


if __name__ == "__main__":
    mcp.run()
