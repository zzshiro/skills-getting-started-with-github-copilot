"""
Mergington High School Activities MCP Server

An MCP (Model Context Protocol) server that exposes the Mergington High School
extracurricular activities API as tools for AI assistants.
"""

from mcp.server.fastmcp import FastMCP
from src.app import activities

# Initialize the MCP server
mcp = FastMCP("Mergington High School Activities")


@mcp.tool()
def get_activities() -> dict:
    """Get all available extracurricular activities at Mergington High School.

    Returns a dictionary of activities with their descriptions, schedules,
    maximum participant counts, and current participant lists.
    """
    return activities


@mcp.tool()
def signup_for_activity(activity_name: str, email: str) -> dict:
    """Sign up a student for an extracurricular activity.

    Args:
        activity_name: The name of the activity to sign up for (e.g. "Chess Club")
        email: The student's email address

    Returns:
        A message confirming the signup.

    Raises:
        ValueError: If the activity is not found, the student is already signed up,
                    or the activity is full.
    """
    if activity_name not in activities:
        raise ValueError(f"Activity '{activity_name}' not found")

    activity = activities[activity_name]

    if email in activity["participants"]:
        raise ValueError(f"Student {email} is already signed up for {activity_name}")

    if len(activity["participants"]) >= activity["max_participants"]:
        raise ValueError(f"Activity '{activity_name}' is full")

    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


if __name__ == "__main__":
    mcp.run()
