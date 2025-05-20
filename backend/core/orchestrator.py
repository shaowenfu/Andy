"""
Orchestrator（认知与决策层主控）：
负责理解用户输入、意图识别、调用技能模块。
初版只实现简单的LLM问答分发。
"""
from core.skill_registry import SkillRegistry

class Orchestrator:
    def __init__(self):
        self.skill_registry = SkillRegistry()
        # 注册基础技能
        from skills.llm_skill import LLMSkill
        self.skill_registry.register_skill('llm', LLMSkill())

    def handle_input(self, user_input: str) -> str:
        """
        处理用户输入，分发到合适的技能模块。
        初版：全部转发给llm技能。
        """
        llm_skill = self.skill_registry.get_skill('llm')
        if llm_skill:
            return llm_skill.execute(user_input)
        return "未找到合适的技能处理该请求。"
