# my_app/tools.py
from django_mcp import mcp_app as mcp
from mcp.server.fastmcp import Context

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool()
async def get_user_info_from_path(ctx: Context) -> str:
    """Retrieves user info based on user_uuid from the URL path."""
    # Access path parameters captured during mounting
    path_params = getattr(ctx, 'path_params', {})
    user_uuid = path_params.get('user_uuid', None)

    if not user_uuid:
        await ctx.error("User UUID not found in path parameters.")
        return "Error: User UUID missing."

    # Example: Fetch user from database (requires async ORM or sync_to_async)
    # try:
    #     user = await User.objects.aget(uuid=user_uuid)
    #     return f"User found: {user.username}"
    # except User.DoesNotExist:
    #     await ctx.warning(f"User with UUID {user_uuid} not found.")
    #     return f"Error: User {user_uuid} not found."

    # Simplified example returning the uuid
    await ctx.info(f"Retrieved user_uuid: {user_uuid}")
    return f"Retrieved user_uuid: {user_uuid}"