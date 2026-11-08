from __future__ import annotations

from myloai.backends.base import LLMBackend
from myloai.backends.ollama import OllamaBackend
from myloai.backends.openai import OpenAICompatibleBackend
from myloai.core.config import ProviderProfile


def create_backend(profile: ProviderProfile) -> LLMBackend:
    if profile.provider_type == "openai":
        return OpenAICompatibleBackend(profile.base_url, profile.api_key)
    if profile.provider_type == "llama.cpp":
        return OpenAICompatibleBackend(profile.base_url, profile.api_key)
    return OllamaBackend(profile.base_url, profile.api_key)
