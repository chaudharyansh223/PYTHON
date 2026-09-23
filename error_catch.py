class InvalidPortError(Exception):
    pass
  
def Valid_port(port):
    try:
        if not isinstance(port, int) or port < 1 or port > 65535:
            raise InvalidPortError(f"Port {port} is out of valid range (1-65535)")
        return True
    except InvalidPortError as e:
        print(f"Caught error: {e}")



Valid_port(70000)



