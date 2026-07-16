from abc import ABC, abstractmethod
from typing import Any 
class BaseLLMClient(ABC):
    """
        Abstract base class for LLM clients. All LLM clients should inherit from this class and implement the generate method[Interface].
    """

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> dict[str,Any]:
        """
            Generate a response from the LLM based on the provided prompt.

            Args:
                prompt (str): The input prompt for the LLM.
                
            Returns:
                dict: The response from the LLM.
            """
        ...  # "There is intentionally no implementation.