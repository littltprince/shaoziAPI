warning: LF will be replaced by CRLF in bin/result_report.html.
The file will have its original line endings in your working directory
[1mdiff --git a/.idea/misc.xml b/.idea/misc.xml[m
[1mindex e15fa13..bada80e 100644[m
[1m--- a/.idea/misc.xml[m
[1m+++ b/.idea/misc.xml[m
[36m@@ -3,5 +3,5 @@[m
   <component name="JavaScriptSettings">[m
     <option name="languageLevel" value="ES6" />[m
   </component>[m
[31m-  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.7 (shaoziketang)" project-jdk-type="Python SDK" />[m
[32m+[m[32m  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.7 (python-master)" project-jdk-type="Python SDK" />[m
 </project>[m
\ No newline at end of file[m
[1mdiff --git a/.idea/shaoziketang.iml b/.idea/shaoziketang.iml[m
[1mindex 85c7612..330357c 100644[m
[1m--- a/.idea/shaoziketang.iml[m
[1m+++ b/.idea/shaoziketang.iml[m
[36m@@ -4,7 +4,7 @@[m
     <content url="file://$MODULE_DIR$">[m
       <excludeFolder url="file://$MODULE_DIR$/venv" />[m
     </content>[m
[31m-    <orderEntry type="inheritedJdk" />[m
[32m+[m[32m    <orderEntry type="jdk" jdkName="Python 3.7 (python-master)" jdkType="Python SDK" />[m
     <orderEntry type="sourceFolder" forTests="false" />[m
   </component>[m
   <component name="TestRunnerService">[m
[1mdiff --git a/.idea/workspace.xml b/.idea/workspace.xml[m
[1mindex 1a5c54e..d2f9433 100644[m
[1m--- a/.idea/workspace.xml[m
[1m+++ b/.idea/workspace.xml[m
[36m@@ -2,361 +2,11 @@[m
 <project version="4">[m
   <component name="ChangeListManager">[m
     <list default="true" id="787b1a72-d645-42a9-9ab0-55e7feeb22a7" name="Default Changelist" comment="">[m
[31m-      <change afterPath="$PROJECT_DIR$/.idea/misc.xml" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/.idea/modules.xml" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/.idea/shaoziketang.iml" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/.idea/vcs.xml" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/.idea/workspace.xml" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/bin/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/bin/run.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/configs/OP_config.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/configs/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/configs/test_case.config" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/data/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/data/ddt_data.xlsx" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/method/HttpResquest.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/method/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/method/htmltestrunner.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/method/operationpyxl.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/testcase/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/testcase/test_ddt.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/testcase/test_login.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/testcase/test_wechat.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/utils/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/easy-install.pth" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/PKG-INFO" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/SOURCES.txt" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/dependency_links.txt" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/entry_points.txt" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/not-zip-safe" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO/top_level.txt" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/__main__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/build_env.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cache.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/autocompletion.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/base_command.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/cmdoptions.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/main_parser.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/parser.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/cli/status_codes.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/__init__.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/check.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/completion.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/configuration.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/download.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/freeze.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/hash.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/help.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/install.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/list.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/search.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/show.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3.7.egg/pip/_internal/commands/uninstall.py" afterDir="false" />[m
[31m-      <change afterPath="$PROJECT_DIR$/venv/Lib/site-packages/pip-19.0.3-py3