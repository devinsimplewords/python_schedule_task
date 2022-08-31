# python_schedule_task
In this repository there are two python files to show you how the [schedule package](https://schedule.readthedocs.io/en/stable/index.html) works.  
If you are interested in more details, please check [this post](https://devinsimplewords.com/python-schedule/) on [devinsimplewords blog](https://devinsimplewords.com/)! 

The first file, `schedule_task.py`, shows you how to schedule a task every 20 seconds/minute and other combinations.  
The second file instead (schedule_task_with_decorators.py), shows you how to schedule the same tasks but using decorators.

Steps to run the script:
- prepare a virtualenv and install what it is present in requirements.txt file using the following command:
  ```
  pip install -r requirements.txt
  ```
  If you don't know how to create and activate a virtualenv, please check [this post](https://devinsimplewords.com/python-virtual-environment/)
- Run the script using the following command:
  ```commandline
  python schedule_task.py
  ```
  or
  ```commandline
  python schedule_task_with_decorators.py
  ```
 
