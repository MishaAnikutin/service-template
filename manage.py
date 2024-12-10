import os
import click
from pathlib import Path

TEMPLATE_CONTROLLER = """from fastapi import APIRouter
from src.schemas import {capitalize_model_class}


{model_class}_router = APIRouter()

@{model_class}_router.get("/{{model_class}}")
async def get_handler({model_class}: {capitalize_model_class}):
   ...

@{model_class}_router.post("/")
async def post_handler({model_class}: {capitalize_model_class}):
   ...

@{model_class}_router.put("/{{model_class}}")
async def put_handler({model_class}: {capitalize_model_class}):
   ...

@{model_class}_router.patch("/{{model_class}}")
async def patch_handler({model_class}: {capitalize_model_class}):
   ...

@{model_class}_router.delete("/{{model_class}}")
async def delete_handler({model_class}: {capitalize_model_class}):
   ...
"""

TEMPLATE_SERVICE = """from abc import ABC, abstractmethod


class {capitalize_model_class}ServiceI(ABC):
    ...

class {capitalize_model_class}Service({capitalize_model_class}ServiceI):
    ...
"""

TEMPLATE_GATEWAY = """from abc import ABC, abstractmethod


class {capitalize_model_class}GatewayI(ABC):
    ...

class {capitalize_model_class}Gateway({capitalize_model_class}GatewayI):
    ...
"""


TEMPLATE_SCHEMA = """from pydantic import BaseModel


class {capitalize_model_class}(BaseModel):
    ...

"""

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def create_file(directory: str, name: str, template: str) -> None:
    write_file(
        Path(f'src/{directory}') / f'{name}.py',
        template
    )
     
@click.group()
def cli():
    """Manage your Python web application."""
    pass


@cli.command()
@click.argument('name')
def new_controller(name: str):
    """Create a new controller."""
    
    create_file(
        name=name,
        directory='controller', 
        template=TEMPLATE_CONTROLLER.format(
            model_class=name,
            capitalize_model_class=name.capitalize()
        )
    )
    
    print(f'controller {name} created successful!')


@cli.command()
@click.argument('name')
def new_service(name: str):
    """Create a new service."""
    
    create_file(
        name=name,
        directory='service', 
        template=TEMPLATE_SERVICE.format(
            capitalize_model_class=name.capitalize()
        )
    )

    print(f'service {name} created successful!')

@cli.command()
@click.argument('name')
def new_gateway(name: str):
    """Create a new gateway."""
    
    create_file(
        name=name,
        directory='gateway', 
        template=TEMPLATE_GATEWAY.format(
            capitalize_model_class=name.capitalize()
        )
    )

    print(f'gateway {name} created successful!')

@cli.command()
@click.argument('name')
def new_schema(name: str):
    """Create a new schema."""
    
    create_file(
        name=name,
        directory='schema', 
        template=TEMPLATE_SCHEMA.format(
            capitalize_model_class=name.capitalize()
        )
    )

    print(f'schema {name} created successful!')
    

if __name__ == '__main__':
    cli()
