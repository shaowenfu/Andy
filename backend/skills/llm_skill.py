"""
LLMSkill（大模型技能模块）：
封装与大模型API的交互，当前为mock实现。
"""
from skills.base import BaseSkill

class LLMSkill(BaseSkill):
    def execute(self, user_input: str) -> str:
        """
        模拟调用大模型API，返回问答结果。
        后续可接入OpenAI、Qwen等API。
        """
        # TODO: 接入真实大模型API
        return f"你说：{user_input}，这是大模型的回复示例。"
