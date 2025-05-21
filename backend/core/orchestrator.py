"""
Orchestrator 模块 - 认知与决策层核心组件
负责协调各个技能模块，管理对话流程，分发任务
"""
from typing import Dict, Any, List, Optional
from .skill_registry import SkillRegistry
from ..memory.memory import Memory

class Orchestrator:
    def __init__(self):
        self.skill_registry = SkillRegistry()
        self.memory = Memory()
        
    def process_input(self, user_input: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        处理用户输入，协调技能调用，管理对话流程
        
        Args:
            user_input: 用户输入文本
            context: 上下文信息（可选）
            
        Returns:
            包含响应内容和元数据的字典
        """
        # 1. 更新对话上下文
        conversation_context = self.memory.get_conversation_context()
        if context:
            conversation_context.update(context)
        
        # 2. 意图识别（简化版，后续可扩展为更复杂的NLU）
        intent = self._identify_intent(user_input, conversation_context)
        
        # 3. 技能选择与调用
        skill = self.skill_registry.get_skill(intent["skill_name"])
        if not skill:
            # 默认使用LLM技能
            skill = self.skill_registry.get_skill("llm_skill")
        
        # 4. 执行技能并获取结果
        result = skill.execute(user_input, conversation_context)
        
        # 5. 更新记忆
        self.memory.update_conversation(user_input, result["response"])
        
        return result
    
    def _identify_intent(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        简单的意图识别，确定应该使用哪个技能
        
        后续可扩展为更复杂的NLU系统或使用LLM进行意图分类
        """
        # 简化版意图识别，基于关键词匹配
        # 实际项目中可以使用更复杂的NLU或LLM分类
        intent = {"skill_name": "llm_skill", "confidence": 1.0}
        
        # 示例：简单关键词匹配
        if "计算" in user_input or "等于多少" in user_input:
            intent["skill_name"] = "calculator_skill"
        elif "搜索" in user_input or "查找" in user_input:
            intent["skill_name"] = "search_skill"
            
        return intent
