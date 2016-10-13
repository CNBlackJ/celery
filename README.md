## Celery + Redis 基本示例

* app.py #配置
* tasks.py #任务
* 运行：
 * 安装redis => brew install redis
 * 安装Celery => pip install Celery
 * 安装Flower => pip install flower
 * 启动celery => celery worker -A tasks -l info -c 5
 * 启动Flower监视Redis => celery flower --broker=redis://localhost:6379/0
 * 运行python程序
 ```
from tasks import add
[add.delay(1,a) for a in range(1,5000)]
 ```
