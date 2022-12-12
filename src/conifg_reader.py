from typing import Optional
from dataclasses import dataclass, asdict

configs = {
    "type": "pagination",
    "max_clicks": 17

}

class ConfigManager:
    def __init__(self, config):
        self.config = config


@dataclass
class Params:
    gathering_type: Optional[str] = "html"
    type: Optional[str] = "scroll-down"
    max_clicks: Optional[int] = 3

    def set_gathering_type(self, config: dict) -> None:
        if "gathering_type" in config:
            self.gathering_type = config["gathering_type"]

    def set_type(self, config: dict) -> None:
        if "type" in config:
            self.type = config["type"]

    def set_max_clicks(self, config: dict) -> None:
        if "max_clicks" in config:
            self.max_clicks = config["max_clicks"]

    def set_all(self, config: dict) -> None:
        self.set_gathering_type(config)
        self.set_type(config)
        self.set_max_clicks(config)

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

if __name__ == '__main__':

    params = Params()

    params.set_all(configs)
    print(params)
    dict_params = asdict(params)
    print(dict_params)


