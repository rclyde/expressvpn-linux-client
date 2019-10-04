# expressvpn-linux-client
Tool to automate expressvpn connection on linux

As of 2019, the ExpressVPN client for linux has a few issues.
* does not retry automatically to connect if the connection failed, which can be troublesome in countries where one frequently gets disconnected, and needs to switch server or retry many times.
* on some setups, resolv.conf will be messed up after disconnection
* it only has no GUI

Opening up this repo to solve these issues one at a time.
