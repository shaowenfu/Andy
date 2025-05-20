# Andy AI 助手项目

> 养成式AI助手 —— 分层、模块化、可扩展的智能助手系统

---

## 项目简介

Andy 是一个集成了大语言模型（LLM）、RAG（检索增强生成）、MCP（模型上下文协议）等前沿技术的个人 AI 助手。项目采用前后端分离的 C/S 架构，后端以 Python + Flask 实现智能核心，前端以 Next.js 构建极简交互界面。系统强调分层、模块化、可插拔的能力扩展，支持多种记忆机制，致力于打造可持续成长、易于维护和扩展的智能体。

---

## 目录结构

```
Andy/
├── backend/                # 后端服务（Flask，智能核心、技能、记忆等）
│   ├── app.py              # Flask 应用入口
│   ├── requirements.txt    # 后端依赖
│   ├── assistant_backend_guide.md # 后端开发指南
│   ├── code_log.md         # 后端开发日志
│   ├── core/               # 核心逻辑（编排、路由等）
│   │   ├── orchestrator.py
│   │   └── skill_registry.py
│   ├── skills/             # 能力模块（技能插件）
│   │   ├── base.py
│   │   └── llm_skill.py
│   └── memory/             # 记忆与知识层
│       └── memory.py
├── frontend/               # 前端应用（Next.js，极简交互界面）
│   ├── src/app/            # 页面与全局样式
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── public/             # 静态资源
│   ├── package.json        # 前端依赖
│   └── assistant_frontend_log.md # 前端开发日志
├── README.md               # 项目说明文档
├── 编码指南.md             # 编码与架构设计指南
└── ...
```

---

## 核心特性

- **分层架构**：感知与交互层、认知与决策层、能力与执行层、记忆与知识层，灵感来源于人类认知系统。
- **模块化与可插拔**：每个技能（Skill）为独立模块，标准化接口，便于扩展和维护。
- **多重记忆机制**：短期对话上下文、长期用户画像、交互历史、知识库，支持 SQLite 和 Pinecone 向量数据库。
- **前后端分离**：后端专注智能逻辑，前端专注用户体验。
- **持续成长与反思**：每次功能迭代后反思设计，优化架构，便于长期演进。
- **详细注释与文档**：关键代码配有中文注释，文档持续更新，方便快速上手。

---

## 技术栈

- **后端**：Python 3.x, Flask, SQLite, Pinecone（向量数据库）
- **前端**：Next.js, TypeScript, React
- **开发环境**：WSL2 (Ubuntu), VSCode
- **部署**：Docker（后端容器化）、静态网站托管（前端）

---

## 快速开始

### 1. 环境准备
- 安装 Python 3.x、Node.js、Docker、VSCode

### 2. 后端启动

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. 前端启动

```bash
cd frontend
npm install
npm run dev
```

### 4. 访问

- 前端默认运行在 [http://localhost:3000](http://localhost:3000)
- 后端 API 默认运行在 [http://localhost:5000](http://localhost:5000)

### 5. 部署

- 后端可用 Docker 容器化部署到云服务器
- 前端可部署到静态网站托管平台

---

## 贡献指南

- 阅读 `编码指南.md` 和各模块下的开发日志，了解架构理念与开发规范
- 新增技能模块请遵循统一接口，保持低耦合、可插拔
- 关键代码需添加详细中文注释，便于后续维护
- 每次功能迭代后，及时更新文档和日志
- 有疑问或新想法，欢迎在开发日志中记录并讨论

---

## 未来规划

- 持续丰富技能模块（如日程管理、邮件、更多 API 集成等）
- 优化记忆与知识管理机制
- 支持多用户与权限管理
- 云端自动化部署与监控
- 持续完善开发文档和编码规范

---

## 参考与致谢

- [Flask 官方文档](https://flask.palletsprojects.com/)
- [Next.js 官方文档](https://nextjs.org/)
- [Pinecone 向量数据库](https://www.pinecone.io/)
- [OpenAI API](https://platform.openai.com/)
- 以及所有开源社区贡献者

---

## 联系方式

如有问题或建议，欢迎提交 Issue 或联系项目维护者。

---

> 本项目秉持“成长、反思、持续进化”的理念，欢迎更多开发者参与共建，让 AI 助手真正成为你的得力伙伴！
