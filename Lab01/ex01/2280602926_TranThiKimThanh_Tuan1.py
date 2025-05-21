def show_math_operators():
    a = int(input())
    b = int(input())
    print("Tổng:", a + b)
    print("Hiệu:", a - b)
    print("Tích:", a * b)
    print("Thương:", a / b)
    print("Chia lấy nguyên:", a // b)
    print("Chia lấy dư:", a % b)
    print("Lũy thừa:", a ** b)

def show_logic_operators():
    x = True
    y = False
    print("AND:", x and y)
    print("OR:", x or y)
    print("NOT:", not x)

def show_string_operations():
    text = "Python Programming"
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Substring:", text[0:6])

def greet_user():
    name = input("Nhập tên: ")
    print(f"Chào bạn, {name}")

def age_check():
    age = int(input("Nhập tuổi của bạn: "))
    if age < 18:
        print("Bạn chưa đủ tuổi")
    elif age < 65:
        print("Bạn đã đủ tuổi đi tù")
    else:
        print("Già rồi cha ơi")

def list_example():
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    print("Danh sách:", my_list)

def tuple_example():
    my_tuple = (1, 2, 3)
    print("Tuple:", my_tuple)
    print("Phần tử đầu tiên:", my_tuple[0])

def dict_example():
    my_dict = {"name": "Alice", "age": 25}
    print("Dictionary:", my_dict)
    print("Tên:", my_dict["name"])
    print("Tuổi:", my_dict["age"])

def oop_example():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

    my_car = Car("Toyota", "Corolla")
    print("Xe của bạn:", my_car.brand, my_car.model)

def inheritance_example():
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        def bark(self):
            return "Woof!"

    my_dog = Dog()
    print("Kế thừa speak():", my_dog.speak())
    print("Phương thức riêng bark():", my_dog.bark())

def polymorphism_example():
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    def animal_sound(animal):
        print("Âm thanh:", animal.speak())

    animal_sound(Cat())
    animal_sound(Dog())

def abstract_example():
    from abc import ABC, abstractmethod

    class AbstractAnimal(ABC):
        @abstractmethod
        def sound(self):
            pass

    class Dog(AbstractAnimal):
        def sound(self):
            return "Woof!"

    my_dog = Dog()
    print("Tiếng chó kêu:", my_dog.sound())

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Toán tử số học")
        print("2. Toán tử logic")
        print("3. Xử lý chuỗi")
        print("4. Greet người dùng")
        print("5. Kiểm tra độ tuổi")
        print("6. Danh sách (List)")
        print("7. OOP - Lớp và đối tượng")
        print("8. Lớp trừu tượng (Abstract)")
        print("9. Tuple")
        print("10. Dictionary")
        print("11. Kế thừa")
        print("12. Đa hình")
        print("0. Thoát")

        try:
            choice = int(input("Chọn chức năng: "))
        except ValueError:
            print("Vui lòng nhập một số.")
            continue

        match choice:
            case 1:
                show_math_operators()
            case 2:
                show_logic_operators()
            case 3:
                show_string_operations()
            case 4:
                greet_user()
            case 5:
                age_check()
            case 6:
                list_example()
            case 7:
                oop_example()
            case 8:
                abstract_example()
            case 9:
                tuple_example()
            case 10:
                dict_example()
            case 11:
                inheritance_example()
            case 12:
                polymorphism_example()
            case 0:
                print("Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()