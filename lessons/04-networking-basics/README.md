# Networking 101

## The Simple Version

Networking is devices talking to each other.

Your phone talks to your router. Your laptop talks to your router. Your router talks to the internet. When you open a website, send a message, stream music, or update an app, networking is happening in the background.

The internet is the big version of networking. Your home Wi-Fi is the smaller version.

## What You Are Learning

By the end of this section, you should understand:

- What a network is
- What an IP address does
- What a router does
- What DNS does
- What ports are
- What packets are
- The difference between LAN and WAN
- How to safely inspect basic network information on your own machine

## Key Terms

### Network

A network is a group of devices that can communicate with each other.

Examples:

- Your phone and laptop on the same Wi-Fi
- A printer connected to your router
- A game console connected by Ethernet
- A website server sending data to your browser

### IP Address

An IP address is like a device address on a network.

Example:

```text
192.168.1.25
```

That address usually means the device is on a private local network, like your home Wi-Fi.

### Router

A router moves traffic between networks.

At home, your router usually connects your local devices to the internet.

### DNS

DNS turns names into IP addresses.

You type:

```text
example.com
```

DNS helps your computer find the IP address behind that name.

### Port

A port is like a numbered door on a device.

Common examples:

```text
80   HTTP web traffic
443  HTTPS secure web traffic
22   SSH remote login
53   DNS lookups
```

### Packet

A packet is a small piece of network data.

Big data gets broken into smaller packets, sent across the network, then rebuilt on the other side.

### LAN and WAN

LAN means local area network. That is your home, office, or small local network.

WAN means wide area network. The internet is the biggest example.

## Safe Beginner Commands

These commands only inspect your own system. They do not attack anything.

```bash
ip addr
ip route
hostname
hostname -I
ping -c 4 example.com
```

What they show:

- `ip addr` shows network adapters and IP addresses.
- `ip route` shows where your computer sends traffic by default.
- `hostname` shows your computer name.
- `hostname -I` shows local IP addresses.
- `ping -c 4 example.com` checks whether your computer can reach a domain.

## Beginner Lab

Open the lab here:

[Local Network Check Lab](../../labs/networking/local-network-check.md)

## Python Helper

There is also a simple Python helper script:

[mini_network_lab.py](../../tools/networking/mini_network_lab.py)

It prints basic network information from your own computer. It is meant to help beginners see what their system already knows about the network.

## What To Remember

Networking is not magic.

It is devices, addresses, names, ports, and packets.

Once you understand that, cybersecurity starts making more sense.
