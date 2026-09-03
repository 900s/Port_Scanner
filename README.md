# 🔍 SysScan - 轻量级TCP端口扫描器

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 简介

SysScan 是一个基于 Python Socket 的轻量级 TCP 端口扫描工具，用于快速检测目标主机端口的开放状态。适合网络安全学习、渗透测试辅助、网络运维巡检等场景。

**项目特点：**
- 纯 Python 标准库实现，无需安装第三方依赖
- 命令行交互，简单易用
- 代码结构清晰，适合初学者学习 Socket 编程和端口扫描原理

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| ✅ 默认端口扫描 | 一键扫描 19 个常见服务端口（FTP、SSH、HTTP、MySQL、Redis 等） |
| ✅ 自定义端口列表 | 指定多个特定端口进行扫描，如 `80,443,8080` |
| ✅ 自定义端口范围 | 扫描连续端口区间，如 `81-85` |
| ✅ IP 地址校验 | 自动验证 IPv4 地址格式是否正确 |
| ✅ 端口合法性校验 | 自动检查端口号是否在 0-65535 有效范围内 |
| ✅ 帮助与版本 | 支持 `-h` 查看帮助，`-v` 查看版本号 |

---

## 🚀 快速开始

### 环境要求

- Python 3.6 及以上版本
- 无需额外安装依赖包

### 下载与运行

```bash
# 1. 克隆仓库（或直接下载 sys_scan.py 文件）
git clone https://github.com/yourusername/SysScan.git
cd SysScan

# 2. 运行扫描（控制台输入）
python sys_scan.py 192.168.1.1
```

### 使用示例

```bash
# 1. 扫描默认端口
python sys_scan.py 127.0.0.1

# 2. 扫描指定端口列表（逗号分隔）
python sys_scan.py 127.0.0.1 80,443,8080

# 3. 扫描指定端口范围（起始-结束）
python sys_scan.py 127.0.0.1 81-85

# 4. 查看帮助信息
python sys_scan.py -h

# 5. 查看版本号
python sys_scan.py -v
```

### 输出示例

```
主机 127.0.0.1 的端口 80 open
主机 127.0.0.1 的端口 443 close
主机 127.0.0.1 的端口 8080 open
```

## 🛠️ 核心方法说明

| 方法 | 功能描述 |
|------|----------|
| `is_open(ip, port)` | 尝试 TCP 连接指定端口，返回 True/False |
| `scan(ip, portlist)` | 扫描给定的端口列表 |
| `cscan(ip, *args)` | 扫描可变数量的指定端口 |
| `rscan(ip, s, d)` | 扫描从 s 到 d 的端口范围 |
| `is_valid_ip(ip)` | 校验 IPv4 地址格式 |
| `is_valid_port(port_range)` | 校验端口号是否在有效范围内 |

---

## ⚠️ 注意事项

1. **使用场景**：本工具仅供学习交流和合法授权下的网络检测使用，请勿用于非法入侵。
2. **扫描速度**：当前为单线程扫描，默认超时 0.5 秒，扫描大量端口时耗时较长，建议仅扫描重点关注端口。
3. **防火墙影响**：部分主机可能启用防火墙或 ICMP 过滤，导致扫描结果不准确。
4. **权限要求**：扫描 1024 以下的特权端口在部分操作系统上可能需要管理员/root 权限。

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议，允许自由使用、修改和分发。

---

## 🙏 致谢

- Python Socket 编程官方文档
- 网络安全爱好者社区的学习资源
