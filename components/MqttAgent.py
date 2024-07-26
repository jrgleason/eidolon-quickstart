from eidolon_ai_sdk.agent.agent import register_program
from fastapi import UploadFile, Body
from pydantic import BaseModel, Field
from typing import Annotated
import paho.mqtt.client as mqtt



class IdleStateRepresentation(BaseModel):
    welcome_message: str


class NestedObject(BaseModel):
    str_field: str
    int_field: int
    float_field: float
    bool_field: bool


class ComplexInput(BaseModel):
    int_field: int = Field(description="An integer field")
    float_field: float = Field(description="A float field")
    bool_field: bool = Field(description="A boolean field")
    str_field: str = Field(description="A string field")
    optional_str_field: str = Field(default=None, description="An optional string field")

    nested_object: NestedObject = Field(description="A nested object")
    optional_nested_object: NestedObject = Field(default=None, description="A nested object")

    array_of_strings: list[str] = Field(description="An array of strings")
    optional_array_of_strings: list[str] = Field(default=None, description="An array of strings")
    array_of_objects: list[NestedObject] = Field(description="An array of objects")

    single_file: UploadFile = Field(description="A single file")
    multiple_files: list[UploadFile] = Field(description="A list of files")

    optional_file: UploadFile = Field(default=None, description="A single file")
    optional_multiple_files: list[UploadFile] = Field(default=None, description="A list of files")


class MqttAgent:
    @register_program()
    async def connect_and_subscribe(
            self,
            broker: Annotated[str, Body(description="MQTT Broker URL", embed=True)],
            port: Annotated[int, Body(description="MQTT Broker Port", embed=True)],
            topic: Annotated[str, Body(description="MQTT Topic to subscribe to", embed=True)],
            password: Annotated[str, Body(description="MQTT Password", embed=True)],
            username: Annotated[str, Body(description="MQTT Username", embed=True)],
    ) -> IdleStateRepresentation:
        def on_message(client, userdata, message):
            print(f"Received message: {message.payload.decode()} on topic {message.topic}")

        client = mqtt.Client()
        client.on_message = on_message

        if username and password:
            client.username_pw_set(username, password)

        client.connect(broker, port)
        client.subscribe(topic)
        client.loop_start()

        return IdleStateRepresentation(welcome_message=f"Subscribed to {topic} on {broker}:{port}")
