# symcopy
A python module for allowing one directory to be copied into another via symbolic links.

Before
```
PS D:\> dir 'C:\Program Files (x86)\'


    Directory: C:\Program Files (x86)


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        12/2/2017   9:09 PM                Common Files
d-----        12/2/2017   8:13 PM                Internet Explorer
d-----        9/29/2017   9:46 AM                Microsoft.NET
d-----        12/2/2017   8:10 PM                MSBuild
d-----        12/3/2017  12:14 PM                NVIDIA Corporation
d-----        12/2/2017   8:10 PM                Reference Assemblies
d-----        12/3/2017  12:13 PM                VulkanRT
d-----        9/29/2017  10:41 AM                Windows Defender
d-----        9/29/2017   9:46 AM                Windows Mail
d-----        9/29/2017  10:42 AM                Windows Media Player
d-----        9/29/2017   9:46 AM                Windows Multimedia Platform
d-----        9/29/2017   9:46 AM                windows nt
d-----        9/29/2017  10:41 AM                Windows Photo Viewer
d-----        9/29/2017   9:46 AM                Windows Portable Devices
d-----        9/29/2017   9:46 AM                WindowsPowerShell


PS D:\> dir 'D:\InstalledSoftware\Program Files (x86)\'


    Directory: D:\InstalledSoftware\Program Files (x86)


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/30/2017  12:13 PM                Android
d-----       11/30/2017  12:17 PM                Application Verifier
d-----       11/30/2017  12:17 PM                Battle.net
d-----       11/30/2017  12:17 PM                Common Files
d-----       11/30/2017  12:17 PM                Entity Framework Tools
d-----       11/30/2017  12:17 PM                Google
d-----       11/30/2017  12:17 PM                GtkSharp
d-----       11/30/2017  12:17 PM                GUMFF27.tmp
d-----       11/30/2017  12:17 PM                Hearthstone
d-----       11/30/2017  12:17 PM                IIS
d-----       11/30/2017  12:17 PM                IIS Express
d-----       11/30/2017  12:17 PM                Intel
d-----       11/30/2017  12:17 PM                Internet Explorer
d-----       11/30/2017  12:17 PM                Java
d-----       11/30/2017  12:21 PM                Microsoft SDKs
d-----       11/30/2017  12:21 PM                Microsoft SQL Server
d-----       11/30/2017  12:28 PM                Microsoft Visual Studio
d-----       11/30/2017  12:28 PM                Microsoft Visual Studio Tools for Unity
d-----       11/30/2017  12:29 PM                Microsoft Web Tools
d-----       11/30/2017  12:29 PM                Microsoft.NET
d-----       11/30/2017  12:29 PM                Mozilla Maintenance Service
d-----        12/2/2017   2:05 AM                Mozilla Thunderbird
d-----       11/30/2017  12:29 PM                MSBuild
d-----       11/30/2017  12:29 PM                NuGet
d-----       11/30/2017  12:29 PM                NVIDIA Corporation
d-----       11/30/2017  12:29 PM                Reference Assemblies
d-----        12/2/2017   4:44 AM                StarCraft II
d-----        12/2/2017   5:34 PM                Steam
d-----       11/30/2017  12:35 PM                VulkanRT
d-----       11/30/2017  12:35 PM                Windows Defender
d-----       11/30/2017  12:36 PM                Windows Kits
d-----       11/30/2017  12:36 PM                Windows Mail
d-----       11/30/2017  12:36 PM                Windows Media Player
d-----       11/30/2017  12:36 PM                Windows Multimedia Platform
d-----       11/30/2017  12:36 PM                Windows NT
d-----       11/30/2017  12:36 PM                Windows Phone Kits
d-----       11/30/2017  12:36 PM                Windows Photo Viewer
d-----       11/30/2017  12:36 PM                Windows Portable Devices
d-----       11/30/2017  12:36 PM                WindowsPowerShell
d-----        12/2/2017   4:45 AM                World of Warcraft
d-----       11/30/2017  12:41 PM                Xamarin
```

`python -c "__import__('symcopy').symcopy(r'C:\Program Files (x86)', r'D:\InstalledSoftware\Program Files (x86)')"`

```
PS D:\> dir 'C:\Program Files (x86)\'


    Directory: C:\Program Files (x86)


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d----l        12/3/2017   2:10 PM                Android
d----l        12/3/2017   2:10 PM                Application Verifier
d----l        12/3/2017   2:10 PM                Battle.net
d-----        12/2/2017   9:09 PM                Common Files
d----l        12/3/2017   2:10 PM                Entity Framework Tools
d----l        12/3/2017   2:10 PM                Google
d----l        12/3/2017   2:10 PM                GtkSharp
d----l        12/3/2017   2:10 PM                GUMFF27.tmp
d----l        12/3/2017   2:10 PM                Hearthstone
d----l        12/3/2017   2:10 PM                IIS
d----l        12/3/2017   2:10 PM                IIS Express
d----l        12/3/2017   2:10 PM                Intel
d-----        12/2/2017   8:13 PM                Internet Explorer
d----l        12/3/2017   2:10 PM                Java
d----l        12/3/2017   2:10 PM                Microsoft SDKs
d----l        12/3/2017   2:10 PM                Microsoft SQL Server
d----l        12/3/2017   2:10 PM                Microsoft Visual Studio
d----l        12/3/2017   2:10 PM                Microsoft Visual Studio Tools for Unity
d----l        12/3/2017   2:10 PM                Microsoft Web Tools
d-----        9/29/2017   9:46 AM                Microsoft.NET
d----l        12/3/2017   2:10 PM                Mozilla Maintenance Service
d----l        12/3/2017   2:10 PM                Mozilla Thunderbird
d-----        12/2/2017   8:10 PM                MSBuild
d----l        12/3/2017   2:10 PM                NuGet
d-----        12/3/2017  12:14 PM                NVIDIA Corporation
d-----        12/2/2017   8:10 PM                Reference Assemblies
d----l        12/3/2017   2:10 PM                StarCraft II
d----l        12/3/2017   2:10 PM                Steam
d-----        12/3/2017  12:13 PM                VulkanRT
d-----        9/29/2017  10:41 AM                Windows Defender
d----l        12/3/2017   2:10 PM                Windows Kits
d-----        9/29/2017   9:46 AM                Windows Mail
d-----        9/29/2017  10:42 AM                Windows Media Player
d-----        9/29/2017   9:46 AM                Windows Multimedia Platform
d-----        9/29/2017   9:46 AM                windows nt
d----l        12/3/2017   2:10 PM                Windows Phone Kits
d-----        9/29/2017  10:41 AM                Windows Photo Viewer
d-----        9/29/2017   9:46 AM                Windows Portable Devices
d-----        9/29/2017   9:46 AM                WindowsPowerShell
d----l        12/3/2017   2:10 PM                World of Warcraft
d----l        12/3/2017   2:10 PM                Xamarin
```
