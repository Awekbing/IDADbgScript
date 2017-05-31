"# IDADbgScript" 

启动调试需要打开4个CMD窗口至少
1-启动android_server
2-转发端口
3-启动jdb
4-am start启动app  

不小心过了断点，好麻烦 所以
FirstDbg.py 是用来首次启动的  打开修改package startActivity 2个参数
StartDbg.py 是用来第二次启动的（不小心过了断点）