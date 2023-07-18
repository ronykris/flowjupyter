# Flow Jupyter

Flow's command line tool is a powerful way to interact with the blockchain, but it comes with traditional limitations. One of the main disadvantages is that it is difficult to remember the correct commands. There are often many different options available for each command and it can be easy to make mistakes.

For a new member it could be a daunting experience to explore and learn the tool while using it. Also, not having a way to save the chain of commands makes it all the more annoying. Advanced operations like interacting with the blockchain via scripts and transactions are definitely cumbersome for a new member from the terminal. Therefore, a handy web interface similar to a notebook could be very beneficial to a new member of the community.

This idea was conceptualized during discussions in the discord dev channels. We believe this tool can improve developer experience many fold.

### Planned Enhancements

- Auto install of Flow Command Line (if it doesn't exist already)
- Command auto completion support
- Command chaining support
- Improve UX/UI
- Add support to add cadence code in cell
- Dockerise and host

### Test the Kernel

- Install Flow's command line
- Clone Repo
- Edit / update flow.json

Start the kernel
```
python3 -m flowjupyter
```
Verify emulator has started
```
roger@roger:~/dev/flowjupyter$ ps -ef|grep flow
roger    1237520 1055869  0 18:35 ?        00:00:00 flow cadence language-server --enable-flow-client=false
roger    1237784    2185  0 18:36 ?        00:00:00 flow emulator start
roger    1239355 1090745  3 18:57 pts/18   00:00:00 python3 -m flowjupyter
roger    1239423 1230558  0 18:57 pts/20   00:00:00 grep --color=auto flow
roger@roger:~/dev/flowjupyter$ 
```

Execute the following commands
```
flow blocks get latest --network=emulator
flow accounts get f8d6e0586b0a20c7
```