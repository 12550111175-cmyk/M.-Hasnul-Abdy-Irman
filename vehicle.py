class Vehicle:
    def __init__(self, brand, model):
        if not isinstance(brand, str) or not isinstance(model, str):
            raise ValueError("Brand dan Modelnya harus berupa string broo")        
        
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)

        if doors <= 1:
            raise ValueError("Jumlh pintu mobil harus lebih dari 1, gak mungkin kan cuman ada 1 pintu aja")
        
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)

        if load_capacity <= 0:
            raise ValueError("Kapasitas yang bisa truk gak mungkin 0 atau kurangkan")
        
        self.load_capacity = load_capacity

    def load(self, weight):
        try:
            if weight < 0:
                raise ValueError("Berat tidak boleh negatif")
            
            if weight > self.load_capacity:
                raise ValueError("Muatan yang dimasukkan lebih dari kapasitas euyy")
            
            print(f"loaded {weight} kg")

        except ValueError as e:
            print("Error:", e)

def main():
    try:
        my_car = Car("Toyota", "Corolla", 4)
        my_truck = Truck("Ford", "F-150", 1000)

        my_car.drive()
        my_car.honk()

        my_truck.drive()
        my_truck.load(1200)

    except ValueError as e:
        print("Terjadi kesalahan:", e)

    finally:
        print("Program telah selesai")

if __name__ == "__main__":
    main()