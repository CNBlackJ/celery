## Celery + Redis 基本示例

* app.py #配置
* tasks.py #任务
* 运行：
 * 安装了redis
 * 安装了Celery
 * celery worker -A tasks -l info -c 5
