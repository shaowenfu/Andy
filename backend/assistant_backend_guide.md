# 智能助手后端开发指南

## 1. 项目架构概览

本项目采用分层与模块化思想，参考人类认知与行为系统，分为：
- **感知与交互层**（前端，Next.js，暂未实现）
- **认知与决策层**（Orchestrator，意图识别、对话管理、任务调度）
- **能力与执行层**（Skill，技能模块，标准化接口，易扩展）
- **记忆与知识层**（Memory，短期/长期记忆，数据存储）

## 2. 目录结构与主要文件

```
backend/
  app.py                # Flask入口，API路由
  requirements.txt      # 依赖管理
  core/
    orchestrator.py     # 认知与决策主控
    skill_registry.py   # 技能注册表
  skills/
    base.py             # 技能基类
    llm_skill.py        # LLM技能（大模型问答）
  memory/
    memory.py           # 记忆与上下文管理
  config/               # 配置文件（预留）
assistant_backend_guide.md # 本开发指南
```

## 3. 技能注册与扩展机制

- **SkillRegistry** 负责注册、查找所有技能模块。
- **BaseSkill** 为所有技能定义统一接口（execute方法）。
- 新增技能只需继承BaseSkill并注册到SkillRegistry，低耦合高扩展。

## 4. 当前开发进度

- [x] 分层目录结构与核心骨架搭建
- [x] 技能注册表与基类实现
- [x] LLM_Skill（大模型问答，mock版）实现
- [x] Flask API（/ask）可接收用户输入并返回LLM_Skill结果
- [x] 记忆层Memory骨架预留
- [x] requirements.txt与本开发指南

## 5. API请求示例

### 5.1 curl命令

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"input": "你好，帮我查下明天天气"}'
```

### 5.2 Python requests示例

```python
import requests

url = "http://localhost:8000/ask"
data = {"input": "你好，帮我查下明天天气"}
response = requests.post(url, json=data)
print(response.json())
```

### 5.3 请求体说明

- URL: `POST /ask`
- Content-Type: `application/json`
- Body参数:
  - `input` (string): 用户输入内容

### 5.4 返回示例

```json
{
  "result": "你说：你好，帮我查下明天天气，这是大模型的回复示例。"
}
```

## 6. 未来完善方向

- [ ] LLM_Skill对接真实大模型API（如OpenAI、Qwen等）
- [ ] 实现对话管理器、意图识别、任务调度等认知层功能
- [ ] 能力层扩展：WebSearch_Skill、Calculator_Skill、Notes_Skill等
- [ ] 记忆层完善：短期/长期记忆、用户画像、知识库、向量数据库集成
- [ ] 配置与密钥管理
- [ ] 完善异常处理与日志
- [ ] 单元测试与模块化开发
- [ ] 前端Next.js极简界面开发
- [ ] 容器化部署与云端上线

---

**迭代建议：**
每完成一小步，反思设计是否易扩展、代码是否清晰，及时记录问题与TODO，保持架构灵活性。
