"""
Memory（记忆与数据层）：
负责对话上下文、短期记忆等管理。
当前为骨架，后续可扩展实现。
"""
class Memory:
    def __init__(self):
        # 初始化记忆存储结构
        self.context = {}

    def get_context(self, user_id: str):
        """
        获取指定用户的对话上下文
        """
        return self.context.get(user_id, {})

    def update_context(self, user_id: str, new_context: dict):
        """
        更新指定用户的对话上下文
        """
        self.context[user_id] = new_context
