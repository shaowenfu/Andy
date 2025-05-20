"""
SkillRegistry（技能注册表）：
负责注册、查找和管理所有技能模块。
"""
class SkillRegistry:
    def __init__(self):
        self._skills = {}

    def register_skill(self, name: str, skill):
        """
        注册一个技能模块
        :param name: 技能名称（唯一标识）
        :param skill: 技能实例（需实现统一接口）
        """
        self._skills[name] = skill

    def get_skill(self, name: str):
        """
        获取指定名称的技能模块
        :param name: 技能名称
        :return: 技能实例或None
        """
        return self._skills.get(name)
