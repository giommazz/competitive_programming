class Vehicle:
    
    """A simple vehicle with brand and production year."""

    def __init__(self, brand: str, production_year: int):
        self.brand = brand
        self.production_year = production_year
    
    def __str__(self):
        return f"{self.brand} ({self.production_year})"
    
    def __repr__(self):
        return f"Vehicle(brand={self.brand!r}, production_year={self.production_year})"


