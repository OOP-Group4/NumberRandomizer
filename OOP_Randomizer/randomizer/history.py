from typing import List, Dict, Union

class HistoryManager:
    def __init__(self):
        self.logs: Dict[str, List[Union[int, List[int]]]] = {"ByRange": [], "ByList": []}

    def update_history(self, category: str, result: Union[int, List[int]]) -> None:
        if category in self.logs:
            self.logs[category].append(result)
        else:
            raise ValueError(f"Invalid category: {category}")

    def get_history(self, category: str) -> List[Union[int, List[int]]]:
        if category in self.logs:
            return self.logs[category]
        raise ValueError(f"Invalid category: {category}")

    def clear_history(self, category: str) -> None:
        if category in self.logs:
            self.logs[category] = []
        else:
            raise ValueError(f"Invalid category: {category}")

    def clear_all_history(self) -> None:
        for key in self.logs:
            self.logs[key] = []
