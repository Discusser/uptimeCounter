# uptimeCounter
Simple python script to track your uptime on your computer and display it as a graph.

![image](https://user-images.githubusercontent.com/47938380/179482456-e7ad8ec8-f130-4a51-8bb8-fcbe2cfdf885.png)


# How to use (WINDOWS)
Put the three python scripts in a single directory and make sure you have installed matplotlib (to install it, run `pip install matplotlib` in a terminal)
Open `Task Scheduler`, navigate to `Task Scheduler (Local) > Task Scheduler Library`, and right click on `Task Scheduler Library`. Click on `Create Task`
Change the group from your user to `SYSTEM`

![image](https://user-images.githubusercontent.com/47938380/179463634-8f3562db-d959-4233-b836-be37decbcd82.png)

Next, go to the `Triggers` tab, click on `New`, and choose `At startup`

![image](https://user-images.githubusercontent.com/47938380/179463792-a3127eb4-9afa-447c-93c2-aa0abb04a870.png)

Now you want to go to the `Actions` tab, click on `New`, and fill out the boxes like so:

![image](https://user-images.githubusercontent.com/47938380/179463940-d29eeb15-509c-49e6-bd3d-f1ec86f15b86.png)

Finally to avoid any issues, uncheck everything in the `Conditions` tab.
Next, do the same thing, but by replacing `uptimeCounterStart.bat` with `uptimeCounterEnd.bat`, and changing the trigger to this:

![image](https://user-images.githubusercontent.com/47938380/179464291-32f0aa3d-a8f1-4bc3-b677-5486b9f35886.png)


The last step is to create your batch scripts that will run your python scripts.
`uptimeCounterStart.bat` should look like this:
```
D:
cd D:\path\to\dir
py D:\path\to\dir\start.pyw
```
and `uptimeCounterEnd.bat` should look like this:
```
D:
cd D:\path\to\dir
py D:\path\to\dir\end.pyw
```

Once you've done all that, it should work. To make sure it's working, restart your PC and check for a file called `data.txt`
