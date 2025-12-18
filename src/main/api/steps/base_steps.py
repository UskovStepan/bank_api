from typing import List, Any



class BaseSteps:
    def __init__(self, created_obj: List[Any]):
        self.create_obj = created_obj