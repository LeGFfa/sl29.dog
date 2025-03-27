"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass


class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        _race (str): La race du chien.
        _sex (str): Le sexe du chien ('M' ou 'F').
        name (str): Le nom du chien.
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race
        self._sex = sex
        self.name = name

    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        Retourne le sex du chien.

        Returns:
            str: Le sex du chien.
        """
        return self._sex

    def __str__(self) -> str:
        """
        DOCSTRINGS A COMPLETER
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"

    def bark(self, n: int = 1) -> str:
        return "Woff" * n

    def chew(self, stuff: str) -> str:
        """Retire la dernière lettre d'une chaîne de caractères.
        
        Args:
            stuff (str): La chaîne à modifier.
            
        Returns:
            str: La chaîne sans sa dernière lettre.
        """
        if len(stuff) > 0:
            return stuff[:-1]
        return stuff

if __name__ == "__main__":
    pass


