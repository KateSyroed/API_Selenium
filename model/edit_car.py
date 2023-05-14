# edit car by ID /cars/{id}
class EditCarPutModel:
    def __init__(self, carBrandId, carModelId, mileage):
        self.carBrandId = carBrandId
        self.carModelId = carModelId
        self.mileage = mileage