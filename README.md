## **Computer Networking Systems**

**Note**: These are the assignments that I completed in this course. That means the skeleton of the project was given to us by the instructor and I worked on completing the required tasks.
In this course, we created a simple router and went over the lower level operations that it should be able to do in detail. We also simulated the bufferbloat problem and did some network measurements. The description of each assignment’s tasks can be viewed in a pdf in this repo.

As the starter codes of the assignments of this course are the instructor's property, I have removed most of the implementations from the files. That means this public repo is only an extremely *partial* view of the implementations. Please request to view the complete impelmentation on my private repo.

The following is each of these assignments in detail.


### **`Assignment 1`**

In assignment 1, I wrote a simple router with a static routing table by using *networking* and *socket programming* concepts. The router receives raw Ethernet frames. It processes the packets just like a real router, then forward them to the correct outgoing interface. The goal is to get hands-on experience as to how a router really works. The router receives the Ethernet frames and my job was to create the forwarding logic so packets go to the correct interface.
The router routes packets from an emulated `host` (client) to two emulated application `servers` (HTTP Server 1 and 2) sitting behind the router. The application servers are each running an HTTP server. The router is able to connect the client to these servers using regular client software. Particularly, as a functioning Internet router, it enables us to **`ping`** and **`traceroute`** each of these emulated nodes.
All of the implementations for this assignment is done in the `router` folder, and all other files are for setup purposes.

<p  align="center">
    <kbd><img src="/A1/simple_router.png" style="width:600px;height:400px;"></kbd>
</p>

The picture is from the assignment's handout [*here*](/A1/A1.pdf).

**Note**

This assignment runs on top of **`Mininet`**. Mininet allows you to emulate a topology on a single machine. It provides the needed isolation between the emulated nodes so that your router node can process and forward real Ethernet frames between the hosts like a real router. 

To get started, follow these steps:

1) Download and run the VM `cs144-vm.7z` from your google drive CSC458/A1 (I did not add it to github since it is very large). You might need the `7zip` to extract the `.7z` file. To do that install the `7zip` by:

```
brew install p7zip
```

Then extract the archived file by:

```
7za x file.7z
```

Then `import` its `.ovf` file into the `virtualBox` to create its VM.

2) Enable the `ssh` into the VM by:

- Go to the `Settings` of the VM
- Select one of the free network adapters, like adapter 2. Then check `Enable the Network Adapter`.
- Select the NAT network.
- Open the Advanced options and click on Port Forwarding. Leave other settings as default.
- Click on the `+` icon to add a new rule. The add:

Name: `ssh`
Protocol: `TCP`
Host Port: `3033` (3033 is an arbitary number.)
Guest Port: `22`
Leave other fields empty.

Then you can `ssh` into the VM by:

```
sh mininet@127.0.0.1 -p 3033 -vv
```

The password is `mininet`.

3) Since this VM is the original raw VM that we were provided with, the `router` folder in it has no implementation and so we need to replace it with my own implementation in the folder `router`. So remove the `route` folder that already exists in the projects' VM, by doing `rm -rf router`. Then replace it with my own implementation which is in the folder `router`. To add my own `router` folder, run:

```
scp -r -P 3033 ../router mininet@127.0.0.1:~/cs144_lab3/
```

This will create a new folder called `router` which has my own implementation.


Then follow the instructions in the `Get Started` section of the assignment pdf. Sepcifically, you can see the list of the IP addresses assigned to the emulated hosts and our static routing table by running the followings:

```
cat ~/cs144_lab3/IP_CONFIG
server1 192.168.2.2
server2 172.64.3.10
client    10.0.1.100
sw0-eth1 192.168.2.1
sw0-eth2 172.64.3.1
sw0-eth3 10.0.1.1

cat ~/cs144_lab3/rtable
10.0.1.100  10.0.1.100  255.255.255.255 eth3
192.168.2.2 192.168.2.2 255.255.255.255 eth1
172.64.3.10  172.64.3.10  255.255.255.255 eth2
```


**Running the simple router project**

You can build and run the starter code as follows:

```
cd ~/cs144_lab3/router/
```

Then `make` and run the executable `sr` by:

```
make
```

```
./sr
```

### **Simple Router Operation Examples**

The simple router is able to do the following operations:

```
client ping -c <number-of-times-to-ping> <IP>
```

```
client traceroute -n <IP>
```

```
client wget <IP>
```

The results of running these commands on our router are as follow:

- Pinging from the client to any of the router's interfaces (`192.168.2.1`, `172.64.3.1`, `10.0.1.1`).

<p  align="center">
    <kbd><img src="/A1/ping/client_ping_router_interface1.png" style="width:400px;height:150px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/ping/client_ping_router_interface2.png" style="width:400px;height:150px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/ping/client_ping_router_interface3.png" style="width:400px;height:150px;"></kbd>
</p>

&nbsp;

- Tracerouting from the client to any of the router's interfaces.

<p  align="center">
    <kbd><img src="/A1/traceroute/client_traceroute_router_interface1.png" style="width:500px;height:50px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/traceroute/client_traceroute_router_interface2.png" style="width:500px;height:50px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/traceroute/client_traceroute_router_interface3.png" style="width:500px;height:50px;"></kbd>
</p>

&nbsp;

- Pinging from the client to any of the app servers (`192.168.2.2`, `172.64.3.10`).

<p  align="center">
    <kbd><img src="/A1/ping/client_ping_server1.png" style="width:400px;height:100px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/ping/client_ping_server2.png" style="width:400px;height:100px;"></kbd>
</p>

&nbsp;

- Tracerouting from the client to any of the app servers.

<p  align="center">
    <kbd><img src="/A1/traceroute/client_traceroute_server1.png" style="width:500px;height:80px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/traceroute/client_traceroute_server2.png" style="width:500px;height:80px;"></kbd>
</p>

&nbsp;

- Downloading a file using HTTP from any of the app servers.

<p  align="center">
    <kbd><img src="/A1/http/client_http_server1.png" style="width:400px;height:120px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A1/http/client_http_server2.png" style="width:400px;height:120px;"></kbd>
</p>

&nbsp;

You can view the detailed completion requirements of this assignment [*here*](/A1/A1.pdf) and its tutorial [*here*](/A1/tutorial.pdf).

### **`Assignment 2`**

In assignment 2, I simulated the bufferbloat problem through a *Mininet* topology that could make it occur. The topology for this assignment was the following:

<p  align="center">
    <kbd><img src="/A2/topology.png" style="width:600px;height:400px;"></kbd>
</p>

**Running the VM and SSH**

This Mininet topology was already provided to us inside a virtual machine. 

- Download `cs244‐vm.7z` from your google drive CSC458/A2 (I did not add it to github since it is very large). Then decompress it and import its `cs244‐vm.ova` in the VirtualBox.

- Go to `File -> Host Network Manager` and add a `host-only network adapter`.

- Then enable host-only adapter on newly created VM, by going to `Settings->Network->Adapter 2` and add a `host-only-network adapter` with the name of `vboxnet0`.

- Then start the VM and login. The username and password is `cs244`. 

- Check the available networks in your VM by typing `ifconfig`. You should see both eth0 and eth1. One should have a `192.168.X.X` (host-only) and the other `10.0.X.X` (NATted). If one of the two is missing, run `sudo dhclient ethX` (replace with `eth0` or `eth1`). Check again with `ifconfig`. Write down the IP address for host-only, it should be something like 192.168.56.101. You’ll use this to SSH to your VM shortly.

**Note:** The `h1` has one outgoing interface `eth0` towards `s0` and similarly `h2` has one outgoing interface `eth0` towards `s0`. The router `s0` have two interfaces called `eth1` and `eth2`. The interface `eth0` of `h1` is attached to `eth1` of `s0` and the interface `eth0` of `h2` is attached to `eth2` of `s0`.

- Now you can SSH into this VM by:

```
ssh cs244@192.168.X.X (replace with your host-only IP address)
```

See more in the tutorial pdf [*here*](/A2/tutorial.pdf) and also on the previous course website of this course [*here*](http://www.cs.toronto.edu/~yganjali/courses/csc458/assignments/vm-setup/).


To simulated the bufferbloat problem, as shown in the picture, I performed a **10 secs** simulation in which the following tasks were done *simultaneously*:

- Start a long‐lived TCP flow sending data from `h1` to `h2`, use `iperf`. I recorded the congestion windows size (cwnd) of this connection.

- Send 10 pings per second from `h1` to `h2` and record their RTTs.

- Spawn a webserver on `h1`. Download the index.html web page from h1 repeatedly every two seconds and measure how long it takes to fetch it (on average). Note, I made sure that the webpage download data is going in the same direction as the long‐lived flow (`h1` to `h2`) to make sure the bufferbloat will happen.

To compare the effect of queue sizes, I used different queue sizes (Q=5 packets, Q=20 packets, and Q=100 packets) for the router `s0`.

As we can see in this topology, the link from the router `s0` to `h2` is a bottleneck link. Since packets from `h1` to `s0` can be transferred very fast, but the link from `s0` to `h2` is comparably slow, hence causing the quque at this link (i.e. from `s0` to `h2`) to bloat. Also note that, to successfully simulate this, all of these network operations are from h1 to h2 to make sure this bottleneck link will be filled.


The results of statistics from these simualtion were collected to be plotted. Specifically, I collected the following data:

- The long‐lived TCP flow’s cwnd
- The RTT reported by ping
- Webpage download time
- Queue size at the router

**Running the Simulation**

The main simulation implementation is in `bufferbloat.py` file. To run this simulation and generate the graphs, inside the VM, run the `run.sh` file as:

```
./run.sh
```

The following are the time-series plots of this simulation:

**Download Time in Different Queue Sizes**

<p  align="center">
    <kbd><img src="/A2/bb-q5/download-5.png" style="width:500px;height:300px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A2/bb-q20/download-20.png" style="width:500px;height:300px;"></kbd>
</p>

<p  align="center">
    <kbd><img src="/A2/bb-q100/download-100.png" style="width:500px;height:300px;"></kbd>
</p>

&nbsp;

As demonstrated in the pictures, The *downloadTime* is either below 0.5 secs or greater than 1 sec. So we can see that the buffer sizes of 100 and 5 have a varying *downloadTime* with a greater deviation from an average point. This phenomenon is called packet delay variation or packet jitter...

## Note

**This note continues on my private repo. Since the assignments' starter code is the instructor's property and this is a public repo, I have just provided a partial view of the completed assignments here. Please contact me to view the complete implementations on my private repo. Thank you.**

