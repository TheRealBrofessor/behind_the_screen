# Local Network Check Lab

## Goal

Use your own computer to see basic network information safely.

This lab does not scan other people, break into anything, or touch systems you do not own.

## What You Need

- A Linux machine or Linux terminal
- Internet or local Wi-Fi connection
- Basic terminal access

## Step 1: See Your Network Adapters

Run:

```bash
ip addr
```

Look for names like:

```text
lo
wlan0
enp0s3
eth0
```

Simple meaning:

- `lo` is your loopback adapter. It points back to your own computer.
- `wlan` usually means Wi-Fi.
- `eth` or `enp` usually means wired Ethernet.

## Step 2: See Your Local IP Address

Run:

```bash
hostname -I
```

You may see something like:

```text
192.168.1.25
```

That is usually your local network address.

## Step 3: See Your Default Route

Run:

```bash
ip route
```

Look for a line that starts with:

```text
default via
```

That usually points to your router.

## Step 4: Test DNS and Internet Reachability

Run:

```bash
ping -c 4 example.com
```

If it works, your computer resolved the domain name and reached the server.

If it fails, the problem could be Wi-Fi, routing, DNS, firewall rules, or the network itself.

## Step 5: Write Down What You Found

Use this format:

```text
Computer name:
Local IP address:
Default router/gateway:
Wi-Fi or Ethernet:
Did ping work:
What confused me:
```

## Optional Python Helper

From the repo root, run:

```bash
python3 tools/networking/mini_network_lab.py
```

This prints a beginner-friendly network summary using Python.

## Safety Note

Only inspect your own machine and networks you own or have clear permission to use.

Do not scan random public IP addresses. Do not try to access other devices without permission.
