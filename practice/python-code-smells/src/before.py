"""
Basic example of a Vehicle registration system.
"""
from dataclasses import dataclass
from enum import Enum, auto
from random import *  # Bad practice use explicit imports no wildcard imports
from string import *

# FIXME: from string import xyz is not a good practice, use explicit imports and dots after that


class FuelType(Enum):
    """Types of fuel used in a vehicle."""

    ELECTRIC = auto()
    PETROL = auto()


class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system."""

    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()


taxes = {FuelType.ELECTRIC: 0.02, FuelType.PETROL: 0.05}


@dataclass
class VehicleInfoMissingError(Exception):
    """Custom error that is raised when vehicle information is missing for a particular brand."""

    brand: str
    model: str
    message: str = "Vehicle information is missing."


# INFO: When to use __str__ vs __repr__?
#    repr() is for developers, str() is for customers.
#    repr() recreates the object, str() is a human-readable representation of the object.


@dataclass
class VehicleModelInfo:
    """Class that contains basic information about a vehicle model."""

    # FIME: No default value
    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType
    production_year: int

    @property
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type."""
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def get_info_str(
        self,
    ) -> (
        str
    ):  # FIXME: use dunder method instead. and the to_string method name is better, since it is used in Vehicle class
        """String representation of this instance."""
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax}"


@dataclass
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)."""

    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """String representation of this instance."""
        info_str = self.info.get_info_str()
        return f"Id: {self.vehicle_id}. License plate: {self.license_plate}. Info: {info_str}."


class VehicleRegistry:
    """Class representing a basic vehicle registration system."""

    def __init__(self) -> None:
        self.vehicle_models: list[
            VehicleModelInfo
        ] = []  # FIXME: Use dictionary instead for O(1)read
        self.online = True

    def add_vehicle_model_info(
        self,  # FIXME: Too many parameters. Use a dataclass instead.
        brand: str,
        model: str,
        catalogue_price: int,
        fuel_type: FuelType,
        year: int,
    ) -> None:
        """Helper method for adding a VehicleModelInfo object to a list."""
        self.vehicle_models.append(
            VehicleModelInfo(brand, model, catalogue_price, fuel_type, year)
        )

    # FIXME: Not using the self. Remove it and turn this into a static method
    # INFO: Class methods methods that has access to class instance. static method can't do that.
    def generate_vehicle_id(self, length: int) -> str:
        """Helper method for generating a random vehicle id."""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """Helper method for generating a vehicle license number."""
        return f"{_id[:2]}-{''.join(choices(digits, k=2))}-{''.join(choices(ascii_uppercase, k=2))}"

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate."""

        # FIXME: Too deeply nesting - split things out. There are two responsibilities here
        #   1. Find the vehicle info
        #   2. Create the vehicle
        # FIXME: Combind the two condition
        # FIXME: Handle the error first, it reduces the indentation, increasing the readability
        for vehicle_info in self.vehicle_models:
            if vehicle_info.brand == brand:
                if vehicle_info.model == model:
                    vehicle_id = self.generate_vehicle_id(12)
                    license_plate = self.generate_vehicle_license(vehicle_id)
                    return Vehicle(vehicle_id, license_plate, vehicle_info)
        raise VehicleInfoMissingError(brand, model)

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online."""
        return (
            RegistryStatus.OFFLINE  # FIXME: Nested if-else is not necessary, harde to read. Use the regular if statement instead
            if not self.online
            else RegistryStatus.CONNECTION_ERROR
            if len(self.vehicle_models) == 0
            else RegistryStatus.ONLINE
        )


if __name__ == "__main__":
    # FIXME: Use a main function instead
    #    the variables defined here are global variables(module scope), which is not a good practice

    # create a registry instance
    registry = VehicleRegistry()

    # add a couple of different vehicle models
    registry.add_vehicle_model_info("Tesla", "Model 3", 50000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("Volkswagen", "ID3", 35000, FuelType.ELECTRIC, 2021)
    registry.add_vehicle_model_info("BMW", "520e", 60000, FuelType.PETROL, 2021)
    registry.add_vehicle_model_info("Tesla", "Model Y", 55000, FuelType.ELECTRIC, 2021)

    # verify that the registry is online
    print(f"Registry status: {registry.online_status()}")

    # register a new vehicle
    vehicle = registry.register_vehicle("Volkswagen", "ID3")

    # print out the vehicle information
    print(vehicle.to_string())
