"""
BaseSkill（技能基类）：
所有技能模块需继承本类，实现execute方法。
"""
from abc import ABC, abstractmethod

class BaseSkill(ABC):
    @abstractmethod
    def execute(self, user_input: str) -> str:
        """
        执行技能主逻辑
        :param user_input: 用户输入
        :return: 技能返回结果
        """
        pass
