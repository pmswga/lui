import json
from typing import Any

from lark import Token, Transformer


class IRError(Exception):
    pass


class Property:
    """UI property definition"""

    def __init__(self, name: str = "", value: str | int | None = None) -> None:
        self.name: str = name
        self.value: str | int | None = value

    def getName(self) -> str:
        return self.name

    def getValue(self) -> str | int | None:
        return self.value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"


class Component:
    """UI component definition"""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.properties: dict = {}
        self.components: list[Component] = []

    def getName(self) -> str:
        return self.name

    def getProperty(self, name: str) -> Property | None:
        assert name != ""
        return self.properties.get(name)

    def getProperties(self) -> list[Property]:
        return list(self.properties.values())

    def getComponent(self, name: str, get_first: bool = False) -> Any | None:
        components = list(filter(lambda c: c.getName() == name, self.components))
        if components and get_first:
            return components[0]
        else:
            return components

    def getComponents(self) -> list["Component"]:
        return self.components


class StringRepresentation:
    """String representation of IR"""

    def __init__(self, ir: "IRRepresentation") -> None:
        self.string_repr = []
        self.walk(ir.getComponent())

    def walk(self, component: Component, level: int = 0):
        indent = "  " * level

        self.string_repr.append(f"{indent}{component.name}")

        for p in component.getProperties():
            value = p.getValue()
            value = f'"{value}"' if isinstance(value, str) else value
            self.string_repr.append(f"{indent} {p.getName()}: {value}")

        self.string_repr.append("")

        for c in component.getComponents():
            self.walk(c, level + 1)

    def __str__(self) -> str:
        return "\n".join(self.string_repr)


class JSONRepresentation:
    """JSON representation of IR"""

    def __init__(self, ir: "IRRepresentation", indent: int = 4) -> None:
        assert indent >= 0
        self.indent = indent
        self.json_repr: dict[str, Any] = self.walk(ir.getComponent())

    def walk(self, component: Component) -> dict[str, Any]:
        return {
            "name": component.getName(),
            "properties": {
                p.getName(): p.getValue() for p in component.getProperties()
            },
            "components": [self.walk(c) for c in component.getComponents()],
        }

    def toDict(self) -> dict[str, Any]:
        return self.json_repr

    def __str__(self) -> str:
        return json.dumps(self.json_repr, indent=self.indent, ensure_ascii=False)


class IRRepresentation:
    """Inner representation of UI"""

    def __init__(self, name: str) -> None:
        self.tree: Component = Component(name)

    def getComponent(self) -> Component:
        return self.tree

    def addComponent(self, component: Component) -> None:
        self.tree.components.append(component)

    def addProperty(self, property: Property) -> None:
        if property.getName() in self.tree.properties:
            raise IRError(f'Property "{property.getName()}" already exists')
        else:
            self.tree.properties[property.getName()] = property


class Lexer2IR(Transformer):
    """Builds a IRRepresentation from a Lark parse tree."""

    def main_component(self, children: list[Token]) -> str:
        return str(children[0])

    def component_name(self, children: list[Token]) -> str:
        return children[0].strip()

    def property_name(self, children: list[Token]) -> str:
        return children[0].strip()

    def property_value(self, children: list[Token]) -> str | int:
        token = children[0]
        if token.type == "NUMBER":
            return int(token)

        # Remove quotes
        return str(token)[1:-1]

    def property(self, children: list) -> Property:
        return Property(children[0], children[1])

    def component(self, children: list) -> Component:
        name, *body = children
        component = Component(name)
        for item in body:
            if isinstance(item, Property):
                # same as UIRepresentation.addProperty: the first value wins
                component.properties.setdefault(item.getName(), item)
            elif isinstance(item, Component):
                component.components.append(item)
        return component

    def grammar(self, children: list) -> IRRepresentation:
        name, *body = children
        ui = IRRepresentation(name)
        for item in body:
            if isinstance(item, Property):
                ui.addProperty(item)
            elif isinstance(item, Component):
                ui.addComponent(item)
        return ui
