import os


def get_from_env(env_var_name: str) -> str:
    if env_var_name not in os.environ:
        raise Exception(f"Environment variable {env_var_name} has to be set!")
    return os.environ[env_var_name]
