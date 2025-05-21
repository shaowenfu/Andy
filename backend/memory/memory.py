"""
Memory 模块 - 记忆与知识层
负责管理对话历史、用户画像、知识库等
"""
import json
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
import sqlite3

class Memory:
    def __init__(self, db_path: str = "memory.db"):
        """
        初始化记忆模块
        
        Args:
            db_path: SQLite数据库路径
        """
        self.db_path = db_path
        self._init_db()
        # 短期记忆（当前对话）
        self.current_conversation = []
        # 最大对话轮次（可配置）
        self.max_conversation_turns = 10
        
    def _init_db(self):
        """初始化SQLite数据库，创建必要的表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 创建对话历史表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT DEFAULT 'default_user',
            timestamp TEXT,
            user_input TEXT,
            assistant_response TEXT
        )
        ''')
        
        # 创建用户画像表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profile (
            user_id TEXT PRIMARY KEY,
            profile_data TEXT,
            last_updated TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_conversation_context(self) -> Dict[str, Any]:
        """获取当前对话上下文"""
        return {
            "conversation_history": self.current_conversation,
            "timestamp": datetime.now().isoformat()
        }
    
    def update_conversation(self, user_input: str, assistant_response: str, user_id: str = "default_user"):
        """
        更新对话历史
        
        Args:
            user_input: 用户输入
            assistant_response: 助手回复
            user_id: 用户ID
        """
        # 更新短期记忆（当前对话）
        conversation_turn = {
            "user": user_input,
            "assistant": assistant_response,
            "timestamp": datetime.now().isoformat()
        }
        self.current_conversation.append(conversation_turn)
        
        # 限制对话长度，保留最近的N轮对话
        if len(self.current_conversation) > self.max_conversation_turns:
            self.current_conversation = self.current_conversation[-self.max_conversation_turns:]
        
        # 更新长期记忆（数据库）
        self._save_to_db(user_input, assistant_response, user_id)
    
    def _save_to_db(self, user_input: str, assistant_response: str, user_id: str):
        """保存对话到SQLite数据库"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        timestamp = datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO conversation_history (user_id, timestamp, user_input, assistant_response) VALUES (?, ?, ?, ?)",
            (user_id, timestamp, user_input, assistant_response)
        )
        
        conn.commit()
        conn.close()
    
    def get_conversation_history(self, user_id: str = "default_user", limit: int = 10) -> List[Dict[str, Any]]:
        """
        获取历史对话记录
        
        Args:
            user_id: 用户ID
            limit: 返回的最大记录数
            
        Returns:
            对话历史列表
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT timestamp, user_input, assistant_response FROM conversation_history WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, limit)
        )
        
        history = []
        for row in cursor.fetchall():
            history.append({
                "timestamp": row[0],
                "user": row[1],
                "assistant": row[2]
            })
        
        conn.close()
        return history[::-1]  # 返回时间正序
