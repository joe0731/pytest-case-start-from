# 快速开始指南

## 安装

```bash
pip install -e .
```

## 基本使用

### 1. 从指定测试开始执行

```bash
pytest --start-from test_third
```

这将跳过 `test_third` 之前的所有测试，从 `test_third` 开始执行。

### 2. 使用模式匹配

```bash
# 匹配包含 "third" 的第一个测试
pytest --start-from "third"

# 匹配类中的方法
pytest --start-from "test_class_second"

# 匹配特定参数的测试
pytest --start-from "parameters"
```

### 3. 使用逻辑运算符

```bash
# AND 运算符：匹配同时包含两个关键词的测试
pytest --start-from "parameters and a"

# OR 运算符：匹配包含任一关键词的测试
pytest --start-from "first or second"

# NOT 运算符：匹配包含第一个但不包含第二个关键词的测试
pytest --start-from "test not class"
```

## 示例

使用项目中的 `test_example.py` 进行测试：

```bash
# 正常执行所有测试
pytest test_example.py -v

# 从 test_third 开始执行
pytest test_example.py --start-from test_third -v

# 从类中的第二个方法开始执行
pytest test_example.py --start-from test_class_second -v

# 使用复杂模式
pytest test_example.py --start-from "parameters and a" -v
```

## 验证安装

检查插件是否正确加载：

```bash
pytest --help | grep start-from
```

应该看到：
```
  --start-from=START_FROM
                        Start test execution from the first test matching this
                        pattern (similar to -k). All tests before the matched
                        test will be skipped. Supports substring matching and
                        keywords: and, or, not
```

## 运行演示

运行包含的演示脚本查看完整示例：

```bash
./demo.sh
```

## 运行单元测试

验证插件功能：

```bash
pytest test_plugin.py -v
```

## 更多信息

详细使用说明请参考 [USAGE.md](USAGE.md)
