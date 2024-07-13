from eidolon_ai_sdk.agent.agent import register_program

class JackieWorld:
    @register_program()
    async def execute(self, name: Annotated[str, Body(description="Your name", embed=True)]) -> IdleStateRepresentation:
        return IdleStateRepresentation(welcome_message=f"Hello, welcome to Jackie's world {name}!")