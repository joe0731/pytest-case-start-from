# pytest-start-from 使用说明

这个 pytest 插件允许你指定从某个测试用例开始执行，之前的测试用例都会被跳过。

## 安装

### 开发模式安装（本地使用）

```bash
pip install -e .
```

### 正常安装

```bash
pip install .
```

## 使用方法

### 基本用法

使用 `--start-from` 选项指定要开始执行的测试用例名称：

```bash
pytest --start-from test_third
```

### 匹配规则

匹配规则类似 pytest 的 `-k` 选项，支持子串匹配：

```bash
# 匹配包含 "third" 的第一个测试
pytest --start-from third

# 匹配包含 "class_second" 的第一个测试
pytest --start-from class_second

# 匹配类中的测试方法
pytest --start-from TestClass::test_class_second
```

### 支持的关键字

支持使用 `and`, `or`, `not` 关键字进行复杂匹配：

```bash
# 匹配包含 "parameters" 且包含 "a" 的测试
pytest --start-from "parameters and a"

# 匹配包含 "first" 或 "second" 的测试
pytest --start-from "first or second"

# 匹配包含 "test" 但不包含 "class" 的测试
pytest --start-from "test not class"
```

## 示例输出

### 正常执行（不使用插件）

```bash
$ pytest test_example.py -v
```

所有测试都会执行。

### 从 test_third 开始执行

```bash
$ pytest test_example.py --start-from test_third -v
```

输出示例：
```
test_example.py::test_first SKIPPED (Skipped: execution starts from 'test_third')
test_example.py::test_second SKIPPED (Skipped: execution starts from 'test_third')
test_example.py::test_third PASSED
test_example.py::test_fourth PASSED
test_example.py::test_fifth PASSED
...
```

### 从类方法开始执行

```bash
$ pytest test_example.py --start-from test_class_second -v
```

所有 `test_class_second` 之前的测试都会被跳过。

## 工作原理

1. 插件在每个测试执行前检查测试名称是否匹配指定的模式
2. 在找到第一个匹配的测试之前，所有测试都被标记为 SKIPPED
3. 从第一个匹配的测试开始，后续所有测试正常执行
4. 匹配算法支持：
   - 简单子串匹配
   - 完整的 nodeid 匹配（包含文件路径和类名）
   - 逻辑运算符：`and`, `or`, `not`

## 使用场景

- **调试特定测试**：跳过前面已经通过的测试，从失败的测试开始调试
- **增量测试**：在长时间运行的测试套件中，从中断的位置继续执行
- **开发过程**：开发新功能时，只运行相关的测试而不是全部测试
- **CI/CD 优化**：在某些场景下需要从特定测试点开始执行

## 注意事项

1. **测试独立性**：请确保你的测试用例是独立的，不依赖前面测试的状态
2. **Fixture 影响**：即使测试被跳过，session 级别的 fixture 仍会执行
3. **匹配顺序**：插件按照 pytest 收集测试的顺序进行匹配
4. **第一个匹配**：只有第一个匹配的测试会触发开始执行，后续即使有其他匹配也会执行

## 与 pytest -k 的区别

- `-k` 选项：只运行匹配的测试，不匹配的测试会被跳过或不收集
- `--start-from` 选项：从第一个匹配的测试开始，运行它和后续的所有测试

## 常见问题

### Q: 如果没有测试匹配会怎样？
A: 所有测试都会被跳过，因为插件永远等不到起始点。

### Q: 可以和其他 pytest 选项一起使用吗？
A: 可以！例如：
```bash
pytest --start-from test_third -v -s --tb=short
```

### Q: 如何查看插件是否正确加载？
A: 使用 pytest 的插件列表命令：
```bash
pytest --trace-config
```

## 贡献

欢迎提交 Issue 和 Pull Request！
