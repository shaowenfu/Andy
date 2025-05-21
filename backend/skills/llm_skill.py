"""
LLM_Skill 模块 - 大语言模型问答技能
"""
from typing import Dict, Any, Optional
import openai
from .base import BaseSkill
from ..config.config import Config

class LLMSkill(BaseSkill):
    """大语言模型问答技能，对接OpenAI API"""
    
    def __init__(self):
        super().__init__("llm_skill", "大语言模型问答")
        self.config = Config()
        # 设置OpenAI API密钥
        openai.api_key = self.config.get("llm.api_key")
        # 默认模型参数
        self.model = self.config.get("llm.model")
        self.temperature = self.config.get("llm.temperature")
        self.max_tokens = self.config.get("llm.max_tokens")
    
    def execute(self, user_input: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        执行LLM问答
        
        Args:
            user_input: 用户输入
            context: 上下文信息
            
        Returns:
            包含响应内容和元数据的字典
        """
        try:
            # 构建对话历史
            messages = self._build_messages(user_input, context)
            
            # 调用OpenAI API
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 提取回复内容
            assistant_response = response.choices[0].message.content
            
            return {
                "response": assistant_response,
                "skill": self.name,
                "metadata": {
                    "model": self.model,
                    "usage": response.usage._asdict() if hasattr(response, "usage") else {}
                }
            }
        except Exception as e:
            # 错误处理
            error_message = f"LLM调用出错: {str(e)}"
            print(error_message)  # 后续可替换为日志
            
            return {
                "response": f"抱歉，我遇到了一些问题: {error_message}",
                "skill": self.name,
                "error": str(e)
            }
    
    def _build_messages(self, user_input: str, context: Optional[Dict[str, Any]]) -> list:
        """构建发送给OpenAI的消息列表"""
        messages = [
            {"role": "system", "content": "你是Andy，一个智能AI助手。你的回答应该简洁、有帮助且友好。"}
        ]
        
        # 添加对话历史
        if context and "conversation_history" in context:
            for turn in context["conversation_history"]:
                if "user" in turn:
                    messages.append({"role": "user", "content": turn["user"]})
                if "assistant" in turn:
                    messages.append({"role": "assistant", "content": turn["assistant"]})
        
        # 添加当前用户输入
        messages.append({"role": "user", "content": user_input})
        
        return messages
