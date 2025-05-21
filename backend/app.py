"""
Andy AI 助手后端入口
Flask API服务，处理前端请求
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import logging
from core.orchestrator import Orchestrator
from config.config import Config

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("andy.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("andy")

# 初始化Flask应用
app = Flask(__name__)
CORS(app)  # 启用跨域支持

# 加载配置
config = Config()

# 初始化Orchestrator
orchestrator = Orchestrator()

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({"status": "ok", "version": config.get("app.version")})

@app.route('/ask', methods=['POST'])
def ask():
    """处理用户问题的主接口"""
    try:
        # 获取请求数据
        data = request.json
        if not data or 'input' not in data:
            return jsonify({"error": "缺少必要参数"}), 400
        
        user_input = data['input']
        context = data.get('context', {})
        
        # 记录请求
        logger.info(f"收到请求: {user_input}")
        
        # 处理用户输入
        result = orchestrator.process_input(user_input, context)
        
        # 返回结果
        return jsonify(result)
    
    except Exception as e:
        # 错误处理
        error_message = f"处理请求时出错: {str(e)}"
        logger.error(f"{error_message}\n{traceback.format_exc()}")
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    # 注册默认技能
    logger.info("正在启动Andy AI助手后端...")
    
    # 启动Flask应用
    app.run(
        host=config.get("app.host"),
        port=config.get("app.port"),
        debug=config.get("app.debug")
    )
