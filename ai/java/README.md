# 讯飞工作流API Java集成示例

## 概述

这个项目演示了如何使用Java调用讯飞星火工作流API。基于讯飞开放平台的官方文档和示例代码实现。

## API信息

- **接口地址**: https://xingchen-api.xf-yun.com/workflow/v1/chat/completions
- **API Key**: 2563e7415939bf27e627edc78f2ce83a
- **API Secret**: YWY3OTU0MjI0NjM5NzRiMjUwMDI5MjNj
- **Flow ID**: 7361279241469214722

## 项目结构

```
java/
└── workflow_openapi_demo_java.java/
    └── WorkflowRequest.java      # 主要的API调用示例
```

## 使用说明

### 1. 编译程序

```bash
javac workflow_openapi_demo_java.java/WorkflowRequest.java
```

### 2. 运行程序

```bash
java -cp workflow_openapi_demo_java.java WorkflowRequest
```

### 3. 输出示例

程序成功运行后会返回类似以下的JSON响应：

```json
{
  "code": 0,
  "message": "Success",
  "id": "spf0011b507@dx198d221e2e3a4f3782",
  "created": 1755872114,
  "choices": [{
    "delta": {
      "role": "assistant",
      "content": "\n文枢智创智能办公助手为您服务\n\n\n",
      "reasoning_content": ""
    },
    "index": 0,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 584,
    "completion_tokens": 307,
    "total_tokens": 891
  }
}
```

## 代码说明

### 主要功能

- 使用HTTPS连接讯飞API服务器
- 设置Bearer认证头（API Key + API Secret）
- 发送JSON格式的请求体
- 支持流式和非流式响应处理
- 设置合理的超时时间（120秒）

### 请求参数

- `flow_id`: 工作流ID
- `uid`: 用户ID（可选）
- `parameters`: 工作流输入参数
- `ext`: 扩展信息
- `stream`: 是否启用流式返回

## 注意事项

1. 确保网络可以访问讯飞API服务器
2. API Key和Secret需要保密，不要泄露
3. 可以根据需要修改请求参数和输入内容
4. 支持流式和非流式两种响应模式

## 参考文档

- [讯飞工作流API文档](https://www.xfyun.cn/doc/spark/Agent04-API%E6%8E%A5%E5%85%A5.html)
- 讯飞开放平台官方文档中心

## 许可证

MIT License