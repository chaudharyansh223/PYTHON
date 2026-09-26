class AgeLimitError(Exception):
    pass


def register_voter(name, age):
    if not isinstance(age, int):
        raise TypeError("Age must be an interger")
    elif age < 18:
        raise AgeLimitError(f"{name} is under 18")
    elif age > 18:
        print(f"registration successful for {name}")
    return True
    


def main():
    try:
        register_voter("Rahul", 15)
    except AgeLimitError as e:
        print(f"Caught AgeLimitError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: age must be an integer")


if __name__ == "__main__":
    main()
