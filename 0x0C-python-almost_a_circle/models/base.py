#!/usr/bin/python3
"""module"""


class Base:
    """ the base """

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def __generate_id(cls):
        """
        Generates id
        """

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file
        """

        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if not isinstance(obj, cls):
                    raise TypeError("list_objs must contain only Base subclasses")

                row = [getattr(obj, attr) for attr in ["id", "width", "height", "x", "y"]]
                row.insert(0, cls.__name__)

                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        from models.rectangle import Rectangle
        from models.square import Square
        """
        Deserializes
        """

        filename = f"{cls.__name__}.csv"
        objects = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    class_name = row.pop(0)
                    if class_name == "Rectangle":
                        obj = Rectangle(*[int(val) for val in row])
                    elif class_name == "Square":
                        obj = Square(*[int(val) for val in row])
                    else:
                        raise ValueError(f"Unknown class name: {class_name}")

                    objects.append(obj)

        except FileNotFoundError:
            pass

        return objects
