"use client"; // 声明这是一个客户端组件，启用客户端交互功能

import { useState, useRef, useTransition } from "react";

// 智能助手测试页面组件
export default function AssistantTestPage() {
  // 添加这行测试代码
  console.log("API URL:", process.env.NEXT_PUBLIC_API_BASE_URL);
  
  // 状态管理
  const [question, setQuestion] = useState(""); // 用户输入的问题
  const [answer, setAnswer] = useState<string | null>(null); // 服务器返回的答案
  const [error, setError] = useState<string | null>(null); // 错误信息
  const [isPending, startTransition] = useTransition(); // 用于处理异步状态转换的钩子
  const inputRef = useRef<HTMLInputElement>(null); // 输入框的引用，用于DOM操作

  // 表单提交处理函数
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // 阻止表单默认提交行为
    setError(null); // 清除之前的错误信息
    setAnswer(null); // 清除之前的答案
    
    // 输入验证
    if (!question.trim()) {
      setError("请输入问题");
      return;
    }
    
    // 使用startTransition包装异步操作，提供更好的用户体验
    startTransition(async () => {
      try {
        // 发送POST请求到后端API
        const resp = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/ask`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question }),
        });
        
        // 检查响应状态
        if (!resp.ok) {
          throw new Error(`HTTP ${resp.status}`);
        }
        
        // 解析并设置响应数据
        const data = await resp.json();
        setAnswer(data.answer ?? JSON.stringify(data));
      } catch (err: any) {
        console.error("详细错误:", err);
        setError(err?.message || "请求失败");
      }
    });
  };

  // 页面UI渲染
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-white dark:bg-black px-4">
      <h1 className="text-2xl font-bold mb-6">智能助手测试页</h1>
      
      {/* 问题输入表单 */}
      <form
        className="flex flex-col items-center gap-4 w-full max-w-md"
        onSubmit={handleSubmit}
      >
        <input
          ref={inputRef}
          className="w-full border rounded px-3 py-2 text-base"
          type="text"
          placeholder="请输入你的问题"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          disabled={isPending}
          autoFocus
        />
        <button
          className="w-full bg-blue-600 text-white rounded px-3 py-2 font-semibold disabled:opacity-60"
          type="submit"
          disabled={isPending}
        >
          {isPending ? "提交中..." : "提交"}
        </button>
      </form>

      {/* 答案和错误信息显示区域 */}
      <div className="mt-6 w-full max-w-md min-h-[48px]">
        {error && (
          <div className="text-red-600 text-sm mb-2" role="alert">
            {error}
          </div>
        )}
        {answer && (
          <div className="bg-gray-100 dark:bg-gray-800 rounded p-4 whitespace-pre-wrap break-words">
            {answer}
          </div>
        )}
      </div>
    </div>
  );
}
