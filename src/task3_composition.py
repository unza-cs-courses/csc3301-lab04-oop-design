"""
Task 3: Composition over Inheritance

This module demonstrates the "composition over inheritance" principle by building
a flexible vehicle system without the "class explosion" problem.

The Problem with Inheritance:
If you use inheritance to combine features, you get exponential class growth:
- Car, Boat, Plane (3 classes)
- CarWithEngine, BoatWithEngine, PlaneWithEngine (6 classes)
- CarWithEngineAndWheels, BoatWithEngineAndWheels, PlaneWithEngineAndWheels (9+ classes)

The Solution - Composition:
Instead of creating classes for every combination, use composition to give
vehicles the features they need as objects. This is flexible and scales linearly.

Key Concept: A vehicle IS NOT a sum of its features; a vehicle HAS features.
"""

from abc import ABC, abstractmethod


class Feature(ABC):
    """
    Abstract base class for vehicle features.

    Each feature represents a capability that a vehicle can have.
    Features are composed into vehicles rather than inherited.
    """

    @abstractmethod
    def describe(self) -> str:
        """
        Return a description of what this feature does.

        Returns:
            A string describing the feature's action
        """
        # TODO: Subclasses must implement this
        pass


class Engine(Feature):
    """
    Engine feature - allows vehicles to start and move.
    """

    def describe(self) -> str:
        """
        Return a description of the engine's action.

        Returns:
            The string "Engine started"
        """
        # TODO: Return the engine action
        pass


class Wheels(Feature):
    """
    Wheels feature - allows vehicles to roll on ground.
    """

    def describe(self) -> str:
        """
        Return a description of the wheels' action.

        Returns:
            The string "Wheels rolling"
        """
        # TODO: Return the wheels action
        pass


class Wings(Feature):
    """
    Wings feature - allows vehicles to fly through the air.
    """

    def describe(self) -> str:
        """
        Return a description of the wings' action.

        Returns:
            The string "Wings deployed"
        """
        # TODO: Return the wings action
        pass


class Propeller(Feature):
    """
    Propeller feature - allows vehicles to move through water.
    """

    def describe(self) -> str:
        """
        Return a description of the propeller's action.

        Returns:
            The string "Propeller spinning"
        """
        # TODO: Return the propeller action
        pass


class Vehicle:
    """
    A vehicle composed of features.

    Instead of creating inheritance hierarchies for every vehicle type,
    a Vehicle simply contains a list of features. This is much more flexible
    and allows for arbitrary combinations.

    Example:
        car = Vehicle([Engine(), Wheels()])
        boat = Vehicle([Engine(), Propeller()])
        plane = Vehicle([Engine(), Wings()])
    """

    def __init__(self, name: str, features: list):
        """
        Initialize a vehicle with a name and list of features.

        Args:
            name: The name of the vehicle (e.g., "Car", "Boat", "Plane")
            features: A list of Feature objects this vehicle has
        """
        # TODO: Store the name and features
        pass

    def describe(self) -> list:
        """
        Get descriptions of all this vehicle's features.

        Returns:
            A list of strings, one for each feature's description
        """
        # TODO: Return a list of descriptions from each feature
        pass

    def has_feature(self, feature_type: type) -> bool:
        """
        Check if this vehicle has a particular feature type.

        Args:
            feature_type: A Feature class to check for (e.g., Engine, Wheels)

        Returns:
            True if the vehicle has a feature of that type, False otherwise
        """
        # TODO: Check if any feature is an instance of feature_type
        pass
