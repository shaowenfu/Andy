"""
配置管理模块 - 统一管理系统配置和环境变量
"""
import os
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

class Config:
    """配置管理类，负责加载和提供系统配置"""
    
    _instance = None
    
    def __new__(cls):
        """单例模式实现"""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """初始化配置"""
        if self._initialized:
            return
            
        self._config = {
            # 默认配置
            "app": {
                "name": "Andy AI Assistant",
                "version": "0.1.0",
                "debug": os.getenv("DEBUG", "False").lower() == "true",
                "host": os.getenv("HOST", "0.0.0.0"),
                "port": int(os.getenv("PORT", "5000"))
            },
            "llm": {
                "provider": os.getenv("LLM_PROVIDER", "openai"),
                "model": os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
                "api_key": os.getenv("OPENAI_API_KEY", ""),
                "temperature": float(os.getenv("LLM_TEMPERATURE", "0.7")),
                "max_tokens": int(os.getenv("LLM_MAX_TOKENS", "2000"))
            },
            "memory": {
                "db_path": os.getenv("MEMORY_DB_PATH", "memory.db"),
                "max_conversation_turns": int(os.getenv("MAX_CONVERSATION_TURNS", "10"))
            }
        }
        
        # 尝试从配置文件加载
        config_path = os.getenv("CONFIG_PATH", "config/config.json")
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    # 递归更新配置
                    self._update_config(self._config, file_config)
            except Exception as e:
                print(f"加载配置文件失败: {e}")
        
        self._initialized = True
    
    def _update_config(self, target: Dict[str, Any], source: Dict[str, Any]):
        """递归更新配置字典"""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._update_config(target[key], value)
            else:
                target[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项，支持点号分隔的路径"""
        parts = key.split('.')
        config = self._config
        
        for part in parts:
            if part not in config:
                return default
            config = config[part]
        
        return config
    
    def get_all(self) -> Dict[str, Any]:
        """获取所有配置"""
        return self._config.copy()